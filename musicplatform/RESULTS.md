
# Results.md


### create some artists
 - Q)  Artist.objects.create(stageName="a",socialLink="AA")
 - A) <Artist: stageName is a>
 
### list down all artists
 - Q)  Artist.objects.all()
 - A) <QuerySet [<Artist: stageName is a>, <Artist: stageName is b>, <Artist: stageName is c>]>


### list down all artists sorted by name
 - Q)  Artist.objects.all().order_by('stageName')
 - A) <QuerySet [<Artist: stageName is a>, <Artist: stageName is b>, <Artist: stageName is c>]>

### list down all artists whose name starts with a
 - Q)  Artist.objects.filter(stageName__startswith='a')
 - A) <QuerySet [<Artist: stageName is a>, <Artist: stageName is acd>]>

### create some albums and assign them to any artists
 - Q)
   -  Album.objects.create(Artist=art1,releaseDate="2022-04-22",cost=20.0,name="nas")
   -  art2.album_set.create(Artist=art1,releaseDate="2055-04-22",cost=20.0,name="meen")
 - A) <Album: AlbumName is meen>

### get the latest released album
 - Q)  Album.objects.all().order_by("-releaseDate")[0]
 - A) <Album: AlbumName is New Album>


### get all albums released before today
 - Q)  Album.objects.filter(releaseDate__lt= datetime.date.today())
 - A) <QuerySet [<Album: AlbumName is hena>]>


### get all albums released today or before but not after today
 - Q) Album.objects.filter(releaseDate__lte= datetime.date.today())
 - A) <QuerySet [<Album: AlbumName is hena>, <Album: AlbumName is to>]>



### count the total number of albums
 - Q) Album.objects.count()
 - A) 5


### for each artist, list down all of his/her albums
 - Q1)
  
    arts=Artist.objects.all()
    
    d=dict()
    
    for a in arts:

    ____  d[a.stageName]=a.album_set.all()


 - A1) 
  
    {'': <QuerySet []>, 'a': <QuerySet [<Album: AlbumName is hena>]>, 'acd': <QuerySet []>, 'b': <QuerySet [<Album: AlbumName is meen>, <Album: AlbumName is nas>, <Album: AlbumName is New Album>, <Album: AlbumName is to>]>, 'c': <QuerySet []>}

 - Q2)
  
   albs=Album.objects.select_related('Artist')
   
    d=dict()
    
    for a in albs:

    ____  d.setdefault(a.Artist.stageName,[]).append(a.name)



 - A2)
  
   {'b': ['meen', 'nas', 'New Album', 'to'], 'a': ['hena']}

   

### list down all albums ordered by cost then by name
 - Q) Album.objects.all().order_by("cost","name")
 - A) <QuerySet [<Album: AlbumName is hena>, <Album: AlbumName is meen>, <Album: AlbumName is nas>, <Album: AlbumName is to>, <Album: AlbumName is New Album>]>

