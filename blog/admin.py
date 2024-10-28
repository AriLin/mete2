from django.contrib import admin
from .models import Post
from users.models import Profile,Aurinko,Pumppu,Valaisin

admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Aurinko)
admin.site.register(Pumppu)
admin.site.register(Valaisin)