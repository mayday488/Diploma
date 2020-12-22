from datetime import datetime, timedelta, date

from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy

from .forms import RegistrationForm, TicketPurchaseForm, MovieCreationForm, SessionCreationForm, RoomCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, ListView, DetailView

from .models import Session, Movie, Hall, MovieTicket


class SignInView(LoginView):
    template_name = 'login.html'
    success_url = '/'
    next = '/'


class SignOutView(LogoutView):
    next_page = '/'


class SignUpView(CreateView):
    template_name = 'registration.html'
    form_class = RegistrationForm
    success_url = 'login'

    def get(self, request, *args, **kwargs):
        context = {'form': RegistrationForm()}
        return render(request, 'registration.html', context)

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            userprofile = form.save(commit=False)
            userprofile.save()
            credentials = form.cleaned_data
            userprofile = authenticate(username=credentials['username'],
                                       password=credentials['password1'])
            login(self.request, userprofile)
            return HttpResponseRedirect(reverse_lazy('main_page'))
        return render(request, 'registration.html', {'form': form})


def main_page(request):
    return render(request, 'main.html')


class TodaySessionsList(ListView):
    model = Session
    template_name = 'today_session_list.html'
    today_date = datetime.now().date()
    paginate_by = 10
    queryset = Session.objects.filter(start_datetime__contains=today_date)


# filter(start_datetime__contains=date().today())
class TomorrowSessionsList(ListView):
    model = Session
    template_name = 'tomorrow_sessions_list.html'
    today_date = datetime.now().date()
    queryset = Session.objects.filter(start_datetime__contains=today_date + timedelta(days=1))
    paginate_by = 10


# movie-related views:
class MovieCreationView(CreateView):
    model = Movie
    template_name = 'edit-page.html'
    form_class = MovieCreationForm
    success_url = '/list-of-movies/'


class MoviesList(ListView):
    model = Movie
    paginate_by = 10
    template_name = 'list-of-movies.html'
    queryset = Movie.objects.all()


# session-related views:
class SessionCreationView(CreateView):
    model = Session
    template_name = 'edit-page.html'
    form_class = SessionCreationForm
    success_url = '/list-of-sessions/'


class SessionsList(ListView):
    model = Session
    paginate_by = 10
    template_name = 'list-of-sessions.html'
    queryset = Session.objects.all()


# room-related views:
class RoomCreationView(CreateView):
    model = Hall
    template_name = 'edit-page.html'
    form_class = RoomCreationForm
    success_url = '/list-of-rooms/'


class RoomsList(ListView):
    model = Hall
    paginate_by = 10
    template_name = 'list-of-rooms.html'
    queryset = Hall.objects.all()


# session-related views:
class DetailedSessionView(DetailView):
    model = Session
    template_name = 'detailed_session_view.html'


# ticket-purchase view:
class TicketPurchaseView(CreateView):
    form_class = TicketPurchaseForm
    template_name = 'ticket-purchase.html'
    success_url = '/my-tickets/'


class TicketListView (ListView):
    model = MovieTicket
    paginate_by = 10
    template_name = 'list-of-tickets.html'

    def get_queryset(self):
        return MovieTicket.objects.filter(user=self.request.user)
