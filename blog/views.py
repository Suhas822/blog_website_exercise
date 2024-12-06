from django.shortcuts import render
from .models import BlogPost  # Replace with your model
from .utils import get_user_country, get_client_ip

def blog_posts_view(request):
    
    ip_address = get_client_ip(request)
  
    user_country = get_user_country(ip_address)

    
    country_filter = request.GET.get('filter_by_country', None)

    if country_filter:
     
        posts = BlogPost.objects.filter(country=user_country)
    else:
       
        posts = BlogPost.objects.all()

    return render(request, 'blog/post_list.html', {
        'posts': posts,
        'user_country': user_country,
    })
