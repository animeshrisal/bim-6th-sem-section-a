from django import forms
from .models import Movie, Review, User
from django.contrib.auth.forms import UserCreationForm

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields =  ['title', 'budget', 'genres']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review']

class UploadForm(forms.Form):
    file = forms.FileField()

class UserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user
