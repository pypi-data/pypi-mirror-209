import logging

from cachelib.redis import RedisCache
from celery.schedules import crontab

# https://superset.apache.org/docs/installation/configuring-superset
SECRET_KEY = "{{ CAIRN_SUPERSET_SECRET_KEY }}"
SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://{{ CAIRN_POSTGRESQL_USERNAME }}:{{ CAIRN_POSTGRESQL_PASSWORD }}@cairn-postgresql/{{ CAIRN_POSTGRESQL_DATABASE }}"

# Languages
# https://github.com/apache/superset/blob/dc575080d7e43d40b1734bb8f44fdc291cb95b11/superset/config.py#L324
available_languages = {
    "en": {"flag": "us", "name": "English"},
    "es": {"flag": "es", "name": "Spanish"},
    "it": {"flag": "it", "name": "Italian"},
    "fr": {"flag": "fr", "name": "French"},
    "zh": {"flag": "cn", "name": "Chinese"},
    "ja": {"flag": "jp", "name": "Japanese"},
    "de": {"flag": "de", "name": "German"},
    "pt": {"flag": "pt", "name": "Portuguese"},
    "pt_BR": {"flag": "br", "name": "Brazilian Portuguese"},
    "ru": {"flag": "ru", "name": "Russian"},
    "ko": {"flag": "kr", "name": "Korean"},
    "sl": {"flag": "si", "name": "Slovenian"},
}
{#- https://github.com/apache/superset/blob/master/docs/docs/contributing/translations.mdx#enabling-language-selection #}
enabled_language_codes = ["en"]
LANGUAGES = {}
if "{{ CAIRN_SUPERSET_LANGUAGE_CODE }}" in available_languages:
    enabled_language_codes.append("{{ CAIRN_SUPERSET_LANGUAGE_CODE }}")
    # Set the platform default language/locale
    BABEL_DEFAULT_LOCALE = "{{ CAIRN_SUPERSET_LANGUAGE_CODE }}"
for code in enabled_language_codes:
    LANGUAGES[code] = available_languages[code]

# Borrowed from superset/docker/pythonpath_dev/superset_config.py
REDIS_HOST = "{{ REDIS_HOST }}"
REDIS_PORT = "{{ REDIS_PORT }}"
# Be careful not to conflict with Open edX here
REDIS_CELERY_DB = {{ OPENEDX_CELERY_REDIS_DB + 2 }}
REDIS_CACHE_DB = {{ OPENEDX_CACHE_REDIS_DB + 2 }}

# Charting data queried from datasets cache (optional)
DATA_CACHE_CONFIG = {
    "CACHE_TYPE": "redis",
    "CACHE_DEFAULT_TIMEOUT": 60 * 60 * 24,  # 1 day default (in secs)
    "CACHE_KEY_PREFIX": "superset_data_cache",
    "CACHE_REDIS_URL": f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_CACHE_DB}",
}
# Metadata cache (optional)
CACHE_CONFIG = DATA_CACHE_CONFIG
# SQL Lab query results cache (optional)
RESULTS_BACKEND = RedisCache(
    host=REDIS_HOST,
    port=REDIS_PORT,
    db=REDIS_CACHE_DB,
    key_prefix="superset_results",
)

class CeleryConfig:  # pylint: disable=too-few-public-methods
    BROKER_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_CELERY_DB}"
    CELERY_IMPORTS = ("superset.sql_lab", "superset.tasks")
    CELERYD_LOG_LEVEL = "DEBUG"
    CELERYD_PREFETCH_MULTIPLIER = 1
    CELERY_ACKS_LATE = False
    CELERY_ANNOTATIONS = {
        "sql_lab.get_sql_results": {"rate_limit": "100/s"},
        "email_reports.send": {
            "rate_limit": "1/s",
            "time_limit": 120,
            "soft_time_limit": 150,
            "ignore_result": True,
        },
    }
    CELERYBEAT_SCHEDULE = {
        "email_reports.schedule_hourly": {
            "task": "email_reports.schedule_hourly",
            "schedule": crontab(minute=1, hour="*"),
        },
        "reports.scheduler": {
            "task": "reports.scheduler",
            "schedule": crontab(minute="*", hour="*"),
        },
        "reports.prune_log": {
            "task": "reports.prune_log",
            "schedule": crontab(minute=0, hour=0),
        },
    }


CELERY_CONFIG = CeleryConfig

# Avoid duplicate logging because of propagation to root logger
logging.getLogger("superset").propagate = False

# Enable some custom feature flags
# Do this once native filters are fully functional https://github.com/apache/superset/projects/15+
# def get_cairn_feature_flags(flags):
#     flags["DASHBOARD_NATIVE_FILTERS"] = True
#     return flags
# GET_FEATURE_FLAGS_FUNC = get_cairn_feature_flags

{{ patch("cairn-superset-settings") }}
