from albums.serializer import AlbumSerializer
from auth_client import *


@pytest.mark.django_db
def test_ser(album):
    serializer = AlbumSerializer(
        Album.objects.all(), many=True)
    assert serializer.data[0]['name'] == album.name


@pytest.mark.django_db
def test_deser(artist):
    serializer = AlbumSerializer(
        data=dict(
            name="kol",
            cost=10.1,
            releaseDate="1999-01-01",
            artists=artist
        )
    )
    assert serializer.is_valid()
    assert serializer.data['name'] == "kol"
