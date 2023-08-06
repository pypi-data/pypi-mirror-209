"""Словари используемые в модуле main."""
from collections import namedtuple
from enum import Enum


class Filter(Enum):
    SmartisID = 7071
    Channel = 1222
    Placement = 1223


MethodFields = namedtuple("MethodFields", "method location id")


class Method(Enum):
    get_projects = MethodFields("projects/get", "projects", "project")
    get_metrics = MethodFields("metrics/get", "metrics", "code")
    get_groupings = MethodFields("reports/getGroupings", "groupings", "code")
    get_attributions = MethodFields("reports/getModelAttributions", "modelAttributions", "id")
    get_channels = MethodFields("reports/getChannels", "", "")
    get_placements = MethodFields("reports/getPlacements", "", "")
    get_campaigns = MethodFields("reports/getCampaigns", "", "")
    get_ads = MethodFields("reports/getAds", "", "")
    get_keywords = MethodFields("reports/getKeywords", "", "")
    get_crm_custom_fields = MethodFields("crm/crmCustomField/get", "crmCustomFields", "")
    get_crm_custom_field_groups = MethodFields("crm/crmCustomFieldGroup/get", "crmCustomFieldGroups", "")


class GroupBy(Enum):
    ADS = "ad_id"
    DAY = "day"
    PLACEMENT = "placement_id"
    CAMPAIGN = "campaigns"
    OBJECTS = "smartis_object"


class FilterCategory(Enum):
    SMARTIS_ID = 7071
    CHANNEL = 1222
    PLACEMENT = 1223


class AttributionModel(Enum):
    LAST_CLICK = 1  # Последнее касание
    FIRST_CLICK = 2  # Первое касание
    LINEAR = 3  # Линейное распределение
    BY_POSITION = 4  # На основе позиции
    FIRST_COMMUNICATION = 5  # Первое обращение
    LINEAR_BY_COMMUNICATION = 6  # Линейное распределение на обращениях
    LINEAR_WITH_POSTVIEW = 10  # Линейное распределение с учетом postview
    LAST_CLICK_WITH_POSTVIEW = 15  # Последнее касание с учетом postview
    FIRST_CLICK_WITH_POSTVIEW = 16  # Первое касание с учетом postview
    NOT_FIRST_NOT_LAST_CLICK = 17  # Не первое и не последнее
    LAST_COMMUNICATION = 22  # Последнее обращение
    BY_POSITION_WITH_POSTVIEW = 23  # На основе позиции с учетом postview


class TypeReport(Enum):
    RAW = "raw"
    AGGREGATED = "aggregated"
