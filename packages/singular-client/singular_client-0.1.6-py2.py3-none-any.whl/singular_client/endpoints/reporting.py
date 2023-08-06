"""
General Async Reporting Endpoints
=================================

Async reporting for network and tracker data. Includes a variety of
helper-endpoints to quickly retrieve the information needed to make an async reporting
request.

Once you're ready to create a report, here is some example code:
```
api = SingularAPI(<api key>)
report_queue = api.combined_report(...)
while not (status := report_queue.check_status()):
    time.sleep(10)
if status.failed:
    raise Exception("Report failed")
data = status.read()
```

https://support.singular.net/hc/en-us/articles/360045245692-Reporting-API-Reference?navigation_side_bar=true
"""
from typing import (
    TYPE_CHECKING,
    Optional,
    Union,
    List,
    Dict,
    Literal,
    cast,
)
from singular_client._bases import _Endpoint, ResponseDocList
from singular_client.documents import (
    ReportStatusDoc,
    NameValuesDoc,
    CohortMetricsDoc,
    IDDoc,
    NameDoc,
    DataConnectorDoc,
)
from singular_client.utils import _convert_list_arg
import json
import time
import requests
import io

if TYPE_CHECKING:
    from singular_client.api import SingularAPI
    import pandas as pd


class ReportStatusResponse:
    """
    Returned by a check on the status of a report, through the ReportStatusEndpoint,
    or indirectly, through the CreateReportResponse object.

    Its boolean value is True if the report is done, OR if it has failed.
    """

    cached_download: Optional[Union[requests.Response, "pd.DataFrame"]]
    raw: ReportStatusDoc
    failed = property(lambda x: x.raw["status"] == "FAILED")
    done = property(lambda x: x.raw["status"] == "DONE")
    queued = property(lambda x: x.raw["status"] == "QUEUED")
    started = property(lambda x: x.raw["status"] == "STARTED")
    url = property(lambda x: x.raw["download_url"])

    def __init__(self, doc: dict):
        self.raw = cast(ReportStatusDoc, doc)
        self.cached_download = None

    def __bool__(self) -> bool:
        return self.done or self.failed

    def read(self, no_cache: bool = False) -> Union[dict, "pd.DataFrame"]:
        """
        Download from `status['download_url']`, and read the report without knowing
        whether it is a json or csv report.
        ---
        - If csv, pandas is required.
        - Downloaded response data is cached regardless of whether read errors are raised.
        """
        assert self.done, "Report must be done to read it."

        if self.cached_download and not no_cache:
            res = self.cached_download
        else:
            res = requests.get(self.raw["download_url"])
            self.cached_download = res
        try:
            return res.json()
        except json.JSONDecodeError:
            try:
                import pandas as pd
            except ImportError:
                raise Exception("Pandas is required to read a csv report.")
            buffer = io.BytesIO(res.content)
            return pd.read_csv(buffer, index_col=None)


class ReportStatusEndpoint(_Endpoint[ReportStatusResponse]):
    """
    Check the status of a report, by ID.

    - Rate limited to 1 request per 10 seconds, per report.

    Returns a ReportStatusResponse object, whose boolean value indicates
    whether the report is ready. If True, the report can be downloaded with
    its `.read()` method.
    """

    endpoint = "v2.0/get_report_status"
    data_path = ["value"]
    res_type = ReportStatusResponse
    cacheable = False
    request_times: Dict[str, float] = {}
    returns_collection = False
    report_id: str

    def request(self, report_id: str) -> ReportStatusResponse:
        recent_time = self.request_times.get(report_id, 0)
        if time.time() - recent_time < 10:
            raise Exception("Rate limited to 1 request per 10 seconds, per report.")
        self.request_times[report_id] = time.time()
        return super().request(report_id=report_id)


class FiltersEndpoint(_Endpoint[ResponseDocList[NameValuesDoc]]):
    endpoint = "v2.0/reporting/filters"
    data_path = ["value", "dimensions"]
    res_type = ResponseDocList[NameValuesDoc]


class CohortMetricsEndpoint(_Endpoint[CohortMetricsDoc]):
    endpoint = "cohort_metrics"
    data_path = ["value"]
    res_type = CohortMetricsDoc
    returns_collection = False


