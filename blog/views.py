from django.shortcuts import render
from .models import BlogPost

from .utils import get_user_country

def post_list(request):
    country = get_user_country(request=request)

    posts = BlogPost.objects.all()
    filtered_posts = posts.filter(country=country)

    return render(request, 'blog/post_list.html', {
        'posts': posts,
        'filtered_posts': filtered_posts,
        'country': country,
    })

