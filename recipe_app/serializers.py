from rest_framework_json_api import serializers
from recipe_app.models import Items


class ItemsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Items
        fields = ('title', 'calories', 'url', 'description','time')
