from django.shortcuts import render
from . models import Aiquest
from . serializers import AiquestSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
# Create your views here.

#Queryset
def aiquest_info(request):
    #Complex data
    ai = Aiquest.objects.all()
    
    #Python Dictionary
    serializer = AiquestSerializer(ai, many=True)
    
    #Render to Json
    json_data = JSONRenderer().render(serializer.data)
    
    
    #Sent Json data to user
    return HttpResponse(json_data, content_type='application/json')
    
    



#Model Instance
def aiquest_ins(request, pk):
    #Complex data
    ai = Aiquest.objects.get(id=pk)
    
    #Python Dictionary
    serializer = AiquestSerializer(ai)
    
    #Render to Json
    json_data = JSONRenderer().render(serializer.data)
    
    
    #Sent Json data to user
    return HttpResponse(json_data, content_type='application/json')