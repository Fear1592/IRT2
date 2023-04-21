from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import CategoryListSerializer, CategoryDetailSerializer, \
    ProductListSerializer, ProductDetailSerializer
from .models import Product, CategoryShop, Choices, Images


class CategoryCreateView(generics.CreateAPIView):
    serializer_class = CategoryDetailSerializer


class CategoryListView(generics.ListAPIView):
    serializer_class = CategoryListSerializer
    queryset = CategoryShop.objects.all()


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategoryDetailSerializer
    queryset = CategoryShop.objects.all()


class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductDetailSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ProductListView(generics.ListAPIView):
    serializer_class = ProductListSerializer
    queryset = Product.objects.all()


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.all()

    def put(self, request, *args, **kwargs):
        data = request.data
        product = self.get_object()
        category = CategoryShop.objects.get(id=int(data.get('category', )))
        product.name = data.get('name', )
        product.specifications = data.get('specifications', )
        product.equipment = data.get('equipment', )
        product.category = category
        product.price = data.get('price', )
        product.is_published = bool(data.get('is_published', ))
        product.in_stock = bool(data.get('in_stock', ))

        if data.get('uploaded_images') == None:
            product.image = data.get('uploaded_images')
        product.save()
        serializer = self.serializer_class(product)
        print(data.get('uploaded_images'))
        return Response(serializer.data, status=status.HTTP_200_OK)
