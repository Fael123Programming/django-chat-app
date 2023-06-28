from django.contrib import admin
from .models import Room, Message, User

admin.site.register(
    [
        Room,
        Message,
        User
    ]
)
