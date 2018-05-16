from django.contrib import admin
from .models import Categories, Movies, Actors, Actresses, Directors, Reviews

admin.site.register(Categories)
admin.site.register(Movies)
admin.site.register(Actors)
admin.site.register(Actresses)
admin.site.register(Directors)
admin.site.register(Reviews)
