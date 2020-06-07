from django.shortcuts import render




# serve home page
def index(request):
	context = {

	}
	return render(request, 'index.html', context)

