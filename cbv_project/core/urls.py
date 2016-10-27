from django.conf.urls import url
from django.views.generic import TemplateView
from core.views import HomePageView, ArticleListView, ArticleDetail, ArticleCreate, ArticleUpdate, ArticleDelete


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='core/home.html'), {'var': 'Mundo', 'my_var': 5}, name='home'),
    url(r'^template-view/$', HomePageView.as_view(), name='template_view'),
    url(r'^list-view/$', ArticleListView.as_view(), name='article_list_view'),
    url(r'^create-view/$', ArticleCreate.as_view(), name='article_create_view'),
    url(r'^detail-view/(?P<pk>\d+)/$', ArticleDetail.as_view(), name='article_detail_view'),
    url(r'^update-view/(?P<pk>\d+)/$', ArticleUpdate.as_view(), name='article_update_view'),
    url(r'^delete-view/(?P<pk>\d+)/$', ArticleDelete.as_view(), name='article_delete_view'),

]
