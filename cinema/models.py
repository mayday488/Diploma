from django.contrib.auth.models import AbstractUser
from django.db import models


class CinemaUser(AbstractUser):
    pass

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Movie(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    duration = models.IntegerField()
    director = models.CharField(max_length=150)
    release_date = models.IntegerField(blank=True, null=True)
    cover_image = models.ImageField(
        upload_to='static/cover_images',
        default='static/default.png',
    )

    @property
    def film_duration(self):
        if self.duration // 60:
            return '{}h. {}m.'.format(self.duration // 60, self.duration % 60)
        return '{}minutes'.format(self.duration)

    def __str__(self):
        return self.title


class Hall(models.Model):
    title = models.CharField(max_length=100)
    number_of_seats = models.PositiveIntegerField()

    def __str__(self):
        return "{} | {} seats".format(self.title, self.number_of_seats)


class Session(models.Model):
    film = models.ForeignKey(Movie, on_delete=models.CASCADE)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    session_price = models.DecimalField(blank=False, decimal_places=2, max_digits=12, default=0.01)
    start_datetime = models.DateTimeField(blank=False)

    def __str__(self):
        return "{} | {} | {}".format(self.film.title, self.hall.title, self.session_price)


class MovieTicket(models.Model):
    session = models.ForeignKey(
        Session,
        on_delete=models.CASCADE,
        related_name='ticket_session'
    )
    user = models.ForeignKey(
        CinemaUser,
        on_delete=models.CASCADE,
        related_name='ticket_user'
    )
    date = models.DateTimeField()
    seat_number = models.PositiveIntegerField()

    class Meta:
        unique_together = ("date", "session", "seat_number")

    def __str__(self):
        return "{} | {} | {}".format(self.session.movie.title, self.seat_number, self.session.session_start)
