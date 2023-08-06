from singular_client.api import SingularAPI
from singular_client.endpoints import (
    # Reporting
    ReportStatusResponse,
    ReportStatusEndpoint,
    FiltersEndpoint,
    CohortMetricsEndpoint,
    CustomDimensionsEndpoint,
    ConversionMetricsEndpoint,
    DataAvailabilityEndpoint,
    CreateReportResponse,
    CombinedReportEndpoint,
    # SKAN
    SkanEventsEndpoint,
    SkanRawReportEndpoint,
    SkanReportEndpoint,
    # Apps
    DomainsEndpoint,
    AppsEndpoint,
    AllPartnersEndpoint,
    CreateLinkEndpoint,
    ViewLinksEndpoint,
    ConfiguredPartnersEndpoint,
    # Apps Legacy
    AppsLegacyEndpoint,
    AvailablePartnersLegacyEndpoint,
    CreateLinkLegacyEndpoint,
    CreateCustomLinkLegacyEndpoint,
    ViewLinksLegacyEndpoint,
    ViewCustomLinksLegacyEndpoint,
    # Ad Monetization
    AdMonetizationEndpoint,
    # Governance
    GraphQLEndpoint,
)

from singular_client.documents import (
    NameDoc,
    IDDoc,
    NameValuesDoc,
    DataConnectorDoc,
    ReportStatusDoc,
    CohortMetricsDoc,
    CreateLinkDoc,
    LinkDoc,
    AppDoc,
    PartnerAppDoc,
    PartnerDoc,
    Redirection,
    DomainDoc,
    AppLegacyDoc,
    PartnerLegacyDoc,
    LinkLegacyDoc,
    CustomLinkLegacyDoc,
    AdMonetizationDoc,
    ConversionModelDoc,
    AppConversionModelDoc,
)

import sys

if 'pydantic' in sys.modules:
    from singular_client.models import (
        NameModel,
        IDModel,
        NameValuesModel,
        DataConnectorModel,
        ReportStatusModel,
        CohortMetricsModel,
        CreateLinkModel,
        LinkModel,
        AppModel,
        PartnerAppModel,
        PartnerModel,
        Redirection,
        DomainModel,
        AppLegacyModel,
        PartnerLegacyModel,
        LinkLegacyModel,
        CustomLinkLegacyModel,
        AdMonetizationModel,
        ConversionModelModel,
        AppConversionModelModel,
    )
