from rest_framework.serializers import HyperlinkedModelSerializer 

from .models import Language, AyaLanguage
from Aya.Serializer import AyaSerializer
from Sora.Serializer import SoraSerializer
# Serializers define the API representation.


class LanguageSerializer(HyperlinkedModelSerializer):
    
    class Meta:
        model = Language
        fields = [
            "url",
            "id",
            "name",
            "native",
            "symbol",
            "rtl",
            "emoji",
            "slug",
        ]


class AyaLanguageSerializer(HyperlinkedModelSerializer):
    sora = SoraSerializer(many= False)
    aya = AyaSerializer(many= False)
    class Meta:
        model = AyaLanguage
        fields = [
            "url",
            "language",
            "sora",
            "aya",
            "text",
            "slug",
        ]
