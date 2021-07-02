from rest_framework import generics, viewsets
from rest_framework.generics import ListCreateAPIView, DestroyAPIView, RetrieveAPIView
from .models import Project, PackageRelease
from .serializers import ProjectSerializer, PackageSerializer
import requests
from rest_framework import mixins, viewsets
from rest_framework import status
from rest_framework.response import Response
import ipdb

class MultipleFildLookupMixin:
    def get_queryset(self):
        queryset = self.queryset
        #ipdb.set_trace()
        lookup_filter = {}
        for lookup_fild in self.lookup_filds:
            if self.request.data.get(lookup_fild):
                lookup_filter[f'{lookup_fild}__icontains'] = self.request.data.get(
                    lookup_fild)

        queryset = queryset.filter(**lookup_filter)
        return queryset



class ProjectViewSet(MultipleFildLookupMixin, ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_filds = ['name']
    def create(self, request, *args, **kwargs):
        serializer = ProjectSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        data = serializer.data

        
        project_object = Project.objects.create(name= data["name"])
        #criando o projeto  
        
        for package in data['packages']:
             
            if 'version' not in package.keys():    
                api = f"https://pypi.org/pypi/{package['name']}/json"
                requisition = requests.get(api)
                if requisition.status_code == 404:
                    return Response({"error": "One or more packages doesn't exist"}, status=status.HTTP_400_BAD_REQUEST)
                list = requisition.json()
                
                #criando o pacote e adcionando a versão aos pacotes que não tem 
                PackageRelease.objects.create(name= package['name'], version=list["info"]["version"], project= project_object)
            
            else:
                #criando os pacotes que já tem versão 
                PackageRelease.objects.create(name= package['name'], version= package["version"], project= project_object) 

        serializer = ProjectSerializer(project_object)
        ipdb.set_trace()
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
       


class ProjectRetrieveDestroyView(RetrieveAPIView, DestroyAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()  
    lookup_field = 'name'
    lookup_url_kwarg = 'name'     