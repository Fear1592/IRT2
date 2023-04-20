from rest_framework import serializers
from rest_framework import generics
from .serializers import ProducedListSerializer, ProducedDetailSerializer
from .models import Produced




class ProducedListView(generics.ListAPIView, ):
    serializer_class = ProducedListSerializer
    queryset = Produced.objects.all()


class ProducedDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProducedDetailSerializer
    queryset = Produced.objects.all()


    def get_object(self):
        obj = super().get_object()
        user = self.request.user
        if user.is_authenticated and user not in obj.viewers_pk.all():
            obj.views_counter += 1
            obj.viewers.add(user)
            obj.save()
        return obj
