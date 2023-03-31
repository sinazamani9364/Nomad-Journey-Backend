from rest_framework.views import APIView
from rest_framework import generics , status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer , UserCompeleteProfileSerializer , UserProfileEdit1Serializer,UserProfileEdit2Serializer
from .models import User
from .permissions import IsOwner
import jwt , datetime
from django.shortcuts import get_object_or_404
import json
from NormandJourney.tools import hash_sha256
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterView(APIView):
    permission_classes = (AllowAny,)
    def post(self, request):
        if request.method == "POST":
            # try:
            body = json.loads(request.body.decode('utf-8'))
            serializer = UserSerializer(data=body)
            serializer.is_valid(raise_exception=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)
            # except:
            #     return Response({"message": "Something went wrong:("}, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    permission_classes = (AllowAny, )
    def post(self, request):
        if request.method == "POST":
            try:
                body = json.loads(request.body.decode('utf-8'))

                email = body['email']
                password = body['password']

                user = User.objects.filter(email = email).first()

                if user is None:
                    raise AuthenticationFailed('User not found!')
                
                if not user.check_password(password):
                    raise AuthenticationFailed('Incorrect password!')
                
                payload = {
                    'id': user.id,
                    'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=2),
                    'iat': datetime.datetime.utcnow()
                }
                
                token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')

                response = Response()
                response.status_code = status.HTTP_200_OK
                response.set_cookie(key='jwt', value=token, httponly=True)
                response.data = {
                    'jwt': token,
                    'username': user.username
                }
                return response
            except:
                return Response({"message": "Something went wrong"}, status=status.HTTP_400_BAD_REQUEST)


class UserView(APIView):
    permission_classes=(IsAuthenticated,)
    def get(self , request):
        if request.method == "GET":
            token = request.COOKIES.get('jwt')
            
            if not token:
                raise AuthenticationFailed('Unauthenticated')
            
            try:
                payload = jwt.decode(token , 'secret' , algorithm=['HS256'])
            except jwt.ExpiredSignatureError:
                raise AuthenticationFailed('Unauthenticated')
            
            user = User.objects.filter(id = payload['id']).first()
            serializer = UserCompeleteProfileSerializer(user)
            return Response(serializer.data)

    
class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self , request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({
                'data': {},
                'message': "logout successfully"
            }, status=status.status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
class UserProfileList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserCompeleteProfileSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        return queryset
    
class UserProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwner,)
    queryset = User.objects.all()
    serializer_class = UserCompeleteProfileSerializer
    def get_object(self):
        UserName= self.kwargs.get("username")
        return get_object_or_404(User, username=UserName)


class UserProfileEdit1(APIView):
    def patch(self , request , username):
        try:
            body = json.loads(request.body.decode('utf-8'))
            user = User.objects.filter(username = username)
            if len(user) == 0:
                return Response({
                    'data': {},
                    'message':'invalid username'
                }, status = status.HTTP_400_BAD_REQUEST )
            if request.user.id != user[0].id:
                return Response({
                    'data': {},
                    'message':'you are not authorized to do this'
                }, status = status.HTTP_400_BAD_REQUEST )

            if body.get('first_name') is None:
                return Response({
                    'data': {},
                    'message':'firstname should not be null'
                }, status = status.HTTP_400_BAD_REQUEST )
            if body.get('last_name')  is None:
                return Response({
                    'data': {},
                    'message':'lastname should not be null'
                }, status = status.HTTP_400_BAD_REQUEST )
            if body.get('username')  is None:
                return Response({
                    'data': {},
                    'message':'username should not be null'
                }, status = status.HTTP_400_BAD_REQUEST )
            serializer = UserProfileEdit1Serializer(user[0] , data = body , partial = True)
            if not serializer.is_valid():
                return Response({
                    'data': serializer.errors,
                    'message':'something went wrong'
                } , status = status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response({
                'data': serializer.data,
                'message' : 'user updated successfully'
            } , status = status.HTTP_201_CREATED)
        except Exception as e:
            print(e) 
            return Response({
                'data': {},
                'message':'something went wrong'
            }, status = status.HTTP_400_BAD_REQUEST )


class UserProfileEdit2(APIView):
    def patch(self , request , username):
        try:
            body = json.loads(request.body.decode('utf-8'))
            user = User.objects.filter(username = username)
            if len(user) == 0:
                return Response({
                    'data': {},
                    'message':'invalid username'
                }, status = status.HTTP_400_BAD_REQUEST )
            if request.user.id != user[0].id:
                return Response({
                    'data': {},
                    'message':'you are not authorized to do this'
                }, status = status.HTTP_400_BAD_REQUEST )

            if body.get('User_city') is None:
                return Response({
                    'data': {},
                    'message':'city field should not be null'
                }, status = status.HTTP_400_BAD_REQUEST )
            if body.get('User_country')  is None:
                return Response({
                    'data': {},
                    'message':'country field should not be null'
                }, status = status.HTTP_400_BAD_REQUEST )
            if body.get('User_postal_code')  is None:
                return Response({
                    'data': {},
                    'message':'postal code field should not be null'
                }, status = status.HTTP_400_BAD_REQUEST )
            serializer = UserProfileEdit2Serializer(user[0] , data = body , partial = True)
            if not serializer.is_valid():
                return Response({
                    'data': serializer.errors,
                    'message':'something went wrong'
                } , status = status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response({
                'data': serializer.data,
                'message' : 'user updated successfully'
            } , status = status.HTTP_201_CREATED)
        except Exception as e:
            print(e) 
            return Response({
                'data': {},
                'message':'something went wrong'
            }, status = status.HTTP_400_BAD_REQUEST )

