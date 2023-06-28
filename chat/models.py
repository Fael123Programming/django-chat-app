from django.db import models


class Room(models.Model):
    url = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['url', 'name'],
                name='unique room'
            )
        ]
        
    def __str__(self):
        return self.url


class User(models.Model):
    name = models.CharField(max_length=100)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'room'],
                name='unique user'
            )    
        ]
        
    def __str__(self):
        return f'({self.room}) {self.name}'

    
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.CharField(max_length=1000000)
    timestamp = models.DateTimeField(
        auto_now_add=True,
        blank=True
    )

    def __str__(self):
        return f'{self.user}: {self.value} ({self.timestamp})'
