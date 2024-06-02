#i have created this file

from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     return HttpResponse("<h1>Rafidda</h1> <a href='https://www.youtube.com/@RafiddaShorts'> Laugh with Rafidda </a> ")
#
# def about(request):
#     return HttpResponse("About Rafidda")

def index(request):
    # return HttpResponse("Home")
    # params ={'name':'rafid', 'place':'mars'}
    return render(request,'index.html')

def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    # print(removepunc)
    # print(djtext)
    # analyzed = djtext
    if removepunc == "on":
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext= analyzed
        # return render(request, 'analyze.html', params)
    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
        djtext = analyzed
    if(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'New Line Removed', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
        djtext = analyzed
    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'New Line Removed', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
    if (removepunc != "on" and fullcaps!="on" and newlineremover!="on" and extraspaceremover != "on"):
        return HttpResponse("Please Select Atleast One Operation!")

    return render(request, 'analyze.html', params)

# def capfirst(request):
#     return HttpResponse("Capitalize First")
#
# def newlineremove(request):
#     return HttpResponse("new line remover")
#
# def spaceremove(request):
#     return HttpResponse("space remover")
#
# def charcount(request):
#     return HttpResponse("Char count")
