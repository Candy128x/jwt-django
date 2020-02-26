from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class HomeView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Welcome to FCT..'}
        return Response(content)

    def register(self, request):
        serialized = UserSerializer(data=request.data)
        if serialized.is_valid():
            User.objects.create_user(
                serialized.init_data['email'],
                serialized.init_data['username'],
                serialized.init_data['password']
            )
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)