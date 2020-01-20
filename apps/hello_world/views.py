from django.shortcuts import render

# When this function is called, it will render an HTML file called hello_world.html
def hello_world(request):
	# request param is an HttpRequestObject created when a user requests a page and
	# it contains information related to the request, like the method (GET/POST/etc).

	# render function creates the HTML to display to the user, using the HttpRequestObject
	# and the template file.
	return render(request, 'hello_world.html', {})
