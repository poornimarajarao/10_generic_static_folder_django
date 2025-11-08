from django.shortcuts import render

def generic(request):
    return render(request,'generic.html')
