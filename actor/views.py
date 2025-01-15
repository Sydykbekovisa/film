from rest_framework.generics import ListAPIView

from .models import Actors
from .serializers import ActorsSerializersList


class ActorsListView(ListAPIView):
    queryset = Actors
    serializer_class = ActorsSerializersList

