from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class User(AbstractBaseUser):
    """
    customer user class.
    """
    email = models.EmailField('email address', unique=True, db_index=True)
    joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = model.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    
    def __unicode__(self):
        return self.email
