from django.shortcuts import render
from django.http import HttpRequest
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from bboard.forms import BbForm
from bboard.models import Bb, Rubric

# Create your views here.


def index(request: HttpRequest):

    bbs = Bb.objects.all()
    rubrics = Rubric.objects.all()
    context = {"bbs": bbs, "rubrics": rubrics}
    return render(template_name="index.html", context=context, request=request)


def by_rubric(request: HttpRequest, rubric_id: int):
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {"bbs": bbs, "rubrics": rubrics, "current_rubric": current_rubric}
    return render(template_name="by_rubric.html", context=context, request=request)


class BbCreateView(CreateView):
    template_name = "create.html"
    form_class = BbForm
    success_url = reverse_lazy("index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["rubrics"] = Rubric.objects.all()
        return context


class BbRubricView(ListView):
    # template_name = "by_rubric.html"
    context_object_name = "bbs"
    model = Bb

    def get_queryset(self):
        return Bb.objects.filter(rubric=self.kwargs["rubric_id"])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(BbRubricView, self).get_context_data()
        context["rubrics"] = Rubric.objects.all()
        context["current_rubric"] = Rubric.objects.get(pk=self.kwargs["rubric_id"])

        return context
