from django import forms
from captcha.fields import ReCaptchaField
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    

    username = forms.CharField(label = "username")
    password = forms.CharField(label = "password",widget = forms.PasswordInput)
    captcha = ReCaptchaField()

class RegisterForm(forms.Form):
    

    username = forms.CharField(max_length = 50,label = "username")
    password = forms.CharField(max_length=20,label = "password",widget = forms.PasswordInput)
    confirm = forms.CharField(max_length=20,label ="password(again)",widget = forms.PasswordInput)
    captcha = ReCaptchaField()
  
    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")



        if password and confirm and password != confirm:
            raise forms.ValidationError("Username or password did not match!")
         
        values = {
            "username" : username,
            "password" : password
        }
        return values
    
    def clean_username(self):
        username = self.cleaned_data.get('username')

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(u'Username "%s" is already in use.' % username)

       

