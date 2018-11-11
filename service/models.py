from django.contrib.auth.models import (AbstractBaseUser, AbstractUser,
                                        BaseUserManager, PermissionsMixin,
                                        User, UserManager)
from django.db import models

from .utils.sms_api import sendSms
from django.core.mail import send_mail
from choco.settings import EMAIL_HOST_USER

# Create your models here.

class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)
    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)

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
        return self.email

    def send_sms(self, code):
        sendSms(phone = self.profile.phone, message = code)
        return code

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
    phone = models.CharField(verbose_name='Номер тел', max_length=14, default = '87000000000')

    def send_sms():
        return true

    def __str__(self):
        return ('%s %s'%(self.user.email, self.name))


class Service(models.Model):

    class Meta:
        verbose_name = u'Услуга'
        verbose_name_plural = u'Услуги'


    name = models.CharField(max_length = 64, verbose_name = 'Имя')
    detail = models.TextField(max_length=512, verbose_name='Подробне')

    def __str__(self):
        return self.name

class Salon(models.Model):

    class Meta:
        verbose_name = u'Салон'
        verbose_name_plural = u'Салоны'

    name = models.CharField(max_length=64, verbose_name='Имя')
    address = models.CharField(max_length=128, verbose_name='Адресс')

    def __str__(self):
        return self.name


class Master(models.Model):

    class Meta:
        verbose_name = u'Мастер'
        verbose_name_plural = u'Мастеры'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    salon  = models.ForeignKey(Salon, on_delete=models.CASCADE, verbose_name = u'Салон')
    service = models.ManyToManyField(Service, verbose_name = u'Услуга')
    experience = models.IntegerField(default=0, verbose_name='Опыт работы')
    rating = IntegerRangeField(min_value=0, max_value=100, verbose_name='Рейтинг')
    
    def __str__(self):
        return ('%s-%s'%(self.user, self.salon))


class Order(models.Model):

    class Meta:
        verbose_name = u'Заказ'
        verbose_name_plural = u'Заказы'

    STATUS = (
        (1, 'Не подтвержден'),
        (2, 'Подтвержден')
    )
    TYPE = (
        (1, 'Новый заказ'),
        (2, 'Услуга оказан'),
        (3, 'Отменен')
    )
    user = models.ForeignKey(User, verbose_name=u'Пользователь', on_delete=models.CASCADE)
    master = models.ForeignKey(Master, on_delete=models.CASCADE)
    create_at = models.DateField(verbose_name='Дата создания', auto_now_add=True)
    state = models.IntegerField(verbose_name='Статус', choices=STATUS, default=1)
    type = models.IntegerField(verbose_name='Тип заказа', choices=TYPE, default=1)
    date = models.DateField(verbose_name=u'Дата')
    time = models.TimeField(verbose_name=u'Время')


    def __str__(self):
        return ('%s-%s'%(self.user.profile, self.master.service))


class Comments(models.Model):
    master = models.ForeignKey(Master, on_delete=models.CASCADE)
    name = models.CharField(verbose_name=u'Пользователь', max_length = 64)
    content = models.TextField(max_length=200)

    def __str__(self):
        return 'From %s'%(name)






    





    



