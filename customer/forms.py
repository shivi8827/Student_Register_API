from django import forms
from .models import Class, CustomUser


from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['class_name']



class UserAdminCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ['phone','student_class']
       



