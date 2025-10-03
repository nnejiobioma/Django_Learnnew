from django.shortcuts import render

# Create your views here.

def posts_list(request):
    return render(request, 'posts/posts_list.html')

def posts_about(request):
    return render(request, 'posts/posts_about.html')