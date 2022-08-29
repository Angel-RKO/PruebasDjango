from django.shortcuts import render
# importante!
from django.views.generic import View

# Create your views here.
class BlogListVista(View):
    def get(self, request, *args, **kwargs):
        context={

        }
        return render(request,'blog_list.html', context)