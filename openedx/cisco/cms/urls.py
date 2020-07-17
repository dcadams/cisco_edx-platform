from django.conf.urls import include
from django.conf.urls import url

urlpatterns = [
    url(
        r'^api/ibl/',
        include(
            'ibl_catalog_metadata.urls.lms',
        )
    ),
    url(
        r'^api/ibl/cisco/courses/',
        include(
            'ibl_course_import_from_template.urls',
            namespace='ibl_course_import_from_template'
        )
    ),
    url(
        r'',
        include(
            'ibl_course_management_api.urls'
        )
    ),
]
