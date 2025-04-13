from rest_framework import status

from rest_framework.views import APIView
from rest_framework.generics import (
    CreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from .models import Url
from .serializers import CreateSerializer, SignUpSerializer


# Create your views here.


class SignUpView(APIView):
    serializer_class = SignUpSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ShortenView(CreateAPIView):
    model = Url
    serializer_class = CreateSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.request.user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ShortenDetailView(RetrieveUpdateAPIView):
    queryset = Url.objects.all()
    serializer_class = CreateSerializer
    permission_classes = [
        IsAuthenticated,
    ]
    lookup_field = "short_code"

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.access_count += 1
        instance.save(update_fields=["access_count"])
        serializer = self.serializer_class(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_class(instance, data=request.data, partial=False)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
