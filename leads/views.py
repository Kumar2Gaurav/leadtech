from django.shortcuts import render

# Create your views here.

from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import RetrieveDestroyAPIView, ListCreateAPIView
from django.db.models.deletion import ProtectedError
from .serializers import LeadSerializer
from .models import LeadSolution


class get_delete_update_lead(RetrieveDestroyAPIView):
    http_method_names = ['get', 'put', 'delete', 'head', 'options', 'trace']
    serializer_class = LeadSerializer

    def get_queryset(self,pk):
        try:
            lead = LeadSolution.objects.get(pk=self.kwargs['pk'])
        except Exception as e:
            content = {
                'status': False,
                'reason': str(e)
            }
            return content
        return {"status":True,"data":lead}

    # Get a lead
    def get(self, request, pk):
        import ipdb;ipdb.set_trace()
        lead = self.get_queryset(pk)
        try:
            if lead["status"]:
                serializer = LeadSerializer(lead["data"])
                content=serializer.data
                content["status"]="Created/Contacted"
                return Response(content, status=status.HTTP_200_OK)
            return Response({}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            content={"status":"failure","reason":str(e)}
            return Response(content, status=status.HTTP_200_OK)


    # Update a lead
    def put(self, request, pk):
        import ipdb;ipdb.set_trace()
        lead = self.get_queryset(pk)
        if lead["status"]:
            try:
                serializer = LeadSerializer(lead["data"],request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
            except Exception as e:
                content={"status":"failure","reason":str(e)}
                return Response(content, status=status.HTTP_400_BAD_REQUEST)
        return Response({}, status=status.HTTP_404_NOT_FOUND)

    # Delete a lead
    def delete(self, request, pk):
        import ipdb;ipdb.set_trace()
        lead = self.get_queryset(pk)
        try:
            lead["data"].delete()
        except Exception as e:
            content = {
                "Status":"failure",
                'reason': str(e)
            }
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        content = {
            'status': 'success'
        }
        return Response(content, status=status.HTTP_200_OK)


class get_post_leads(ListCreateAPIView):
    serializer_class = LeadSerializer

    def get_queryset(self):
        leads = LeadSolution.objects.all()
        return leads

    # Get all leads
    def get(self, request):
        import ipdb;ipdb.set_trace()
        leads = self.get_queryset()
        paginate_queryset = self.paginate_queryset(leads)
        serializer = self.serializer_class(paginate_queryset, many=True)
        return self.get_paginated_response(serializer.data)

    # Create a new lead
    def post(self, request):
        # lead = LeadSolution.objects.filter(
        #     mobile=request.data.get('code')).first()
        # if (lead):
        #     serializer = LeadSerializer(
        #         lead, data=request.data)
        # else:
        import ipdb;ipdb.set_trace()
        serializer = LeadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            content=serializer.data
            content["status"]="Created"
            return Response(content, status=status.HTTP_201_CREATED)
        content={"status":"failure","reason":serializer.errors}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)
