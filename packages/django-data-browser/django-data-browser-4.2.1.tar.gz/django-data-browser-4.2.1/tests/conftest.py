import dj_database_url
import pytest
from django.conf import settings

DATABASE_CONFIG = dj_database_url.config(
    conn_max_age=600, default="sqlite:///db.sqlite3"
)

POSTGRES = "postgresql" in DATABASE_CONFIG["ENGINE"]
SQLITE = "sqlite" in DATABASE_CONFIG["ENGINE"]

if POSTGRES:
    ARRAY_FIELD_SUPPORT = True
else:
    ARRAY_FIELD_SUPPORT = False

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.staticfiles",
    "django.contrib.admin",
    "tests.core",
    "tests.json",
    "data_browser",
]

if ARRAY_FIELD_SUPPORT:
    INSTALLED_APPS.append("tests.array")

settings.configure(
    INSTALLED_APPS=INSTALLED_APPS,
    DATABASES={"default": DATABASE_CONFIG},
    ROOT_URLCONF="tests.urls",
    MIDDLEWARE=[
        "django.middleware.security.SecurityMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
    ],
    TEMPLATES=[
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "OPTIONS": {
                "context_processors": [
                    "django.template.context_processors.debug",
                    "django.template.context_processors.request",
                    "django.template.context_processors.static",
                    "django.contrib.auth.context_processors.auth",
                ],
                "loaders": ["django.template.loaders.app_directories.Loader"],
            },
        }
    ],
    STATIC_URL="/static/",
    MEDIA_URL="/media/",
    DATA_BROWSER_ALLOW_PUBLIC=True,
    USE_I18N=True,
    USE_TZ=True,
    TIME_ZONE="UTC",
    SECRET_KEY="secret",
)


@pytest.fixture
def ddb_request(rf):
    from data_browser.common import add_request_info

    request = rf.get("/")
    add_request_info(request)
    return request


@pytest.fixture
def admin_ddb_request(ddb_request, admin_user):
    ddb_request.user = admin_user
    return ddb_request


@pytest.fixture
def mock_admin_get_queryset(mocker):
    from data_browser.orm_admin import admin_get_queryset

    return mocker.patch(
        "data_browser.orm_admin.admin_get_queryset", wraps=admin_get_queryset
    )
