from __future__ import annotations

from django.contrib import admin

from django.urls import path

from landman import views

urlpatterns = [
    path("", views.index),
    path("favicon.ico", views.favicon),
    path("csrf-demo/", views.csrf_demo),
    path("csrf-demo/checker/", views.csrf_demo_checker),
    path("countries/", views.countries),
    path("error-demo/", views.error_demo),
    path("error-demo/trigger/", views.error_demo_trigger),
    path("middleware-tester/", views.middleware_tester),
    path("middleware-tester/table/", views.middleware_tester_table),
    path("partial-rendering/", views.partial_rendering),

    path('admin/', admin.site.urls),
]
