import datetime

from celery import *
from django.core.mail import send_mail

from albums.models import Album
from artists.models import Artist
from users.models import User


@shared_task()
def congrats(album, artist, mail):
    send_mail(
        'Congratulations',
        'Congratulations ' + artist + 'for the new album' + " " + album,
        'ashraf.teleb99@gmail.com',
        [mail],
        fail_silently=False,
    )


@shared_task
def check_email():
    start_date = datetime.datetime.now() - datetime.timedelta(30)
    albums = list(
        Album.objects.filter(creationDate__gte=start_date, creationDate__lte=datetime.datetime.now()).values_list(
            'artists', flat=True))
    artists = Artist.objects.filter()
    for x in artists:
        if x.pk not in albums:
            mail = User.objects.get(pk=x.owner_id).email
            send_mail(
                'Warning',
                'their inactivity is causing their popularity on our platform to decrease.',
                'ashraf.teleb99@gmail.com',
                [mail],
                fail_silently=False,
            )
