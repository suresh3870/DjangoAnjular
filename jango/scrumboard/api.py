#from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from .serializer import ListSerializer, CardSerializer
from .models import List, Card
from rest_framework import permissions


class ListApi(ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer
    permission_classes = (permissions.IsAuthenticated,)



class CardApi(ModelViewSet):
        queryset = Card.objects.all()
        serializer_class = CardSerializer
        permission_classes = (permissions.IsAuthenticated,)


