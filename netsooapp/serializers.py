from rest_framework import serializers
from .models import User

class RegisterSerializer(serializers.Serializer):
    
    email = serializers.EmailField( max_length=225)
    firstName = serializers.CharField(allow_blank=True, max_length=100)
    lastName = serializers.CharField(allow_blank=True, max_length=100)
    password = serializers.CharField(allow_blank=True, max_length=100)
    
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        user = User.objects.create(email= validated_data['email'] , 
                 first_name = validated_data['firstName'],
                 last_name = validated_data['lastName'],
                 password = validated_data['password']
                 )
        user.set_password(validated_data['password'])
        user.save()
        return validated_data

    def validate(self, data):
        if data['email'] :
            if User.objects.filter(email=data['email']):
              raise serializers.ValidationError('email have been taken')
        return data
