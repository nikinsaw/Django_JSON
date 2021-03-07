from recipe_app.models import Items
from recipe_app.serializers import ItemsSerializer
from rest_framework import viewsets


class ItemsViewSet(viewsets.ModelViewSet):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer

