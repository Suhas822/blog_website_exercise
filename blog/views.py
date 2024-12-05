from django.shortcuts import render
from .models import BlogPost

from .utils import get_user_country
from .utils import get_client_ip,get_user_country


def post_list(request):
  
    ip_address = get_client_ip(request)
    country = get_user_country(ip_address)
    
    posts = BlogPost.objects.all()
    filtered_posts = posts.filter(country=country)
    return render(request, 'blog/post_list.html', {'posts': filtered_posts,'user_country': country})
