from django.shortcuts import render
from apps.blog.models import Post, Comment
from apps.blog.forms import CommentForm

def post_list(request):
	posts = Post.objects.all().order_by('-created_on')
	context = { 'posts': posts }
	return render(request, 'post_list.html', context)

# The minus sign tells Django to start with the largest value rather than the smallest.
# We use this, as we want the posts to be ordered with the most recent post first.

def category_post_list(request, category):
	posts = Post.objects.filter(
		categories__name__contains=category
	).order_by(
		'-created_on'
	)

	context = {
		'category': category,
		'posts': posts
	}

	return render(request, 'category_post_list.html', context)

# On line 14 we have used a Django Query Filter. In this case, we have specified
# that we want all posts which have in the 'categories' attribute a category which
# its 'name' attribute contains the 'category' parameter value.

def post_detail(request, pk):
	post = Post.objects.get(pk=pk)

	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = Comment(
				author=form.cleaned_data['author'],
				body=form.cleaned_data['body'],
				post=post
			)

			comment.save()

	comments = Comment.objects.filter(post=post)
	form = CommentForm()

	context = {
		'post': post,
		'comments': comments,
		'form': form
	}

	return render(request, 'post_detail.html', context)

# When a user visits a page containing a form, they send a GET request to the server.
# In this case, there’s no data entered in the form, so we just want to render the
# form and display it.
#
# When a user enters information and clicks the Submit button, a POST request,
# containing the data submitted with the form, is sent to the server. At this point,
# the data must be processed.
#
# On line 38, They keys of the dictionary correspond to the form fields, so you can
# access the author using form.cleaned_data['author'].
