from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password':
                {
                'write_only': True,
                'required' : True
                }
            }
    # print('df')
    def create(self, validated_data):
        # print('df')
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user = user)
        return user
    
    
        