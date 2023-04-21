from rest_framework import generics
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status

from .serializers import ProducedListSerializer, ProducedDetailSerializer, CategoryMakersDetailSerializer \
    , CategoryMakersListSerializer , ProducedImageListSerializer, ProducedImageDetailSerializer
from .models import Produced, CategoryMakers, Images




class ProducedImageCreateView(generics.CreateAPIView):
    serializer_class = ProducedImageDetailSerializer


class ProducedImageListView(generics.ListAPIView):
    serializer_class = ProducedImageListSerializer
    queryset = Images.objects.all()


class ProducedImageDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProducedImageDetailSerializer
    queryset = Images.objects.all()

    def put(self, request, *args, **kwargs):
        data = request.data
        image = self.get_object()
        produced = Produced.objects.get(id=int(data.get('produced', )))
        image.produced = produced
        if data.get('image') != '':
            image.image = data.get('image')
        image.save()
        serializer = self.serializer_class(image)
        print(data.get('video'))
        return Response(serializer.data, status=status.HTTP_200_OK)



class ProducedCreateView(generics.CreateAPIView):
    serializer_class = ProducedDetailSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ProducedListView(generics.ListAPIView):
    serializer_class = ProducedListSerializer
    queryset = Produced.objects.all()


class ProducedDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProducedDetailSerializer
    queryset = Produced.objects.all()

    def put(self, request, *args, **kwargs):
        data = request.data
        choice = self.get_object()
        category = CategoryMakers.objects.get(id=int(data.get('category', )))
        choice.name = data.get('name', )
        choice.specifications = data.get('specifications', )
        choice.equipment = data.get('equipment', )
        choice.article_number = data.get('article_number', )
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



class CategoryMakersCreateView(generics.CreateAPIView):
    serializer_class = CategoryMakersDetailSerializer


class CategoryMakersDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategoryMakersDetailSerializer
    queryset = CategoryMakers.objects.all()


class CategoryMakersListView(generics.ListAPIView):
    serializer_class = CategoryMakersListSerializer
    queryset = CategoryMakers.objects.all()