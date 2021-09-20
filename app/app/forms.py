from django import forms
import datetime
from django.forms.fields import ChoiceField
from django.utils.text import slugify
import datetime


class InputDataForm(forms.Form):

    WIFE_EDUCATION = [(1 , 'Uneducated'),
        (2 , 'High School'),
        (3 , 'Graduated'),
        (4 , 'Post Graduated')]
    
    HUSBAND_EDUCATION = [(1 , 'Uneducated'),
        (2 , 'High School'),
        (3 , 'Graduated'),
        (4 , 'Post Graduated')]
    
    STANDARD_OF_LIVING = [(1 , 'Under Priviliged'),
        (2 , 'Basic'),
        (3 , 'Intermediate'),
        (4 , 'Luxurious')]

    wife_age = forms.IntegerField()
    wife_education = forms.ChoiceField(choices=WIFE_EDUCATION)
    husband_education = forms.ChoiceField(choices=HUSBAND_EDUCATION)
    number_of_children = forms.IntegerField()
    is_wife_islamic = forms.BooleanField(required=False)
    is_wife_non_working = forms.BooleanField(required=False)
    standard_of_living = forms.ChoiceField(choices= STANDARD_OF_LIVING)
    media_exposure = forms.BooleanField(required=False)

