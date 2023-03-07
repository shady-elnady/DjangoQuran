from rest_framework.serializers import HyperlinkedModelSerializer 

from .models import Audio
from Qaria.Serializer import QariaSerializer
# Serializers define the API representation.


class AudioSerializer(HyperlinkedModelSerializer):
    qaria = QariaSerializer(many= False)
    class Meta:
        model = Audio
        fields = [
            "url",
            "id",
            "qaria",
            "type",
            "audio_url",
            "slug",
        ]
