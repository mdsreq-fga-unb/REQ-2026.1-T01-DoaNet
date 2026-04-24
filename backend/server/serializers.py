from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ['id', 'username', 'password', 'email'] #define os campos que serão serializados (ou seja, serao preenchidos ao criar um novo usuário e passados para a api e serializados para o banco de dados)