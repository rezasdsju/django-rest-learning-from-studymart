from django.shortcuts import render
from . models import Aiquest
from . serializers import AiquestSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
# Create your views here.


'''
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


from django.views.decorators.csrf import csrf_exempt
import io
from rest_framework.parsers import JSONParser
@csrf_exempt
def aiquest_create(request):
    if request.method == 'POST':
        json_data = request.body
        
        #json to stream data
        stream = io.BytesIO(json_data)
        
        #stream to python
        pythondata = JSONParser().parse(stream)
        
        #Python to complex data
        serializer = AiquestSerializer(data=pythondata)
        
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'successfully inserted data'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
        
    if request.method == 'PUT':
        json_data = request.body
        
        #Json to stream
        stream = io.BytesIO(json_data)
        
        #stream to python 
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        
        aiq = Aiquest.objects.get(id=id)
        serializer = AiquestSerializer(aiq, data=pythondata, partial = True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'successfully updated partial data'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
                    
    if request.method == 'DELETE':
        json_data = request.body
        
        #json to stream
        stream = io.BytesIO(json_data)
        
        #stream to python 
        pythondata = JSONParser().parse(stream)
        
        id = pythondata.get('id')
        aiq = Aiquest.objects.get(id=id)
        aiq.delete()
        res = {'msg': 'Succesfully deleted data'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type='application/json')
    '''
    
    
    



from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def aiquest_create(request, pk=None):
    if request.method == 'GET':
        id = pk
        if id is not None:
            #Complex Data
            ai = Aiquest.objects.get(id=id)
            
            #complex data to python dictionary
            serializer = AiquestSerializer(ai)
            return Response(serializer.data)
        
        #complex data
        ai = Aiquest.objects.all()
        # complex data to python dictionary
        serializer = AiquestSerializer(ai, many=True)
        return Response(serializer.data)
    
        
    