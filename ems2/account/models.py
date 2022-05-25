from faulthandler import disable
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings
# from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _


class State(models.Model):
    state = models.CharField(max_length=128,null=True,blank=True)

    class Meta:
        db_table = 'account_state'
        verbose_name = _('state')
        verbose_name_plural = _('states')
        ordering = ('-pk',)

    def __str__(self):
        return str(self.state)


class District(models.Model):
    district = models.CharField(max_length=128,null=True,blank=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    class Meta:
        db_table = 'account_district'
        verbose_name = _('district')
        verbose_name_plural = _('districts')
        ordering = ('-pk',)

    def __str__(self):
        return str(self.district)


class MyAccountManager(BaseUserManager):
    def create_user(self, phone,email, password):
        if not phone:
            raise ValueError('Users must have a phone')

        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            phone=phone,
            email=self.normalize_email(email),            
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,phone,password):
        user = self.create_user(
            phone=phone,
            email="example@gmail.com",
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60,)
    phone = models.CharField(max_length=60, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    username = models.CharField(max_length=140)
    phone_code = models.CharField(max_length=30,default="91")
    address = models.CharField(max_length=140,)
    district = models.ForeignKey(District, on_delete=models.CASCADE,blank=True,null=True)


    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    # ordering = ('email',)

    objects = MyAccountManager()

    def __str__(self):
        return str(self.phone)

    def has_perm(self,perm,obj=None):
        return self.is_admin
        
    def has_module_perms(self,app_label):
        return True

    # class Meta:
    #     ordering = ('email',)


