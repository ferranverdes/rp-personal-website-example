from django.shortcuts import render
from apps.portfolio.models import Project

def project_list(request):
	# Query which allows us to retrieve all Project instances from projects table.
	projects = Project.objects.all()

	# Dictionary that will be sent to our templeate as data parameter.
	context = { 'projects': projects }

	# render function creates the HTML to display to the user, using the
	# HttpRequestObject, the template file and all data passed as a parameter.
	return render(request, 'project_list.html', context)

def project_detail(request, pk):
	# Query which allows us to retrieve a Project instance by primary key.
	project = Project.objects.get(pk=pk)

	# Dictionary context that will be sent to our templeate as data parameter.
	context = { 'project': project }

	# render function creates the HTML to display to the user, using the
	# HttpRequestObject, the template file and all data passed as a parameter.
	return render(request, 'project_detail.html', context)
