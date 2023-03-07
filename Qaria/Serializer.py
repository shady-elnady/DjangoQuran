from rest_framework.serializers import HyperlinkedModelSerializer 

from .models import Qaria

# Serializers define the API representation.


class QariaSerializer(HyperlinkedModelSerializer):
    
    class Meta:
        model = Qaria
        fields = [
            "url",
            "id",
            "name",
            "native",
            "slug",
        ]
