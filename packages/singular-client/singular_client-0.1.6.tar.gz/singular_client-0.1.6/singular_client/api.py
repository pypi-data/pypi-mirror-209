from __future__ import annotations
import requests
import os
from typing import (
    Optional,
    Literal,
    TYPE_CHECKING,
)
from singular_client._bases import ResponseSchema

if TYPE_CHECKING:
    from singular_client.endpoints import *


class SingularAPI:
    """
    Stores endpoint instances and handles authentication, sending request arguments,

    Passes a reference to itself to each endpoint instance, so that they can access
    our request method and other endpoints, if needed.

    AUTHENTICATION
    --------------
    Passing a key is not necessary if an environment variable named `SINGULAR_API_KEY`
    can be found.
    """

    base_url = "https://api.singular.net/api/"
    logs = True
    key: str

    # Reporting
    combined_report: "CombinedReportEndpoint"
    data_availability: "DataAvailabilityEndpoint"
    report_status: "ReportStatusEndpoint"
    filters: "FiltersEndpoint"
    custom_dimensions: "CustomDimensionsEndpoint"
    cohort_metrics: "CohortMetricsEndpoint"
    conversion_metrics: "ConversionMetricsEndpoint"
    # SKAdNetwork
    skan_raw_report: "SkanRawReportEndpoint"
    skan_report: "SkanReportEndpoint"
    skan_events: "SkanEventsEndpoint"
    # Links
    create_link: "CreateLinkEndpoint"
    view_links: "ViewLinksEndpoint"
    apps: "AppsEndpoint"
    configured_partners: "ConfiguredPartnersEndpoint"
    domains: "DomainsEndpoint"
    all_partners: "AllPartnersEndpoint"
    # Links (Legacy)
    apps_legacy: "AppsLegacyEndpoint"
    available_partners_legacy: "AvailablePartnersLegacyEndpoint"
    link_legacy: "CreateLinkLegacyEndpoint"
    view_links_legacy: "ViewLinksLegacyEndpoint"
    custom_link_legacy: "CreateCustomLinkLegacyEndpoint"
    view_custom_links_legacy: "ViewCustomLinksLegacyEndpoint"
    # Ad Monetization
    ad_monetization: "AdMonetizationEndpoint"
    # Governance (graphql)
    graphql: "GraphQLEndpoint"

    def __init__(self, key: Optional[str] = None):
        if not key:
            key = os.environ.get("SINGULAR_API_KEY")
            assert key, "No API key provided"

        self.key = key

        from singular_client import endpoints

        self.combined_report = endpoints.CombinedReportEndpoint(self)
        self.data_availability = endpoints.DataAvailabilityEndpoint(self)
        self.report_status = endpoints.ReportStatusEndpoint(self)
        self.filters = endpoints.FiltersEndpoint(self)
        self.custom_dimensions = endpoints.CustomDimensionsEndpoint(self)
        self.cohort_metrics = endpoints.CohortMetricsEndpoint(self)
        self.conversion_metrics = endpoints.ConversionMetricsEndpoint(self)
        self.skan_raw_report = endpoints.SkanRawReportEndpoint(self)
        self.skan_report = endpoints.SkanReportEndpoint(self)
        self.skan_events = endpoints.SkanEventsEndpoint(self)
        self.create_link = endpoints.CreateLinkEndpoint(self)
        self.view_links = endpoints.ViewLinksEndpoint(self)
        self.apps = endpoints.AppsEndpoint(self)
        self.configured_partners = endpoints.ConfiguredPartnersEndpoint(self)
        self.domains = endpoints.DomainsEndpoint(self)
        self.all_partners = endpoints.AllPartnersEndpoint(self)
        self.apps_legacy = endpoints.AppsLegacyEndpoint(self)
        self.available_partners_legacy = endpoints.AvailablePartnersLegacyEndpoint(self)
        self.link_legacy = endpoints.CreateLinkLegacyEndpoint(self)
        self.view_links_legacy = endpoints.ViewLinksLegacyEndpoint(self)
        self.custom_link_legacy = endpoints.CreateCustomLinkLegacyEndpoint(self)
        self.view_custom_links_legacy = endpoints.ViewCustomLinksLegacyEndpoint(self)
        self.ad_monetization = endpoints.AdMonetizationEndpoint(self)
        self.graphql = endpoints.GraphQLEndpoint(self)

    def request(
        self,
        endpoint: str,
        method: Literal["GET", "POST", "PUT", "DELETE"] = "GET",
        params=None,
        headers=None,
        data=None,
        key_in_headers: Optional[bool] = None,
    ) -> dict:
        url = self.base_url + endpoint

        # Default to None instead of dict because mutable defaults persist
        if not params:
            params = dict()
        if not headers:
            headers = dict()
        if not data:
            data = dict()

        # We can usually determine where to place auth key by checking if it's
        # a v1 endpoint. `key_in_headers` can be used to override this.
        if key_in_headers is None:
            key_in_headers = "v1" in url

        if key_in_headers:
            headers["Authorization"] = self.key
        else:
            params["api_key"] = self.key

        res = requests.request(
            method, url=url, params=params, headers=headers, data=data
        )

        assert (code := res.status_code) == 200, (code, res.text)

        # return UtilDict(res.json()).deep_uniform()
        return res.json()

    @property
    def endpoints(self) -> ResponseSchema:
        """
        Returns a dictionary of the attribute name of all endpoints, and their
        types. Useful for printing out and displaying.
        """
        from singular_client import endpoints

        return ResponseSchema(
            {
                attr_name: getattr(endpoints, attr_type.strip("'"))
                if not isinstance(attr_type, type)
                else attr_type
                for attr_name, attr_type in type(self).__annotations__.items()
                if not attr_name.startswith("_") and not attr_name == "key"
            }
        )
