from django.contrib.auth.models import (AbstractBaseUser, AbstractUser,
                                        BaseUserManager, PermissionsMixin,
                                        User, UserManager)
from django.db import models

# Create your models here.

class UserManager(BaseUserManager):
    """

    """

    def create_user(self, email, password=None, type=None):
        if not email:
            raise ValueError('Пользователи должны иметь адрес электронной почты')

        user = self.model(email=self.normalize_email(email))

        user.type = type
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, type):
        user = self.create_user(email, password=password, type=type)
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom user with email authorization
    """

    TYPE = (
        (1, 'Пользватель'),
        (2, 'Мастер'),
        (3, 'Партнер')
    )


    class Meta:
        verbose_name = u'Пользователь'
        verbose_name_plural = u'Пользователи'

    email = models.EmailField(('email address'), unique=True)
    type = models.IntegerField(('type'), choices=TYPE, default=1)
    is_active = models.BooleanField(('active'), default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['type']


    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, EMAIL_HOST_USER, [self.email], fail_silently=True, **kwargs)

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def get_type(self):
        return self.type

    @property
    def is_staff(self):
        return self.is_admin

class Profile(models.Model):
    """
    User profile
    """

    class Meta:
        verbose_name = u'Профиль'
        verbose_name_plural = u'Профили'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Имя', max_length=64)
    last_name = models.CharField(verbose_name='Фамилия', max_length=64)



class Service(models.Model):

    class Meta:
        verbose_name = u'Услуга'
        verbose_name_plural = u'Услуги'


    name = models.CharField(max_length = 64, verbose_name = 'Имя')
    detail = models.TextField(max_length=512, verbose_name='Подробне')


class Master(models.Model):

    class Meta:
        verbose_name = u'Мастер'
        verbose_name_plural = u'Мастеры'


    name = models.CharField(max_length = 64, verbose_name = 'Имя')
    detail = models.TextField(max_length=512, verbose_name='Подробне')


class Salon(models.Model):

    class Meta:
        verbose_name = u'Салон'
        verbose_name_plural = u'Салоны'

    name = models.CharField(max_length=64, verbose_name='Имя')
    address = models.CharField(max_length=128, verbose_name='Адресс') 
