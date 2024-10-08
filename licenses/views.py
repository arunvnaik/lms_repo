# licenses/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import License
from .serializers import LicenseSerializer

class ValidateLicense(APIView):
    def post(self, request, *args, **kwargs):
        key = request.data.get('license_key')
        try:
            license = License.objects.get(key=key)
            serializer = LicenseSerializer(license)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except License.DoesNotExist:
            return Response({'status': 'Invalid License'}, status=status.HTTP_400_BAD_REQUEST)
