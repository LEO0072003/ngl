from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import status
from .serializers import RegisterSerializer, UserAppDownloadSerializer, UserAppDownloadCreateSerializer
from .models import UserAppDownload
from drf_spectacular.utils import extend_schema
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

class RegisterAPIView(APIView):
    @extend_schema(
        request=RegisterSerializer,
        responses={201: "User Created",400:None},
        description="Register User"
    )

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Calls the `create` method in the serializer
            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema_view(
    create=extend_schema(
        request=UserAppDownloadSerializer,
        responses={201: UserAppDownloadSerializer},
        description="Validate App Download.",
    ),
    list=extend_schema(
        request=UserAppDownloadSerializer,
        responses={200: UserAppDownloadSerializer},
        description="List All Taks Done",
    ),
)
class AppDownloadViewset(CreateModelMixin, ListModelMixin, GenericViewSet):
    """Viewset to list and create new app upload task"""
    permission_classes = [IsAuthenticated]
    # serializer_class = UserAppDownloadSerializer
    queryset = UserAppDownload.objects.all()

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return UserAppDownload.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
            # Check the HTTP method and return the appropriate serializer
            if self.action == 'create':
                return UserAppDownloadCreateSerializer
            else:
                return UserAppDownloadSerializer
