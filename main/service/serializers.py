from rest_framework import serializers
from .models import CategoryService, Images, Service


class ServiceImageDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ["id", "service", "image"]


class ServiceImageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ["id", "service", "image"]


class ServiceDetailSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, )
    images = ServiceImageListSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(required=False, allow_empty=True,
                                            child=serializers.ImageField(max_length=1000000, use_url=False),
                                            default=[],
                                            write_only=True
                                            )

    class Meta:
        model = Service
        fields = ["id", 'user', "name", "specifications",
                  "equipment", "category", "price", "is_published", "in_stock", "created_at", "images",
                  "uploaded_images"]

    def create(self, validated_data):
        uploaded_images = validated_data.pop("uploaded_images")
        service = Service.objects.create(**validated_data)
        for image in uploaded_images:
            newproduced_image = Images.objects.create(service=service, image=image)

        return service


class ServiceListSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, )
    images = ServiceImageListSerializer(many=True, read_only=True)

    class Meta:
        model = Service
        fields = ["id", 'user', "name", "specifications",
                  "equipment", "category", "price", "is_published", "in_stock", "created_at", "images"]


class CategoryServiceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryService
        fields = '__all__'


class CategoryServiceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryService
        fields = '__all__'
