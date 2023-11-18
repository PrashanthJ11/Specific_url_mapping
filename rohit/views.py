from django.shortcuts import render

# Create your views here.
def sharma(request):
    data='Hitman Rohit sharma'
    d={'hitman':data}
    return render(request,'rohit.html',context=d)
