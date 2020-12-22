from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, Form

from .models import CinemaUser, Hall, Movie, Session


class RegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=20, required=True)
    email = forms.EmailField(max_length=255, required=False)

    class Meta:
        model = CinemaUser
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        for fieldname in ['password1', 'password2']:
            self.fields[fieldname].help_text = None


class RoomCreationForm(ModelForm):
    class Meta:
        model = Hall
        fields = ('title', 'number_of_seats')


class MovieCreationForm(ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'description', 'duration', 'director', 'release_date', 'cover_image')


class SessionCreationForm(ModelForm):
    class Meta:
        model = Session
        fields = ('film', 'hall', 'session_price', 'start_datetime')


class TicketPurchaseForm(Form):
    class Meta:
        fields = ('session', 'date', 'seat_number')
