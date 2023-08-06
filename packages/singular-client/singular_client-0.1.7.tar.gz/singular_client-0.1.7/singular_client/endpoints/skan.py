"""
SKAN Reporting:
    Skan Raw
    Skan
    Skan Events

https://support.singular.net/hc/en-us/articles/360056377792-Singular-SKAdNetwork-API-Reference?navigation_side_bar=true#Create_Async_SKAdNetwork_Raw_Report_Endpoint
"""
from typing import Literal, Optional, List, Union
from singular_client._bases import _Endpoint, ResponseDocList
from singular_client.documents import NameDoc
from singular_client.endpoints.reporting import CreateReportResponse
from singular_client.utils import _convert_list_arg


class SkanEventsEndpoint(_Endpoint[ResponseDocList[NameDoc]]):
    """
    Retrieve a list of available SKAN events for use in Create Async SKAdNetwork
    Report queries. Events are displayed as "display_name" and "name" pairs.
    """

    endpoint = "v2.0/skan_events"
    data_path = ["value", "skan_events"]
    res_type = ResponseDocList[NameDoc]


class SkanRawReportEndpoint(_Endpoint[CreateReportResponse]):
    """
    Query an asynchronous report for raw SKAdNetwork data collected from postbacks.
    This endpoint provides the number of SKAdNetwork conversions per network and app.
    """

    endpoint = "v2.0/create_async_skadnetwork_raw_report"
    data_path = ["value", "report_id"]
    res_type = CreateReportResponse
    returns_collection = False
    method = "POST"

    def request(
        self,
        start_date: str,
        time_breakdown: Literal["day", "week", "month", "all"] = "all",
        end_date: Optional[str] = None,
        skadnetwork_date_type: Literal[
            "skan_postback_date", "estimated_install_date"
        ] = "skan_postback_date",
        dimensions: Optional[Union[List[str], str]] = None,
        metrics: Optional[Union[List[str], str]] = None,
        app: Optional[List[str]] = None,
        source: Optional[List[str]] = None,
        filters: Optional[List[dict]] = None,
        format: Literal["json", "csv"] = "csv",
        country_code_format: Literal["iso3", "iso"] = "iso3",
    ):
        report_id = super().request(
            data=dict(
                start_date=start_date,
                end_date=end_date or start_date,
                time_breakdown=time_breakdown,
                skadnetwork_date_type=skadnetwork_date_type,
                dimensions=_convert_list_arg(dimensions),
                metrics=_convert_list_arg(metrics),
                app=_convert_list_arg(app),
                source=_convert_list_arg(source),
                filters=filters,
                format=format,
                country_code_format=country_code_format,
            ),
        )
        report_id.api = self.api
        return report_id


class SkanReportEndpoint(_Endpoint[CreateReportResponse]):
    """
    Generate an asynchronous report query for SKAdNetwork data combined with ad network
    and tracker data. Use it to measure metrics like CPI, click-through rate,
    etc., for SKAdNetwork campaigns, grouped by network and/or campaign.
    """

    endpoint = "v2.0/create_async_skadnetwork_report"
    data_path = ["value", "report_id"]
    res_type = CreateReportResponse
    returns_collection = False
    method = "POST"

    def request(
        self,
        start_date: str,
        time_breakdown: Literal["day", "week", "month", "all"] = "all",
        end_date: Optional[str] = None,
        skadnetwork_date_type: Literal[
            "skan_postback_date", "estimated_install_date"
        ] = "skan_postback_date",
        dimensions: Optional[Union[List[str], str]] = None,
        metrics: Optional[Union[List[str], str]] = None,
        skan_events: Optional[List[str]] = None,
        format: Literal["json", "csv"] = "csv",
    ):
        report_id = super().request(
            data=dict(
                start_date=start_date,
                end_date=end_date or start_date,
                time_breakdown=time_breakdown,
                skadnetwork_date_type=skadnetwork_date_type,
                dimensions=_convert_list_arg(dimensions),
                metrics=_convert_list_arg(metrics),
                skan_events=_convert_list_arg(skan_events),
                format=format,
            ),
        )
        report_id.api = self.api
        return report_id
