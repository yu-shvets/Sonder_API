from django.contrib import admin
from .models import Posts, Comments, Messages

admin.site.register(Posts)
admin.site.register(Comments)
admin.site.register(Messages)
