from django.shortcuts import render
from django.contrib.auth.models import User
from recipe.serializers import ReviewSerializer,RecipeSerializer,UserSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from recipe.models import Recipe,Review
from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class RecipeViewSet(viewsets.ModelViewSet):
    queryset=Recipe.objects.all()
    serializer_class=RecipeSerializer

class ReviewSerializer(viewsets.ModelViewSet):
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer

class UserViewSet(viewsets.ModelViewSet):  # get,post,put,delete
    queryset = User.objects.all()
    serializer_class = UserSerializer

class user_logout(APIView):
        permission_classes = [IsAuthenticated, ]
        def get(self, request):
            self.request.user.auth_token.delete()
            return Response({"message": "logout successfully"}, status=status.HTTP_200_OK)


class Createrev(APIView):
    permission_classes = [IsAuthenticated, ]
    def POST(self,request):
        r=ReviewSerializer(data=request.data)
        if r.is_valid():
            r.save()
            return Response(r.data,status=status.HTTP_201_CREATED)
        return Response(status.HTTP_400_BAD_REQUEST)


class Detailrev(APIView):
    permission_classes = [IsAuthenticated, ]
    def get_object(self,pk):
        try:
            return Recipe.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk):
        r = self.get_object(pk)
        rev = Review.objects.filter(recipe_name=r)
        revdet = ReviewSerializer(rev, many=True)
        return Response(revdet.data)

#filter based on cuisine
class CuisineFilter(APIView):           #eg:queryparameter:{'cuisine':'chinese'}
    def get(self,request):
        query = self.request.query_params.get('cuisine')
        recipes = Recipe.objects.filter(cuisine=query)
        r=RecipeSerializer(recipes,many=True)
        return Response(r.data)

#filter based on meal type
class MealFilter(APIView):          #eg:queryparameter:{'mealtype':'chinese'}
    def get(self,request):
        query = self.request.query_params.get('meal_type')
        recipes = Recipe.objects.filter(meal_type=query)
        r=RecipeSerializer(recipes,many=True)
        return Response(r.data)

#filter based on ingredients
class IngreditesFilter(APIView):        #eg:queryparameter:{'ingredients':'chinese'}
    def get(self,request):
        query = self.request.query_params.get('recipe_ingredients')#here ingredient is keyword
        recipes = Recipe.objects.filter(recipe_ingredients=query)#here its is fieldname
        r=RecipeSerializer(recipes,many=True)
        return Response(r.data)