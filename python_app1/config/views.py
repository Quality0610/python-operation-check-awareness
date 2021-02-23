from django.http import HttpResponse
from django.views.generic import TemplateView

def helloworldfunction(request):
    return_object = HttpResponse('<h1>hello, world</h1>')
    return return_object

class HelloWorldView(TemplateView):
    template_name = 'hello.html'