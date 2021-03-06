from django.urls import include, path
from research import views
from rest_framework import routers

app_name = "research"
router = routers.DefaultRouter()
router.register(r"study", views.StudyViewSet)
router.register(r"subject", views.SubjectViewSet)
router.register(r"group", views.GroupViewSet)
router.register(r"procedure", views.ProcedureViewSet)
router.register(r"event", views.EventViewSet)
router.register(
    r"procedure_step", views.ProcedureStepViewSet, basename="procedure_step"
)
router.register(r"task", views.TaskViewSet)
router.register(
    r"measurement", views.MeasurementDefinitionViewSet, basename="measurement"
)

urlpatterns = [
    path(
        "research/procedure/items/",
        views.ProcedureViewSet.as_view({"get": "get_items"}),
        name="get_procedure_items",
    ),
    path(
        "research/event/items/",
        views.EventViewSet.as_view({"get": "get_items"}),
        name="get_event_items",
    ),
    path(
        "research/measurement/items/",
        views.MeasurementDefinitionViewSet.as_view({"get": "get_items"}),
        name="get_measurement_definition_items",
    ),
    path("research/", include(router.urls)),
]
