from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from getotp.models import OtpRequest, OtpRequest
from getotp.serializers import RequestOtpSerializer, RequestOtpResponseSerializer


class RequestOtp(APIView):
    def post(self, request):
        serializer = RequestOtpSerializer(data=request.data)
        if serializer.is_valid():
            req_otp = OtpRequest()
            req_otp.phone = serializer.validated_data['phone']
            req_otp.channel = serializer.validated_data['phone']
            req_otp.generate_password()
            req_otp.save()

            return Response(RequestOtpResponseSerializer(req_otp).data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyOtp(APIView):
    def post(self, req_otp):
        pass
