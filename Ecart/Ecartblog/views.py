from django.shortcuts import render
from django.http import HttpResponse
from.models import post

# Create your views here.
def blogview(request):
    fethome=post.objects.all()
    print(fethome)
    
    return render(request,"Ecartblog/rk.html",{'fethome':fethome})
def blogpost(request,id):
    postfetch=post.objects.filter(post_id=id)[0]
    print(postfetch)
    return render(request,"Ecartblog/blogpost.html",{'postfetch':postfetch})
