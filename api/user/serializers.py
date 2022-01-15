from django.contrib.auth.models     import update_last_login
from django.contrib.auth            import authenticate, get_user_model
from rest_framework                 import serializers
from rest_framework_jwt.settings    import api_settings

JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER  = api_settings.JWT_ENCODE_HANDLER
User = get_user_model()

class UserSignUpSerializer(serializers.ModelSerializer):
    
    class Meta:
        model        = User
        fields       = ['email', 'nickname', 'password']
        extra_kwargs = {
                'email': {'required':True},
                'nickname': {'required':True},
                'password': {'required':True},
                } 

    def create(self, validated_data):
        user = User.objects.create(
                email       = validated_data['email'],
                nickname    = validated_data['nickname']
                )
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserSignInSerializer(serializers.Serializer):
    email       = serializers.CharField(max_length=64)
    password    = serializers.CharField(max_length=128, write_only=True)
    token       = serializers.CharField(max_length=255, read_only=True)
                    
    def validate(self, data):
        email       = data.get('email', None)
        password    = data.get('password', None)
        
        user = authenticate(email=email, password=password)
        if user is None:
            results = {
                    'email':'None'
                    }
            return results
        
        try:
            payload     = JWT_PAYLOAD_HANDLER(user)
            jwt_token   = JWT_ENCODE_HANDLER(payload)

            update_last_login(None, user)

        except User.DoesNotExist:
            raise serializers.ValidationError(
                'User with given email and password does not exists'
            )
        
        results = {
                'email'       : user.email,
                'access_token': jwt_token
            }

        return results 
