from django.shortcuts import render

from django.views.generic import TemplateView


class IndexTemplateView(TemplateView):
    template_name = 'index.html'
    extra_context = {
        'title': 'Главная'
    }
