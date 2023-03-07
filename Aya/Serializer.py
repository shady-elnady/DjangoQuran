from rest_framework.serializers import HyperlinkedModelSerializer 

from .models import Aya

# Serializers define the API representation.



class AyaSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Aya
        fields = [
            "url",
            "id",
            "soraid",
            "ayaid",
            "page",
            "quarter",
            "hezb",
            "joza",
            "sajda",
            "text",
            "uthmanitext",
            "searchtext",
            "quarterstart",
            "slug",
        ]
