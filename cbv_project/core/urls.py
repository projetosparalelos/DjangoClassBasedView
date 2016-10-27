from django.conf.urls import url
from django.views.generic import TemplateView
from core.views import HomePageView


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='core/home.html'), {'var': 'Mundo', 'my_var': 5}, name='home'),
    url(r'^template-view/$', HomePageView.as_view(), name='template_view'),

]
