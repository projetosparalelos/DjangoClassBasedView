from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=500)
    content = models.TextField()
    slug = models.SlugField()

    def __str__(self):
    	return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        # return reverse('article_detail_view', kwargs={'pk':self.id})
        return reverse('article_list_view')


class Coments(models.Model):
    title = models.CharField(max_length=500)
    content = models.TextField()
    number = models.IntegerField(default=0)
    
    def __str__(self):
    	return self.title
