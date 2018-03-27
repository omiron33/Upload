from __future__ import unicode_literals

from django.db import models
from datetime import datetime
import re
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your models here.
class UserManager(models.Manager):
    def registration_validator(self,postData):
        errors = {}
        ## Registration
        if len(postData['name']) < 1:
            errors['name'] = "Name can't be empty"
        elif len(postData['name']) < 4:
            errors['name1'] = "Name must be greater than 3 characters"
        if len(postData['alias']) < 1:
            errors['alias'] = "Username can't be empty"
        elif len(postData['alias']) < 4:
            errors['alias'] = "Username must be greater than 3 characters"
        if len(postData['pw']) < 1:
            errors['pw_len'] = "Password field is empty"
        elif len(postData['pw']) < 8:
            errors['pw_len2'] = "Password is less than 8 characters"
        elif postData['pw'] != postData['confirm']:
             errors['pw'] = "Passwords do not match"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = 'Email is not a valid email address'
        if len(postData['dob']) == 0:
            errors['dob'] = 'Must enter valid birthday'
        elif datetime.strptime(postData['dob'], '%Y-%m-%d') >= datetime.today():
                errors['dob'] = "Birthday is not valid. You weren't born today or after."
        return errors
    def login_validator(self,postData):
        errors = {}
        ## Login
        if len(postData['logPW']) < 1:
            errors['pw_len'] = "Password field is empty"
        else:
            check = User.objects.filter(email = postData['logemail'])
            if len(check) < 1:
                errors['login'] = "User does not exist"
            elif not bcrypt.checkpw(postData['logPW'].encode(), check[0].password.encode()):
                errors['password'] = "Password is incorrect"
        return errors

class QuoteManager(models.Manager):
    def quote_validator(self,postData):
        errors = {}
        ## Registration
        if len(postData['author']) < 1:
            errors['author'] = "Author can't be empty"
        elif len(postData['author']) < 4:
            errors['author'] = "Author must be greater than 3 characters"
        if len(postData['message']) < 1:
            errors['message'] = "Message can't be empty"
        elif len(postData['message']) < 10:
            errors['message'] = "Author must be greater than 10 characters"
        
        return errors


class User(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)
    dob = models.DateTimeField()
    objects = UserManager()

class Quote(models.Model):
    quote = models.TextField()
    author = models.CharField(max_length=255)
    poster = models.ForeignKey(User, related_name="quotes")
    likers = models.ManyToManyField(User, related_name="favorites")
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)
    objects = QuoteManager()