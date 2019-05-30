from django.shortcuts import render
from datetime import datetime
from .Serializers import CommentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse


# Create your views here.
class Comment:
    def __init__(self,email,content,created=None):
        self.email=email
        self.content=content
        self.created=created or datetime.now()

def myapi(request):
    comment=Comment(email='mahisoft2020@gmail.com', content='Good mahi keep it Up.')
    serializer=CommentSerializer(comment)
    return HttpResponse(JSONRenderer().render(serializer.data),content_type="text/html")