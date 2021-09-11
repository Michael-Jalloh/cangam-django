from django import forms
from django.forms import modelformset_factory
# from django.contrib.auth import authenticate
from django.db.models import fields
# from allauth.account.forms import SignupForm
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import Group
from .models import Question, Option

class QuestionModel(forms.ModelForm):
     
    class Meta:
        model = Question
        fields = ('text',)
        widgets = {
                'question' : forms.TextInput(attrs={'class':'form-control','id':'question','name':'basic-default-name','placeholder':'Enter Question'}),
                
                

               
            }
