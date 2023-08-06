from typing import (
    List,
    Optional,
    Literal,
)
from singular_client._bases import _Endpoint, ResponseDocList
from singular_client.documents import (
    DomainDoc,
    AppDoc,
    PartnerDoc,
    PartnerAppDoc,
    CreateLinkDoc,
    Redirection,
    LinkDoc,
)
from singular_client.utils import _convert_list_arg


class DomainsEndpoint(_Endpoint[ResponseDocList[DomainDoc]]):
    endpoint = "v1/singular_links/domains"
    data_path = ["available_domains"]
    res_type = ResponseDocList[DomainDoc]


class AppsEndpoint(_Endpoint[ResponseDocList[AppDoc]]):
    endpoint = "v1/singular_links/apps"
    data_path = ["available_apps"]
    res_type = ResponseDocList[AppDoc]


class AllPartnersEndpoint(_Endpoint[ResponseDocList[PartnerDoc]]):
    endpoint = "v1/singular_links/all_partners"
    data_path = ["partners"]
    res_type = ResponseDocList[PartnerDoc]

    def request(self, singular_partner_id: Optional[List[str]] = None):
        return super().request(
            singular_partner_id=_convert_list_arg(singular_partner_id)
        )


class CreateLinkEndpoint(_Endpoint[CreateLinkDoc]):
    endpoint = "v1/singular_links/links"
    data_path = []
    res_type = CreateLinkDoc
    returns_collection = False
    method = "POST"

    def request(
        self,
        app_id: int,
        partner_id: int,
        tracking_link_name: str,
        link_dns_zone: str,
        link_subdomain: str,
        destination_fallback_url: str,
        link_type: Literal["partner", "custom"] = "partner",
        android_redirection: Optional[Redirection] = None,
        ios_redirection: Optional[Redirection] = None,
        enable_reengagement: Optional[bool] = None,
        click_deterministic_window: Optional[int] = None,
        click_probabilistic_window: Optional[int] = None,
        view_deterministic_window: Optional[int] = None,
        view_probabilistic_window: Optional[int] = None,
        click_reengagement_window: Optional[int] = None,
        enable_ctv: Optional[bool] = None,
    ):
        assert (
            android_redirection or ios_redirection
        ), "Must provide at least one redirection"

        if click_reengagement_window:
            assert (
                enable_reengagement
            ), "enable_reengagement must be True if click_reengagement_window is set"

        if click_deterministic_window:
            assert (
                0 <= click_deterministic_window <= 30
            ), "click_deterministic_window 0 to 30"

        if click_probabilistic_window:
            assert (
                0 <= click_probabilistic_window <= 24
            ), "click_probabilistic_window 0 to 24"

        if view_deterministic_window:
            assert (
                0 <= view_deterministic_window <= 24
            ), "view_deterministic_window 0 to 24"

        return super().request(
            data=dict(
                app_id=app_id,
                partner_id=partner_id,
                tracking_link_name=tracking_link_name,
                link_dns_zone=link_dns_zone,
                link_subdomain=link_subdomain,
                destination_fallback_url=destination_fallback_url,
                link_type=link_type,
                android_redirection=android_redirection,
                ios_redirection=ios_redirection,
                enable_reengagement=enable_reengagement,
                click_deterministic_window=click_deterministic_window,
                click_probabilistic_window=click_probabilistic_window,
                view_deterministic_window=view_deterministic_window,
                view_probabilistic_window=view_probabilistic_window,
                click_reengagement_window=click_reengagement_window,
                enable_ctv=enable_ctv,
            ),
        )


class ViewLinksEndpoint(_Endpoint[ResponseDocList[LinkDoc]]):
    endpoint = "v1/singular_links/links"
    data_path = []
    res_type = ResponseDocList[LinkDoc]

    def request(
        self,
        link_type: Optional[Literal["custom", "partner", "mobile_web_to_app"]] = None,
        partner_id: Optional[str] = None,
        app_id: Optional[str] = None,
        app_site_id: Optional[str] = None,
        tracking_link_id: Optional[str] = None,
    ):
        return super().request(
            link_type=link_type,
            partner_id=partner_id,
            app_id=app_id,
            app_site_id=app_site_id,
            tracking_link_id=tracking_link_id,
        )


class ConfiguredPartnersEndpoint(_Endpoint[ResponseDocList[PartnerAppDoc]]):
    endpoint = "v1/singular_links/configured_partners"
    data_path = ["available_partners"]
    res_type = ResponseDocList[PartnerAppDoc]

    def request(
        self,
        app_site_id: Optional[List[str]] = None,
        partner_id: Optional[List[str]] = None,
    ):
        return super().request(
            app_site_id=_convert_list_arg(app_site_id),
            partner_id=_convert_list_arg(partner_id),
        )
