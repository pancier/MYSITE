from django.shortcuts import render

posts = [
	{
		'author': 'AB',
		'title': 'Blog Post 1',
		'content': 'First Post Content',
		'date_posted': 'June 2019'
	},
	{
		'author': 'AC',
		'title': 'Blog Post 2',
		'content': 'Second Post Content',
		'date_posted': 'July 2019',
	}
]

def home(request):
	context = {
		'posts': posts
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})

