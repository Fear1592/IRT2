from rest_framework import generics
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from .serializers import CategoryServiceListSerializer, CategoryServiceDetailSerializer, \
    ServiceListSerializer, ServiceDetailSerializer, ServiceImageDetailSerializer, \
    ServiceImageListSerializer
from .models import CategoryService, Images, Service


class ServiceImageCreateView(generics.CreateAPIView):
    serializer_class = ServiceImageDetailSerializer


class ServiceImageListView(generics.ListAPIView):
    serializer_class = ServiceImageListSerializer
    queryset = Images.objects.all()


class ServiceImageDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ServiceImageDetailSerializer
    queryset = Images.objects.all()

    def put(self, request, *args, **kwargs):
        data = request.data
        image = self.get_object()
        service = Service.objects.get(id=int(data.get('service', )))
        image.service = service
        if data.get('image') != '':
            image.image = data.get('image')
        image.save()
        serializer = self.serializer_class(image)
        print(data.get('video'))
        return Response(serializer.data, status=status.HTTP_200_OK)


class CategoryMakersCreateView(generics.CreateAPIView):
    serializer_class = CategoryServiceDetailSerializer


class CategoryMakersDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategoryServiceDetailSerializer
    queryset = CategoryService.objects.all()


class CategoryMakersListView(generics.ListAPIView):
    serializer_class = CategoryServiceListSerializer
    queryset = CategoryService.objects.all()


class ServiceCreateView(generics.CreateAPIView):
    serializer_class = ServiceDetailSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ServiceListView(generics.ListAPIView):
    serializer_class = ServiceListSerializer
    queryset = Service.objects.all()


class ServiceDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ServiceDetailSerializer
    queryset = Service.objects.all()

    def put(self, request, *args, **kwargs):
        data = request.data
        choice = self.get_object()
        category = CategoryService.objects.get(id=int(data.get('category', )))
        choice.name = data.get('name', )
        choice.specifications = data.get('specifications', )
        choice.equipment = data.get('equipment', )
        choice.category = category
        choice.price = data.get('price', )
        choice.is_published = bool(data.get('is_published', ))
        choice.in_stock = bool(data.get('in_stock', ))

        if data.get('uploaded_images') == None:
            choice.image = data.get('uploaded_images')
        choice.save()
        serializer = self.serializer_class(choice)
        print(data.get('uploaded_images'))
        return Response(serializer.data, status=status.HTTP_200_OK)
