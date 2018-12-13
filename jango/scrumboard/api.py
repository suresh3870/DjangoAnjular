from rest_framework.generics import ListAPIView


from .serializer import ListSerializer, CardSerializer
from .models import List, Card

class ListApi(ListAPIView):
    queryset = List.object.all()
    serilize_class = ListSerializer


class CardApi(ListAPIView):
        queryset = List.object.all()
        serilize_class = CardSerializer
