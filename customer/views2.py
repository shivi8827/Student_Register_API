from django.shortcuts import render
from .forms import ClassForm

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
# from accounts.forms import UserAdminCreationForm
from customer.forms import UserAdminCreationForm,StudentProfileForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
from django.contrib.auth.forms import AuthenticationForm

from rest_framework.authtoken.models import Token

# def add_class(request):
#     if request.method == 'POST':
#         form = ClassForm(request.POST)
#         if form.is_valid():
#             form.save()
#     else:
#         form = ClassForm()
#     return render(request, 'add_class.html', {'form': form})
from django.views import View
class AddClassView(View):
    template_name = 'add_class.html'  # Set your template name here

    def get(self, request, *args, **kwargs):
        form = ClassForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = ClassForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_url_name')  # Redirect to a success URL after saving
        return render(request, self.template_name, {'form': form})
class RegisterView(View):
    template_name = 'customer.html'  # Set your template name here

    def get(self, request, *args, **kwargs):
        form = UserAdminCreationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = UserAdminCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()
            # Redirect to the profile or another URL after successful registration
            return redirect('profile')  # Replace 'profile' with your desired URL name
        return render(request, self.template_name, {'form': form})


# def register(req):
#     form = UserAdminCreationForm()
#     if req.method == 'POST':
#         form = UserAdminCreationForm(req.POST)
#         if form.is_valid():
#             user = form.save(commit=False)  # Don't save yet
#             user.is_active = True  # Set inactive status
#             user.save()
#             #form.save()
#            # return redirect('profile')
#     return render(req, 'customer.html', {'form': form})



def home_view(request):
    return render(request, 'home.html')

from django.contrib import messages

class LoginView(View):
    template_name = 'login.html'  # Set your template name here

    def get(self, request):
        form = AuthenticationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.is_active:
                login(request, user)
                token, created = Token.objects.get_or_create(user=user)
                return redirect('profile')  # Redirect to profile or another URL
            else:
                error_message = "Your account is not yet activated."
                return render(request, self.template_name, {'form': form, 'error_message': error_message})

        return render(request, self.template_name, {'form': form})





    




from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import StudentProfileSerializer

class UpdateProfileAPIView(APIView):
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]

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