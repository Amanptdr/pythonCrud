from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UserRegistrationSerializer,MyTokenObtainPairSerializer,RegisterSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

class HomeView(APIView):
     
   permission_classes = (IsAuthenticated, )
   def get(self, request):
       content = {'message': 'Welcome to the JWT Authentication page using React Js and Django!'}
       return Response(content)

class Testing(APIView):
   def get(self, request):
       content = {'message': 'THIS IS AMAN ','id':1}
       return Response(content)

class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
class UserRegistrationView(APIView):
    def post(self, request):
        print(request.data,"1222222222222")
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class LogoutView(APIView):
     permission_classes = (IsAuthenticated,)
     def post(self, request):
          
          try:
               refresh_token = request.data["refresh_token"]
               token = RefreshToken(refresh_token)
               token.blacklist()
               return Response(status=status.HTTP_205_RESET_CONTENT)
          except Exception as e:
               return Response(status=status.HTTP_400_BAD_REQUEST)
# @api_view(['GET'])
# def ApiOverview(request):
#     api_urls = {
#         'all_items': '/',
#         'Search by Category': '/?category=category_name',
#         'Search by Subcategory': '/?subcategory=category_name',
#         'Add': '/create',
#         'Update': '/update/pk',
#         'Delete': '/item/pk/delete'
#     }
 
#     return Response(api_urls)
# @api_view(['POST'])
# def add_category(request):
#     item = CategorySerializer(data=request.data)
 
#     # validating for already existing data
#     if Category.objects.filter(**request.data).exists():
#         raise serializers.ValidationError('This data already exists')
 
#     if item.is_valid():
#         item.save()
#         return Response(item.data)
#     else:
#         return Response(status=status.HTTP_404_NOT_FOUND)


# @api_view(['GET'])
# def view_category(request):
	
	
# 	# checking for the parameters from the URL
# 	if request.query_params:
# 		items = Category.objects.filter(**request.query_params.dict())
# 	else:
# 		items = Category.objects.all()
# 	# if there is something in items else raise error
# 	if items:
# 		serializer = CategorySerializer(items, many=True)
# 		return Response(serializer.data)
# 	else:
# 		return Response('status=status.HTTP_404_NOT_FOUND')



# @api_view(['POST'])
# def update_category(request, pk):
#     item = Category.objects.get(pk=pk)
#     data = CategorySerializer(instance=item, data=request.data)
 
#     if data.is_valid():
#         data.save()
#         return Response(data.data)
#     else:
#         return Response(status=status.HTTP_404_NOT_FOUND)


# @api_view(['DELETE'])
# def delete_category(request, pk):
#     item = get_object_or_404(Category, pk=pk)
#     item.delete()
#     return Response(status=status.HTTP_202_ACCEPTED)