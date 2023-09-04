from django.contrib import admin
from .models import Post, Review, Appointment
# Register your models here.

admin.site.register(Post)
admin.site.register(Review)
admin.site.register(Appointment)