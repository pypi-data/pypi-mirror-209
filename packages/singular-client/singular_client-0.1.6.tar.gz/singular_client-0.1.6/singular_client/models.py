"""
Pydantic models for data structures returned by Singular API.

These are not used by this package. Rather, they're here for the user's
convenience, when needed.

Pydantic models validate data at runtime according to the provided types.
Therefore, this package does not use them by default, to avoid breaking
changes when Singular decides to change the data structure of their API.
"""
from typing import (
    List,
    Optional,
    Literal,
    Union,
    Dict,
)
from pydantic import BaseModel


class NameModel(BaseModel):
    display_name: str
    name: str


class IDModel(BaseModel):
    display_name: str
    id: str


class NameValuesModel(BaseModel):
    name: str
    display_name: str
    values: List[NameModel]


# Reporting API
# ==============================================================================


class DataConnectorModel(BaseModel):
    data_connector_id: str
    data_connector_source_name: str
    data_connector_username: str
    is_active_last_30_days: bool
    is_available: bool
    is_empty_data: str
    last_updated_utc: str
    data_connector_timestamp_utc: str
    status: str


class ReportStatusModel(BaseModel):
    status: Literal["DONE", "FAILED", "QUEUED", "STARTED"]
    url_expires_in: int
    generated_url_time_in_utc: str
    url_expired_time_in_utc: str
    download_url: str
    report_id: str


class CohortMetricsModel(BaseModel):
    metrics: List[NameModel]
    periods: List[str]


# [NEW] TRACKING LINKS API
# ==============================================================================


class CreateLinkModel(BaseModel):
    tracking_link_id: str
    tracking_link_name: str
    click_tracking_link: str
    impression_tracking_link: str
    extra_info: List[str]


class Redirection(BaseModel):
    app_site_id: int
    destination_url: str
    destination_deeplink_url: Optional[str] = None
    destination_deferred_deeplink_url: Optional[str] = None


class LinkModel(BaseModel):
    tracking_link_id: str
    tracking_link_name: str
    click_tracking_link: str
    impression_tracking_link: str
    created_utc: str
    modified_utc: str
    link_type: str
    partner_id: int
    app_id: int
    android_redirection: Optional[Redirection] = None
    ios_redirection: Optional[Redirection] = None
    destination_fallback_url: str
    enable_reengagement: bool
    enabled_ctv: bool
    click_deterministic_window: str
    click_probabilistic_window: str
    view_deterministic_window: str
    view_probabilistic_window: str
    click_reengagement_window: Optional[str] = None


class AppModel(BaseModel):
    app_site_id: int
    app_platform: str
    app_store_url: str
    site_public_id: str
    app_id: int
    app: str


class PartnerAppModel(BaseModel):
    app_site_id: int
    app_id: int
    singular_partner_display_name: str
    singular_partner_id: int


class PartnerModel(BaseModel):
    singular_partner_id: int
    singular_partner_display_name: str
    support_multiple_os: bool
    support_reengagement: bool
    support_ctv: bool


class DomainModel(BaseModel):
    subdomain: str
    dns_zone: str


# Legacy Link Management API
# ==============================================================================


class AppLegacyModel(BaseModel):
    singular_app_id: int
    app_name: str
    app_longname: str
    app_platform: str
    app_public_id: str
    admon_revenue_sources: List[str]


class PartnerLegacyModel(BaseModel):
    singular_partner_id: int
    singular_partner_display_name: str


class LinkLegacyModel(BaseModel):
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
    status: Optional[str] = None


class CustomLinkLegacyModel(BaseModel):
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
    status: Optional[str] = None


# Ad Monetization API
# ==============================================================================


class AdMonetizationModel(BaseModel):
    ad_impressions: int
    end_date: str
    app: str
    ad_requests: int
    ad_fill_rate: float
    ad_revenue: float
    source: str
    start_date: str


class ConversionModelModel(BaseModel):
    conversion_name: str
    conversion_type: str
    partner_conversion_name: str
    value: Union[int, Dict[str, int]]


class AppConversionModelModel(BaseModel):
    currency: str
    keepalive_interval: int
    measurement_period: int
    start_ts: int
    update_ts: int
    version: int
    previous_version: int
    conversion_model: Dict[str, List[ConversionModelModel]]
