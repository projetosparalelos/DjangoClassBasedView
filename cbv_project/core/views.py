from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, DeleteView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from core.models import Article, Coments


class HomePageView(TemplateView):

    '''   TemplateResponseMixin requires either a definition of 'template_name' 
          or an implementation of 'get_template_names()
    '''
    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['latest_articles'] = range(0, 100)
        return context


class ArticleListView(ListView):

    model = Article

    # When you set the qeuryset yo can ignore the model attribute
    #queryset = Coments.objects.all()
    ordering = 'title'
    paginate_by = 10


    '''The view assumes app_name + model_name + list + .html
     If you pass a template name that doesn't exist it will find the defaul template
     If you put another Model in the queryset and don't set up the template_name
     the view will look for a template with the same name of the model from the queryset o.0
    '''
    template_name = 'core/article_list.html'

    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        context['now'] = 'Var passed by context'
        return context



class ArticleDetail(DetailView):
    model = Article


class ArticleCreate(CreateView):
    model = Article
    fields = ['title', 'content', 'slug']

    # You have to setup the get_absolute_url in your models if you don't want to set th success_url

    
    # initial = {'title': 'Titulo padrao', 'content': 'content padrao'}
    # form_class = None
    # success_url = None

    def get_context_data(self, **kwargs):
        """
        Insert the form into the context dict.
        """
        if 'form' not in kwargs:
            kwargs['form'] = self.get_form()
        return super(ArticleCreate, self).get_context_data(**kwargs)

    # Optional
    def form_valid(self, form):
        form.instance.title = form.instance.title + ' Modified '
        self.object = form.save()
        return super(ArticleCreate, self).form_valid(form)


class ArticleUpdate(UpdateView):
    model = Article
    fields = ['title', 'content', 'slug']

    # Optional
    def form_valid(self, form):
        form.instance.title = form.instance.title + ' Updated '
        self.object = form.save()
        return super(ArticleUpdate, self).form_valid(form)


class ArticleDelete(DeleteView):
    model = Article

    # This is optional if the get_absolute_url is implemented in the Model
    success_url = reverse_lazy('article_list_view')
