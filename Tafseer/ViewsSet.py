from rest_framework.viewsets import ModelViewSet
# from rest_framework.permissions import IsAuthenticated, IsAdminUser 

from .models import Tafseer
from .Serializer import TafseerSerializer 


class TafseerViewSet(ModelViewSet):
    queryset = Tafseer.objects.all()
    serializer_class = TafseerSerializer
    # permission_classes = [IsAuthenticated, IsAdminUser]
