from django.contrib import admin

# Register your models here.

from .models import CinemaUser, Hall, Movie, Session, MovieTicket

admin.site.register(MovieTicket)
admin.site.register(CinemaUser)
admin.site.register(Hall)
admin.site.register(Movie)
admin.site.register(Session)
