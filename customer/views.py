from django.shortcuts import render, redirect
from .forms import ClassForm
import requests
from customer.forms import UserAdminCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from rest_framework.authtoken.models import Token


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import StudentProfileSerializer
from django.views import View

class AddClassView(View):
    template_name = 'add_class.html'  

    def get(self, request):
        form = ClassForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ClassForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')  
        return render(request, self.template_name, {'form': form})
    
class RegisterView(View):
    template_name = 'customer.html' 

    def get(self, request):
        form = UserAdminCreationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserAdminCreationForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('login')  
        return render(request, self.template_name, {'form': form})



class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        form = AuthenticationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            #if user and user.status == 'True':
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return redirect('profile')  
            

        return render(request, self.template_name, {'form': form})




    


class UpdateProfileAPIView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = StudentProfileSerializer(user)
        return Response(serializer.data)

    def put(self, request):
        user = request.user
        serializer = StudentProfileSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)



        