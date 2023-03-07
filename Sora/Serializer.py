from rest_framework.serializers import HyperlinkedModelSerializer

from .models import Sora
from Aya.Serializer import AyaSerializer
# Serializers define the API representation.


class SoraSerializer(HyperlinkedModelSerializer):
    # Ayat = AyaSerializer(many= True)
    class Meta:
        model = Sora
        fields = [
            "url",
            "soraid",
            "name",
            "native",
            "place",
            "noOfVerses",
            # "Ayat",
            "slug",
        ]
