from django.contrib import admin
from .models import NeighbourHood,Post,Business,Profile

# Register your models here.
admin.site.register(NeighbourHood),
admin.site.register(Post),
admin.site.register(Business),
admin.site.register(Profile)

