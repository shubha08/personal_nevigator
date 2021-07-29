# I have create this file. 
from django.http import HttpResponse

def index(request):
    return HttpResponse("hello, Shubha Paliwal")

def about(request):
    return HttpResponse("About shubha")

def navigatorbar(request):
    return HttpResponse('''<h1>Navigator Bar</h1> <a href ="https://www.facebook.com/"> facebook </a>\n'''
                        ''' <h2> <a href ="https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox"> Gmail </a></h2>'''
                        '''<a href ="https://www.linkedin.com/feed/"> linkedin </a>''')