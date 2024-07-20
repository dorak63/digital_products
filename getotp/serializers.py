from rest_framework import serializers

from getotp.models import OtpRequest


class RequestOtpSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=12, allow_null=False)
    channel = serializers.ChoiceField(allow_null=False, choices=['android', 'ios', 'web'])


# class RequestOtpResponseSerializer(serializers.Serializer):
#     class Meta:
#         model = OtpRequest
#         fields = ['request_id']
class RequestOtpResponseSerializer(serializers.Serializer):
    request_id = serializers.CharField()
    password = serializers.CharField()
    # Add other fields if needed


class VerifyOtpSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=12, allow_null=False)
    password = serializers.CharField(allow_null=False)


class VerifyOtpResponseSerializer(serializers.Serializer):
    token = serializers.CharField()
    new_user = serializers.BooleanField()