class CustomDimensionsEndpoint(_Endpoint[ResponseDocList[IDDoc]]):
    endpoint = "custom_dimensions"
    data_path = ["value", "custom_dimensions"]
    res_type = ResponseDocList[IDDoc]


class ConversionMetricsEndpoint(_Endpoint[ResponseDocList[NameDoc]]):
    endpoint = "conversion_metrics"
    data_path = ["value", "metrics"]
    res_type = ResponseDocList[NameDoc]


class DataAvailabilityEndpoint(_Endpoint[ResponseDocList[DataConnectorDoc]]):
    endpoint = "v2.0/data_availability_status"
    data_path = ["value", "data_connectors"]
    res_type = ResponseDocList[DataConnectorDoc]

    def request(
        self,
        data_date: str,
        format: Literal["json", "csv"] = "json",
        expanded: bool = True,
        display_non_active_sources: bool = False,
    ):
        return super().request(
            format=format,
            data_date=data_date,
            expanded=expanded,
            display_non_active_sources=display_non_active_sources,
        )


class CreateReportResponse(str):
    api: "SingularAPI"
    # Response gets cached whent the report has failed or completed,
    # so requests can no longer be sent after that.
    cached_status: Optional[ReportStatusResponse]

    def check_status(self, api: Optional["SingularAPI"] = None) -> ReportStatusResponse:
        if hasattr(self, "cached_status") and self.cached_status:
            return self.cached_status

        assert api or self.api, "An API must be provided"
        if not api:
            api = self.api

        status = api.report_status.request(str(self))
        if status:
            self.cached_status = status
        return status


class CombinedReportEndpoint(_Endpoint[CreateReportResponse]):
    """
    This subclass of _Endpoint solves the problem that Singular does not offer a way to
    control which type of data is returned by the 'Create Async Report' endpoint.

    The 'Create Async Report' endpoint offers 3 options for the types of data returned,
    but the only way to control which report is returned is by the dimensions and
    metrics provided.

    Child classes should subscript this class with a dimension type and a metric
    type. Each should be a `Literal[...]` whose arguments are the valid columns
    that can be chosen. This class applies those types as type hints for the `dimensions`
    and `metrics` arguments of the `post` method. As a result, the user's type checker
    will immediately report issues if they try to pass invalid columns to the `post`
    method of their chosen report type.

    The user can easily override this type checking if they first join their list
    of columns as a comma-separated string.
    """

    endpoint = "v2.0/create_async_report"
    data_path = ["value", "report_id"]
    res_type = CreateReportResponse
    returns_collection = False
    method = "POST"

    def request(
        self,
        start_date: str,
        time_breakdown: Literal["day", "week", "month", "all"] = "all",
        end_date: Optional[str] = None,
        dimensions: Optional[Union[List[str], str]] = None,
        metrics: Optional[Union[List[str], str]] = None,
        custom_dimensions: Optional[List[str]] = None,
        cohort_metrics: Optional[List[str]] = None,
        cohort_periods: Optional[List[str]] = None,
        app: Optional[List[str]] = None,
        source: Optional[List[str]] = None,
        filters: Optional[List[dict]] = None,
        format: Literal["json", "csv"] = "csv",
        country_code_format: Literal["iso3", "iso"] = "iso3",
        display_alignment: bool = False,
        display_unenriched: bool = False,
    ):
        dimensions_str = _convert_list_arg(dimensions)
        if custom_dimensions:
            dimensions_str += "," + _convert_list_arg(custom_dimensions)
        report_id = super().request(
            data=dict(
                start_date=start_date,
                end_date=end_date or start_date,
                time_breakdown=time_breakdown,
                dimensions=dimensions_str,
                metrics=_convert_list_arg(metrics),
                custom_dimensions=_convert_list_arg(custom_dimensions),
                cohort_metrics=_convert_list_arg(cohort_metrics),
                cohort_periods=_convert_list_arg(cohort_periods),
                app=_convert_list_arg(app),
                source=_convert_list_arg(source),
                filters=filters,
                format=format,
                country_code_format=country_code_format,
                display_alignment=display_alignment,
                display_unenriched=display_unenriched,
            ),
        )
        report_id.api = self.api
        return report_id
