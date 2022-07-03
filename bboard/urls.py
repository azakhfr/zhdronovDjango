from django.urls import path

from bboard.views import index, by_rubric, BbCreateView, BbRubricView

urlpatterns = [
    path("add/", BbCreateView.as_view(), name="add"),
    path("<int:rubric_id>", BbRubricView.as_view(), name="by_rubric"),
    path("", index, name="index"),
]
