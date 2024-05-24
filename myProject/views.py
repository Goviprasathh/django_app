from django.shortcuts import HttpResponse

# Create your views here.


# def CallPage(request):
#     return HttpResponse(request, 'index.html')


def main(request):
    return HttpResponse ('<h1>hello</h1>')