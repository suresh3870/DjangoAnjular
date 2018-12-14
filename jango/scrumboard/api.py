#from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from .serializer import ListSerializer, CardSerializer
from .models import List, Card


class ListApi(ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer


class CardApi(ModelViewSet):
        queryset = Card.objects.all()
        serializer_class = CardSerializer
