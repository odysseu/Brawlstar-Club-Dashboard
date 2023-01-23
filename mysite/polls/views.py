from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    html = "<html><h1> Local Time: {{ TIME_ZONE }} </h1><head><style> body{background-color: #000000; color: #ffffff;} </style></head><body>This is in dark mode</body></html>"
    return HttpResponse(html)
