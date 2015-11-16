from django.shortcuts import render_to_response
from . import database

def mainpage(request):
    return render_to_response('mainpage.html')
    
def allBookIns(request):
    tups = database.selectAllBookIns()
    return render_to_response('table.html', {"tups": tups})
    
def bookInByName(request, name):
    tups = database.selectBookInsByName(name)
    return render_to_response('table.html', {"tups": tups})