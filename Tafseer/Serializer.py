from rest_framework.serializers import HyperlinkedModelSerializer 

from .models import Tafseer

# Serializers define the API representation.


class TafseerSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Tafseer
        fields = [
            "url",
            "serial_no",
            "id",
            "title",
            "info",
            "type",
            "is_download",
            "slug",
        ]
