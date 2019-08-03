from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# posts = [
# 	{
# 		'author' : 'Neeraj',
# 		'title' : 'Blog Post 1',
# 		'content'  : 'First post content',
# 		'date_posted' : 'August 3,2019'
# 	},
# 	{
# 		'author' : 'Aggarwal',
# 		'title' : 'Blog Post 2',
# 		'content'  : 'First post content',
# 		'date_posted' : 'August 3,2019'
# 	}
# ]

def home(request):
	context = {
		'posts' : Post.objects.all()
	}
	return render(request,'blog/home.html',context)

def about(request):
	# return HttpResponse('<h1>Blog About</h1>')
	return render(request,'blog/about.html',{'title':'About'})