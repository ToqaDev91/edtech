import json
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_403_FORBIDDEN
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import extend_schema, OpenApiTypes
from .serializers import JSONFileUploadSerializer

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
    responses={200: OpenApiTypes.OBJECT}
)
@api_view(http_method_names=["POST"])
@permission_classes([AllowAny])
#@parser_classes([MultiPartParser])
def start_enrollment(request):
    data = JSONFileUploadSerializer(data=request.data)
    if data.is_valid():
        # Process the valid data
        pass
    return Response({"message": "File uploaded successfully!"})