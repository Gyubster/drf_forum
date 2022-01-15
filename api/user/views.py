from rest_framework                 import generics, status
from rest_framework.permissions     import AllowAny
from rest_framework.response        import Response

from .serializers import UserSignInSerializer, UserSignUpSerializer
from user.models  import User

class UserSignIn(generics.GenericAPIView):
    queryset            = User.objects.all()
    serializer_class    = UserSignInSerializer
    permission_classes  = [AllowAny]

    def post(self, request):
        serializer = UserSignInSerializer(data = request.data)
        
        if not serializer.is_valid(raise_exception=True):
            return Response({"message": "Request Body Error."}, status=status.HTTP_409_CONFLICT)
        
        if serializer.validated_data['email'] == 'None':
            return Response({"message": "fail"}, status=status.HTTP_200_OK)
        response = {
                "access_token": serializer.validated_data['access_token']
                }

        return Response(response, status=status.HTTP_200_OK)

class UserSignUp(generics.CreateAPIView):
    queryset            = User.objects.all()
    serializer_class    = UserSignUpSerializer
    permission_classes  = [AllowAny]
