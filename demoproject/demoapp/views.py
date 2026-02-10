from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Home(Request):
    text='''<h1 style=color:green>About Myself<h1>
    <p style=color:brown>I am Dheypalli Anusha from madanapalli<p>
    <h1 style=color:blue>About my College<h1>
    <p style=color:black>My college name is sri venkateswara college of engineering and technology in chittoor<p>'''
    return HttpResponse(text)