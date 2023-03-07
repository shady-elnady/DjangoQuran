from rest_framework.viewsets import ModelViewSet
# from rest_framework.permissions import IsAuthenticated, IsAdminUser 

from .models import Qaria
from .Serializer import QariaSerializer 


class QariaViewSet(ModelViewSet):
    queryset = Qaria.objects.all()
    serializer_class = QariaSerializer
    # permission_classes = [IsAuthenticated, IsAdminUser]
