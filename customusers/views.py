from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        data = request.data
        username = data.get('username', None)
        password = data.get('password', None)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({"success": "User logged in."}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Wrong credentials."}, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, format=None):
        logout(request)
        return Response({"success": "User logged out."}, status=status.HTTP_200_OK)
        