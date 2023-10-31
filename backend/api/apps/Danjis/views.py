from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import DanjisSerializer
from .models import Danjis


class DanjisViewSet(viewsets.ModelViewSet):
    queryset = Danjis.objects.all()
    serializer_class = DanjisSerializer

    def post(self, request, *args, **kwargs):
        danjis = self.get_object()
        serializer = DanjisSerializer(data=request.data)
        if serializer.is_valid():
            post = danjis.save(commit=False)
            post.code = '0001'
            post.profile_img = request.code + '/' + request.profile_img
            post.save()
            return Response({'status': 'Danji set.'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
