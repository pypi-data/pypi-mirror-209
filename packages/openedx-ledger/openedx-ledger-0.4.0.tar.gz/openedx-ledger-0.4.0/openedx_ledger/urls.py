"""
URLs for openedx_ledger.
"""
from django.contrib import admin
from django.urls import path, re_path  # pylint: disable=unused-import
from django.views.generic import TemplateView  # pylint: disable=unused-import

urlpatterns = [
    # TODO: Fill in URL patterns and views here.
    # re_path(r'', TemplateView.as_view(template_name="openedx_ledger/base.html")),
    path('admin/', admin.site.urls)
]
