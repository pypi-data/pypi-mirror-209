from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

class RolesPermissionsViewSet(APIView):
    http_method_names = ['get']
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        roles = set([group.name for group in user.groups])
        permissions = set([permission.name for permission in user.permissions])
        data = {
            'roles': list(roles),
            'permissions': list(permissions)
        }
        return Response(data=data, status=status.HTTP_200_OK)