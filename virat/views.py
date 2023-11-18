from django.shortcuts import render

# Create your views here.
def kohli(request):
    data='Virat king kohli'
    d={'king':'Virat king kohli'}
    return render(request,'virat.html',context=d)