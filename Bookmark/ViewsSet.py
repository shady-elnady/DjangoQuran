from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated 

from .models import BookMark
from .Serializer import BookMarkSerializer 


class BookMarkViewSet(ModelViewSet):
    queryset = BookMark.objects.all()
    serializer_class = BookMarkSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return BookMark.objects.all().filter(user=self.request.user)
