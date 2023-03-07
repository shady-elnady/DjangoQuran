from rest_framework.serializers import HyperlinkedModelSerializer 

from .models import BookMark
from Aya.Serializer import AyaSerializer

# Serializers define the API representation.


class BookMarkSerializer(HyperlinkedModelSerializer):
    aya = AyaSerializer(many= False) 
    class Meta:
        model = BookMark
        fields = [
            "url",
            "id",
            "aya",
            "created_time",
            "slug",
        ]
