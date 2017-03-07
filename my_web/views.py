from django.shortcuts import render


# Create your views here.
def MyFirstView(request):
	return render(request,'index.html')
