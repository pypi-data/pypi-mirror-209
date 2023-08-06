from typing import Optional, List
from singular_client._bases import _Endpoint, ResponseDocList
from singular_client.documents import (
    AppLegacyDoc,
    PartnerLegacyDoc,
    LinkLegacyDoc,
    CustomLinkLegacyDoc,
)
from singular_client.utils import _convert_list_arg


class AppsLegacyEndpoint(_Endpoint[ResponseDocList[AppLegacyDoc]]):
    endpoint = "v1/links/discover_apps"
    data_path = ["available_apps"]
    res_type = ResponseDocList[AppLegacyDoc]


class AvailablePartnersLegacyEndpoint(_Endpoint[ResponseDocList[PartnerLegacyDoc]]):
    endpoint = "v1/links/discover_available_partners"
    data_path = ["available_partners"]
    res_type = ResponseDocList[PartnerLegacyDoc]

    def request(self, singular_app_id: int):
        return super().request(singular_app_id=singular_app_id)


class CreateLinkLegacyEndpoint(_Endpoint[LinkLegacyDoc]):
    endpoint = "v1/links/create"
    data_path = []
    res_type = LinkLegacyDoc
    returns_collection = False
    method = "POST"

    def request(
        self,
        singular_app_id: int,
        singular_partner_id: int,
        tracker_campaign_name: str,
        destination_fallback_url: str,
        destination_deeplink_url: Optional[str] = None,
        destination_universal_link_url: Optional[str] = None,
        deferred_deeplink_enabled: bool = False,
        reengagement_enabled: bool = False,
    ):
        return super().request(
            data=dict(
                singular_app_id=singular_app_id,
                singular_partner_id=singular_partner_id,
                tracker_campaign_name=tracker_campaign_name,
                destination_fallback_url=destination_fallback_url,
                destination_deeplink_url=destination_deeplink_url,
                destination_universal_link_url=destination_universal_link_url,
                deferred_deeplink_enabled=deferred_deeplink_enabled,
                reengagement_enabled=reengagement_enabled,
            ),
        )


class CreateCustomLinkLegacyEndpoint(_Endpoint[CustomLinkLegacyDoc]):
    endpoint = "v1/links/create_custom"
    data_path = []
    res_type = CustomLinkLegacyDoc
    returns_collection = False
    method = "POST"

    def request(
        self,
        ios_singular_app_id: int,
        android_singular_app_id: int,
        custom_source_name: str,
        tracker_campaign_name: str,
        ios_destination_fallback_url: str,
        ios_destination_deeplink_url: Optional[str] = None,
        ios_destination_universal_link_url: Optional[str] = None,
        ios_deferred_deeplink_enabled: Optional[bool] = None,
        android_destination_fallback_url: Optional[str] = None,
        android_destination_deeplink_url: Optional[str] = None,
        android_deferred_deeplink_enabled: Optional[bool] = None,
        reengagement_enabled: Optional[bool] = None,
        other_destination_fallback_url: Optional[str] = None,
    ):
        assert (
            ios_singular_app_id or android_singular_app_id
        ), "Must provide at least one app id"

        if ios_singular_app_id:
            assert (
                ios_destination_fallback_url
            ), "Must provide ios_destination_fallback_url"

        if android_singular_app_id:
            assert (
                android_destination_fallback_url
            ), "Must provide android_destination_fallback_url"

        if ios_deferred_deeplink_enabled:
            assert (
                ios_destination_deeplink_url
            ), "Must provide ios_destination_deeplink_url"

        if android_deferred_deeplink_enabled:
            assert (
                android_destination_deeplink_url
            ), "Must provide android_destination_deeplink_url"

        return super().request(
            data=dict(
                ios_singular_app_id=ios_singular_app_id,
                android_singular_app_id=android_singular_app_id,
                custom_source_name=custom_source_name,
                tracker_campaign_name=tracker_campaign_name,
                ios_destination_fallback_url=ios_destination_fallback_url,
                ios_destination_deeplink_url=ios_destination_deeplink_url,
                ios_destination_universal_link_url=ios_destination_universal_link_url,
                ios_deferred_deeplink_enabled=ios_deferred_deeplink_enabled,
                android_destination_fallback_url=android_destination_fallback_url,
                android_destination_deeplink_url=android_destination_deeplink_url,
                android_deferred_deeplink_enabled=android_deferred_deeplink_enabled,
                reengagement_enabled=reengagement_enabled,
                other_destination_fallback_url=other_destination_fallback_url,
            ),
        )


class ViewLinksLegacyEndpoint(_Endpoint[ResponseDocList[LinkLegacyDoc]]):
    endpoint = "v1/links/view"
    data_path = ["results"]
    res_type = ResponseDocList[LinkLegacyDoc]

    def request(
        self,
        singular_app_ids: Optional[List[str]] = None,
        singular_partner_ids: Optional[List[str]] = None,
        tracking_link_ids: Optional[List[str]] = None,
        include_archived_links: bool = False,
    ):
        return super().request(
            singular_app_ids=_convert_list_arg(singular_app_ids),
            singular_partner_ids=_convert_list_arg(singular_partner_ids),
            tracking_link_ids=_convert_list_arg(tracking_link_ids),
            include_archived_links=include_archived_links,
        )


class ViewCustomLinksLegacyEndpoint(_Endpoint[ResponseDocList[CustomLinkLegacyDoc]]):
    endpoint = "v1/links/view_custom"
    data_path = ["results"]
    res_type = ResponseDocList[CustomLinkLegacyDoc]

    def request(
        self,
        singular_app_ids: Optional[List[str]] = None,
        custom_source_name: Optional[str] = None,
        tracking_link_ids: Optional[List[str]] = None,
        include_archived_links: bool = False,
    ):
        return super().request(
            singular_app_ids=_convert_list_arg(singular_app_ids),
            custom_source_name=custom_source_name,
            tracking_link_ids=_convert_list_arg(tracking_link_ids),
            include_archived_links=include_archived_links,
        )
