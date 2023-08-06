"""
Data structures returned by Singular API.

--------------------------------------------------------------------------------
USED FOR STATIC TYPE CHECKING ONLY. These won't be instantiated.
--------------------------------------------------------------------------------

Endpoints are type-hinted using these classes as the structure of an individual
document within a list of documents in a response. They serve two purposes:
1. Easy access by the user for referencing the expected response data structure
2. Static type checking. The user's IDE will bark at them or give red underline
   if they try to access an attribute from a response that is not present.
"""
from typing import (
    TypedDict,
    List,
    Optional,
    Literal,
    Union,
    Dict,
)


class NameDoc(TypedDict):
    display_name: str
    name: str


class IDDoc(TypedDict):
    display_name: str
    id: str


class NameValuesDoc(TypedDict):
    name: str
    display_name: str
    values: List[NameDoc]


# Reporting API
# ==============================================================================


class DataConnectorDoc(TypedDict):
    data_connector_id: str
    data_connector_source_name: str
    data_connector_username: str
    is_active_last_30_days: bool
    is_available: bool
    is_empty_data: str
    last_updated_utc: str
    data_connector_timestamp_utc: str
    status: str


class ReportStatusDoc(TypedDict):
    status: Literal["DONE", "FAILED", "QUEUED", "STARTED"]
    url_expires_in: int
    generated_url_time_in_utc: str
    url_expired_time_in_utc: str
    download_url: str
    report_id: str


class CohortMetricsDoc(TypedDict):
    metrics: List[NameDoc]
    periods: List[str]


# [NEW] TRACKING LINKS API
# ==============================================================================


class CreateLinkDoc(TypedDict):
    tracking_link_id: str
    tracking_link_name: str
    click_tracking_link: str
    impression_tracking_link: str
    extra_info: List[str]


class Redirection(TypedDict, total=False):
    app_site_id: int
    destination_url: str
    destination_deeplink_url: Optional[str]
    destination_deferred_deeplink_url: Optional[str]


class LinkDoc(TypedDict, total=False):
    tracking_link_id: str
    tracking_link_name: str
    click_tracking_link: str
    impression_tracking_link: str
    created_utc: str
    modified_utc: str
    link_type: str
    partner_id: int
    app_id: int
    android_redirection: Redirection
    ios_redirection: Redirection
    destination_fallback_url: str
    enable_reengagement: bool
    enabled_ctv: bool
    click_deterministic_window: str
    click_probabilistic_window: str
    view_deterministic_window: str
    view_probabilistic_window: str
    click_reengagement_window: Optional[str]


class AppDoc(TypedDict):
    app_site_id: int
    app_platform: str
    app_store_url: str
    site_public_id: str
    app_id: int
    app: str


class PartnerAppDoc(TypedDict):
    app_site_id: int
    app_id: int
    singular_partner_display_name: str
    singular_partner_id: int


class PartnerDoc(TypedDict):
    singular_partner_id: int
    singular_partner_display_name: str
    support_multiple_os: bool
    support_reengagement: bool
    support_ctv: bool


class DomainDoc(TypedDict):
    subdomain: str
    dns_zone: str


# Legacy Link Management API
# ==============================================================================


class AppLegacyDoc(TypedDict):
    singular_app_id: int
    app_name: str
    app_longname: str
    app_platform: str
    app_public_id: str
    admon_revenue_sources: List[str]


class PartnerLegacyDoc(TypedDict):
    singular_partner_id: int
    singular_partner_display_name: str


class LinkLegacyDoc(TypedDict, total=False):
    app_longname: str
    app_platform: str
    singular_app_id: int
    singular_partner_id: int
    singular_partner_display_name: str
    tracking_link_id: int
    tracker_campaign_name: str
    destination_fallback_url: str
    destination_deeplink_url: str
    deferred_deeplink_enabled: bool
    reengagement_enabled: bool
    click_tracking_link: str
    impression_tracking_link: str
    created_utc: str
    updated_utc: str
    # `status` not included in Create Link response
    status: Optional[str]


class CustomLinkLegacyDoc(TypedDict, total=False):
    custom_source_name: str
    tracker_campaign_name: str
    ios_singular_app_id: int
    ios_app_longname: str
    ios_destination_fallback_url: str
    ios_destination_deeplink_url: str
    ios_deferred_deeplink_enabled: bool
    android_singular_app_id: int
    android_app_longname: str
    android_destination_fallback_url: str
    android_deferred_deeplink_enabled: bool
    reengagement_enabled: bool
    other_destination_fallback_url: str
    click_tracking_link: str
    impression_tracking_link: str
    tracking_link_id: int
    created_utc: str
    updated_utc: str
    # `status` not included in Create Link response
    status: Optional[str]


# Ad Monetization API
# ==============================================================================


class AdMonetizationDoc(TypedDict):
    ad_impressions: int
    end_date: str
    app: str
    ad_requests: int
    ad_fill_rate: float
    ad_revenue: float
    source: str
    start_date: str


class ConversionModelDoc(TypedDict):
    conversion_name: str
    conversion_type: str
    partner_conversion_name: str
    value: Union[int, Dict[str, int]]


class AppConversionModelDoc(TypedDict):
    currency: str
    keepalive_interval: int
    measurement_period: int
    start_ts: int
    update_ts: int
    version: int
    previous_version: int
    conversion_model: Dict[str, List[ConversionModelDoc]]
