__author__ = 'Lada'

from django.shortcuts import render_to_response

# def index(request):
#     return render_to_response('index.html',
#         {'user':request.user})

def index(request):
    return render_to_response('index.html')

