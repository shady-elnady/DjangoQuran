from rest_framework.viewsets import ModelViewSet
# from rest_framework.permissions import IsAuthenticated, IsAdminUser 

from .models import Sora
from .Serializer import SoraSerializer 


class SoraViewSet(ModelViewSet):
    queryset = Sora.objects.all()
    serializer_class = SoraSerializer
    # permission_classes = [IsAuthenticated, IsAdminUser]
