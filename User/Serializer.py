from rest_framework.serializers import  HyperlinkedModelSerializer

from .models import User, Profile
from Languages.Serializer import LanguageSerializer


class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            "url",
            "username",
            "email",
            "slug",
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
 

class MyProfileSerializer(HyperlinkedModelSerializer):
    user = UserSerializer(many= False)
    language = LanguageSerializer(many= False)
    class Meta:
        model = Profile
        fields = [
            "url",
            "user",
            "image",
            "phone_number",
            "full_name",
            "family_name",
            "birth_date",
            "gender",
            "language",
            "created_date",
            "last_updated",
            "age",
            "slug",
        ]
