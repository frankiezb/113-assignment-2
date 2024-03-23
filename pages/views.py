from django.shortcuts import render

 # Create your views here.

from django.views.generic import TemplateView

class HomePageView(TemplateView):
     template_name = "pages/home.html"
        
class AboutPageView(TemplateView):
     template_name = "pages/about.html"
    
    
    




#from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
)
from .modles import Post


#class PostListView(ListView):
   # template_name = "posts/list.html"
   # model = Post
    
#class PostDetailView(DetailView):
        template_name = "posts/detail.html"
        model = Post
        
#class PostCreateView(CreateView):
   # template_name = "posts/new.html"
   # model = Post
   # fields = ["title", "subtitle", "author", "body"]




#from django.views.generic import TemplateView


#class HomePageView(TemplateView):
    #template_name = "pages/home.html"
    
#class AboutPageView(TemplateView):
    #template_name = "pages/about.html"
# Create your views here.
