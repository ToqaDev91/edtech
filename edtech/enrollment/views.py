from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import extend_schema, OpenApiTypes
from .serializers import JSONFileUploadSerializer
from .service import bulk_process

@api_view(http_method_names=["GET"])
@permission_classes([AllowAny])
def test_api(request):
    ttt= "rrrr"
    return Response({"message": "Hello, World!"})

@extend_schema(
    request={
        'multipart/form-data': {
            'type': 'object',
            'properties': {
                'file': {
                    'type': 'string',
                    'format': 'binary',
                    'description': 'Upload a .json file'
                }
            },
            'required': ['file']
        }
    },
    responses={
        200: OpenApiTypes.OBJECT,
        400: OpenApiTypes.OBJECT
    }
)
@api_view(http_method_names=["POST"])
@permission_classes([AllowAny])
def start_enrollment(request):
    data = JSONFileUploadSerializer(data=request.data)
    if data.is_valid():
        bulk_process(raw_data=data.validated_data.get('file'))
    else:
        return Response(data.errors, status=HTTP_400_BAD_REQUEST)
    return Response({"message": "File uploaded successfully!"}, status=HTTP_200_OK)