from rest_framework import serializers
from .models import Produced, Images, CategoryMakers


class ProducedImageDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ["id", "produced", "image"]


class ProducedImageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ["id", "produced", "image"]




class ProducedDetailSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, )
    images = ProducedImageListSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(required=False, allow_empty=True,
                                            child=serializers.ImageField(max_length=1000000, use_url=False),
                                            default=[],
                                            write_only=True
                                            )

    class Meta:
        model = Produced
        fields = ["id", 'user', "name", "article_number", "specifications",
                  "equipment", "category", "price", "is_published", "in_stock", "created_at", "images",
                  "uploaded_images"]

    def create(self, validated_data):
        uploaded_images = validated_data.pop("uploaded_images")
        produced = Produced.objects.create(**validated_data)
        for image in uploaded_images:
            newproduced_image = Images.objects.create(produced=produced, image=image)

        return produced


class ProducedListSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, )
    images = ProducedImageListSerializer(many=True, read_only=True)

    class Meta:
        model = Produced
        fields = ["id", 'user', "name", "article_number", "specifications",
                  "equipment", "category", "price", "is_published", "in_stock", "created_at", "images"]


class CategoryMakersDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryMakers
        fields = '__all__'


class CategoryMakersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryMakers
        fields = '__all__'
