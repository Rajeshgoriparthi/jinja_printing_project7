from django.shortcuts import render

# Create your views here.
def virat(request):
    dic={'name':'The_king'}
    return render(request,'virat.html',context=dic)
