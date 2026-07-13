from django.db import models
from django.contrib.auth.models import User
from posts.models import Post
# Create your models here.

class Like(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    posts=models.ForeignKey(Post,on_delete=models.CASCADE)
    owner=models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['posts', 'owner'], name='unique_like')
        ]

    def __str__(self):
        return self.owner.username

class Comment(models.Model):
    comment=models.TextField(blank=True)
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    posts=models.ForeignKey(Post,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.owner.username

class Follow(models.Model):
    following=models.ForeignKey(User,on_delete=models.CASCADE,related_name='following')
    follower=models.ForeignKey(User,on_delete=models.CASCADE,related_name='follower')
    followed_at=models.DateTimeField(auto_now_add=True)
    class Meta:
        constraints = [
        models.UniqueConstraint(
            fields=["follower", "following"],
            name="unique_follow"
        )
    ]