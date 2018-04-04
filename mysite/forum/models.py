from django.db import models
from django.utils import timezone
#import datetime

# Create new databases here
class User(models.Model):
    user_id = models.AutoField(max_length=8, primary_key=True)
    user_name = models.CharField(max_length=30, null=False, unique=True)
    user_pass = models.CharField(max_length=255, null=False)
    user_email = models.CharField(max_length=255, null=False)
    user_date = models.DateTimeField(default=timezone.now)
    user_level = models.IntegerField(null=False)

    def new_user(self):
        self.save()

    def __str__(self):
        return self.user_name

class Categories(models.Model):
    cat_id = models.AutoField(max_length=8, primary_key=True)
    cat_name = models.CharField(max_length=255, null=False, unique=True)
    cat_description = models.CharField(max_length=255, null=False)

class Topics(models.Model):
    topic_id = models.AutoField(max_length=8, primary_key=True)
    topic_subject = models.CharField(max_length=255, null=False)
    topic_date = models.DateTimeField(null=False)
    topic_cat = models.IntegerField(null=False)
    topic_by = models.IntegerField(null=False)
    topic_deletion = models.ForeignKey(Categories, on_delete=models.DO_NOTHING)
    #DO_NOTHING is a replacement for restrict (prevents user from deleteing all topics they've made)
    topic_user_deletion = models.ForeignKey(User, on_delete=models.DO_NOTHING)

class Posts(models.Model):
    post_id = models.AutoField(max_length=8, primary_key=True)
    post_content = models.TextField(null=False)
    post_date = models.DateTimeField(null=False)
    post_topic = models.IntegerField(null=False)
    post_by = models.IntegerField(null=False)
    models.ForeignKey(Topics, on_delete=models.CASCADE)
    models.ForeignKey(User, on_delete=models.DO_NOTHING)