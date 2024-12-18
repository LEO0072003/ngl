from rest_framework.response import Response
from app.serializers import AppSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from app.models import App, Category, SubCategory
from core.permission import AdminUserPermission
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.pagination import PageNumberPagination
# Create your views here.

class AppPagination(PageNumberPagination):
    page_size = 10  # Number of items per page
    max_page_size = 10  # Maximum number of items per page


@extend_schema_view(
    create=extend_schema(
        request=AppSerializer,
        responses={201: AppSerializer},
        description="Add a new app by providing details in the body.",
    ),
    list=extend_schema(
        request=AppSerializer,
        responses={200: AppSerializer},
        description="List All Apps",
    ),
    retrieve=extend_schema(
        request=AppSerializer,
        responses={200: AppSerializer},
        description="Retrieve a particular app.",
    ),
    update=extend_schema(
        request=AppSerializer,
        responses={200: AppSerializer},
        description="Update an existing app with optional chapters.",
    ),
    delete=extend_schema(
        request=AppSerializer,
        responses={204: AppSerializer},
        description="Delete the App",
    )
)
class AppViewSet(ModelViewSet):
    """Viewset for app models"""

    serializer_class = AppSerializer
    queryset = App.objects.all()
    pagination_class = AppPagination

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'GET':
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [IsAuthenticated,AdminUserPermission]
        return super().dispatch(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        print(request.FILES)
        print(request.POST)
        return super().create(request, *args, **kwargs)


class CategoryApiView(ListAPIView):
    def get(self, request, *args, **kwargs):
        # Fetch only category names with values_list
        category_names = Category.objects.all().values_list('id','category_name')

        return Response(data=category_names)


class SubCategoryApiView(ListAPIView):
    def get(self, request, *args, **kwargs):
        category = kwargs.get('pk')
        sub_category_names = SubCategory.objects.filter(category=category).all().values_list('id', 'sub_category_name')
        return Response(data=sub_category_names)
