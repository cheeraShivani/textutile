#it was created by me
from django.http import HttpResponse
from django.shortcuts import render
#CODE FOR VIDEO 7

# def index(request):
#     return HttpResponse('hello')


# def YT(request):
#     return HttpResponse('<a href="https://www.youtube.com/">click here to open youtube')

# def about(request):
#     return HttpResponse('<h1>About<br>Me<a href="https://www.google.com/"> CLICK THE LINK TO ACCESS GOOGLE</h1>')
#naviiiii
def navi(request):
    s='''<h2>NAVIGATION BAR <br></h2>
    <ul>
        <li><a href="https://github.com/cheeraShivani">github</a></li>
        <li><a href="https://github.com/cheeraShivani">github</a></li>
        <li><a href="https://github.com/cheeraShivani">github</a></li>
    </ul>

    '''
    return HttpResponse(s)



def index(request):
    return render(request,'index.html')


def analyze(request):
# .GET text
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    Newline_remover=request.POST.get('Newline_remover','off')
    
    if removepunc=="on":
    # analyzed=djtext
        punctuations='''!,.(){}[];:><\~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose':'Removed Punctuations','analyzed_text':analyzed}
        djtext=analyzed
    if(fullcaps=='on'):
        analyzed=''
        for char in djtext:
            analyzed=analyzed+char.upper()
        params={'purpose':'changed to uppercase','analyzed_text':analyzed}
        djtext=analyzed

    #it remove chare to enter to a new line
    if(Newline_remover=='on'):
        analyzed=''
        for char in djtext:
            if char!='\n' and char!='\r':
                analyzed=analyzed+char
        params={'purpose':'Remove new line','analyzed_text':analyzed}
        djtext=analyzed

    return render(request,'analyze.html',params)

    


