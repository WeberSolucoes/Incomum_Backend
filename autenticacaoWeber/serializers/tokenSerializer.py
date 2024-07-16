# serializers.py
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

class loginSerializer(TokenObtainPairSerializer):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['email'] = serializers.EmailField(required=True)
        self.fields['password'] = serializers.CharField(required=True, write_only=True, trim_whitespace=False)
    username_field = 'email'
    auth_fields = ('email', 'password')
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        attrs['username'] = attrs.get('email')
        del attrs['email']

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError('No user with this email')

        if not user.check_password(password):
            raise serializers.ValidationError('Incorrect password')

        refresh = self.get_token(user)

        data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

        return data

class registerSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True,validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

