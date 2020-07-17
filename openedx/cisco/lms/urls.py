from django.conf.urls import include
from django.conf.urls import url


urlpatterns = [
    url(
        r'^api/ibl/cisco/courses/',
        include(
            'ibl_assessments_results.urls',
            namespace='ibl_assessments_results',
        )
    ),
    url(
        r'^api/ibl/',
        include(
            'ibl_catalog_dashboard_api.urls',
        )
    ),
    url(
        r'^api/ibl/',
        include(
            'ibl_catalog_metadata.urls.lms',
        )
    ),
]
