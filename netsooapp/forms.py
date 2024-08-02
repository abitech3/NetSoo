from django.forms import ModelForm
from django.contrib.auth import get_user_model 
from django import forms
from django.contrib.auth.forms import UserCreationForm



User = get_user_model()


class RegistrationForm(UserCreationForm):
     def __init__(self, *args, **kwargs):
        super().__init__(*args , **kwargs)
        self.fields['password1'].widget.attrs.update({
            'class' : 'form-control'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control'
        })

     class Meta:
        model = User
        fields = ["email", "first_name", "last_name"]
        widgets = {
             'email': forms.EmailInput(attrs={'class': 'form-control' ,  'name':'email'}),
             'first_name': forms.TextInput(attrs={'class': 'form-control' ,  'name':'fname'}),      
             'last_name': forms.TextInput(attrs={'class': 'form-control' ,  'name':'lname'}),      
             
           }
     


class UserUpdateForm(ModelForm):

    class Meta:
         model = User

         fields = "__all__"

         widgets = {
             
             'first_name': forms.TextInput(attrs={'class': 'form-control','name':'fname'}),
             'last_name': forms.FileInput(attrs={'class': 'form-control', 'name':'lname'}),
             'email': forms.EmailInput(attrs={'class': 'form-control' ,'name':'email'}),
               }



