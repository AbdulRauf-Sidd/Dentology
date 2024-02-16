from django.shortcuts import render
from mainapp import models
from .serializers import PatientSerializers
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, get_list_or_404 #return a friendly error response

# Create your views here.
'''
class PatientView(generics.ListCreateAPIView):
    queryset = models.Patient.objects.all();
    serializer_class = PatientSerializers;
    
class SinglePatientView(generics.RetrieveUpdateAPIView):
    queryset = models.Patient.objects.all();
    serializer_class = PatientSerializers;
'''

@api_view(['GET', 'POST'])
def patients(request):
    if request.method == 'GET':
        items = get_list_or_404(models.Patient);
        serialized_item = PatientSerializers(items, many=True);
        return Response(serialized_item.data);
    if request.method == 'POST':
        serialized_item = PatientSerializers(data=request.data);
        serialized_item.is_valid(raise_exception=True);
        serialized_item.save()
        return Response(serialized_item.data, status.HTTP_201_CREATED);
        

@api_view()
def single_patient(request, pk):
    items = get_object_or_404(models.Patient, pk=pk);
    serialized_item = PatientSerializers(items);
    return Response(serialized_item.data);

'''
@api_view(['GET', 'POST'])
def menu_items_view(request):
    if request.method == 'GET':
        queryset = MenuItem.objects.all()

        # Apply ordering
        ordering = request.query_params.get('ordering', None)
        if ordering in ['price', '-price', 'inventory', '-inventory']:
            queryset = queryset.order_by(ordering)

        # Apply filtering
        price_filter = request.query_params.get('price', None)
        if price_filter:
            queryset = queryset.filter(price=price_filter)
        inventory_filter = request.query_params.get('inventory', None)
        if inventory_filter:
            queryset = queryset.filter(inventory=inventory_filter)

        # Apply search
        search_query = request.query_params.get('search', None)
        if search_query:
            queryset = queryset.filter(title__icontains=search_query)
'''