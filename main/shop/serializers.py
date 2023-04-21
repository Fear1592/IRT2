from rest_framework import serializers
from .models import Product, CategoryShop, Choices, Images


class ProductImageDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ["id", "product", "image"]


class ProductImageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ["id", "product", "image"]


class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryShop
        fields = '__all__'


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryShop
        fields = '__all__'


class ProductDetailSerializer(serializers.ModelSerializer):
    # choices = ChoicesListSerializer(many=True, read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True, )
    images = ProductImageListSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(required=False, allow_empty=True,
                                            child=serializers.ImageField(max_length=1000000, use_url=False),
                                            default=[],
                                            write_only=True
                                            )

    class Meta:
        model = Product
        fields = ['id', 'user', 'name', 'choice_cat',
                  'specifications', 'equipment', "is_published",
                  'category', 'created_at', "images", "uploaded_images",
                  ]

    def create(self, validated_data):
        uploaded_images = validated_data.pop("uploaded_images")
        product = Product.objects.create(**validated_data)
        print(product)
        for image in uploaded_images:
            newproduced_image = Images.objects.create(product=product, image=image)

        return product


class ProductListSerializer(serializers.ModelSerializer):
    # choices = ChoicesListSerializer(many=True, read_only=True)
    # videos = VideosListSerializer(many=True, read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True, )
    images = ProductImageListSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'user', 'name', 'choice_cat',
                  'specifications', 'equipment',
                  'category', 'created_at', "images",
                  ]
