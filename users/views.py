import uuid
import random

from django.core.cache import cache
from rest_framework.decorators import api_view

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User, Device
from .helpers import send_otp_to_phone


# @api_view(['POST'])
# def send_otp(request):
#     data = request.data
#
#     if data.get('phone_number') is None:
#         return Response({
#             'status': 400,
#             'message': 'key phone_number is required'
#         })
#     if data.get('password') is None:
#         return Response({
#             'status': 400,
#             'message': 'key phone_number is required'
#         })
#
#     user = User.objects.create(
#         phone_number = data.get('phone_number'),
#     otp = send_otp_to_phone(data.get('phone_number'))
#     )
#     user.set_password = data.get('set_password')
#     user.save()
#
#     return Response({
#         'status': 200, 'message': 'Otp Sent'
#     })


class RegisterView(APIView):

    def post(self, request):
        phone_number = request.data.get('phone_number')

        if not phone_number:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(phone_number=phone_number)
            # return Response({'detail': 'User already registered!'},
            #                 status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            user = User.objects.create_user(phone_number=phone_number)

        # user, created = User.objects.get_or_create(phone_number=phone_number)

        device = Device.objects.create(user=user)

        code = random.randint(10000, 99999)

        # send message (sms or email)
        # cache
        cache.set(str(phone_number), code, 2 * 60)

        return Response({'code': code})


class GetTokenView(APIView):

    def post(self, request):
        phone_number = request.data.get('phone_number')
        code = request.data.get('code')

        cached_code = cache.get(str(phone_number))
        print(cached_code)

        if code != cached_code:
            return Response(status=status.HTTP_403_FORBIDDEN)

        token = str(uuid.uuid4())
        print(token)

        return Response({'token': token})
