from typing import Optional, List, Union, Literal
from singular_client._bases import _Endpoint, ResponseDocList
from singular_client.documents import AdMonetizationDoc
from singular_client.utils import _convert_list_arg


class AdMonetizationEndpoint(_Endpoint[ResponseDocList[AdMonetizationDoc]]):
    endpoint = "v2.0/admonetization/reporting"
    data_path = ["value", "results"]
    res_type = ResponseDocList[AdMonetizationDoc]

    def request(
        self,
        start_date: str,
        end_date: Optional[str] = None,
        time_breakdown: Literal["day", "week", "month", "all"] = "all",
        dimensions: Optional[Union[List[str], str]] = None,
        metrics: Optional[Union[List[str], str]] = None,
        app: Optional[List[str]] = None,
        source: Optional[List[str]] = None,
        filters: Optional[List[dict]] = None,
        format: Literal["json", "csv"] = "json",
        country_code_format: Literal["iso3", "iso"] = "iso3",
    ):
        return super().request(
            start_date=start_date,
            end_date=end_date or start_date,
            time_breakdown=time_breakdown,
            dimensions=_convert_list_arg(dimensions),
            metrics=_convert_list_arg(metrics),
            app=_convert_list_arg(app),
            source=_convert_list_arg(source),
            filters=filters,
            format=format,
            country_code_format=country_code_format,
        )
