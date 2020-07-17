from django.conf.urls import include
from django.conf.urls import url

urlpatterns = [
    url(
        r'^api/ibl/',
        include(
            'ibl_catalog_metadata.urls.lms',
        )
    ),
]
