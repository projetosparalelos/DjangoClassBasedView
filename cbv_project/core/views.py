from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):

    '''   TemplateResponseMixin requires either a definition of 'template_name' 
          or an implementation of 'get_template_names()
    '''
    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['latest_articles'] = range(0, 100)
        return context

