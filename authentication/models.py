import jwt

from datetime import datetime, timedelta

from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)

from django.db import models
from enumchoicefield import ChoiceEnum, EnumChoiceField


class UserManager(BaseUserManager):
    def create_user(self, login, password, name, surname, patronymic=None, photo=None,
                    faculty=None, course=None, group=None, email=None, telegram=None,
                    role=None, is_active=True):
        if login is None:
            raise TypeError('Users must have a login.')
        if name is None:
            raise TypeError('Users must have a name.')
        if surname is None:
            raise TypeError('Users must have a surname.')
        if password is None:
            raise TypeError('Users must have a password.')

        user = self.model(login=login, name=name, surname=surname,
                          patronymic=patronymic, photo=photo, course=course,
                          group=group, faculty=faculty, telegram=telegram,
                          role=role, is_active=is_active, password=password,
                          email=email, role_id=None if role is None else role.id)

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, login, password):
        user = self.model(login=login)
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class Faculties(ChoiceEnum):
    bio = "Биологический факультет"
    war = "Военный факультет"
    geo = "Факультет географии и геоинформатики"
    journ = "Факультет журналистики"
    hist = "Исторический факультет"
    mech = "Механико-математический факультет"
    famcs = "Факультет прикладной математики и информатики"
    raf = "Факульет радиофизики и компьютерных технологий"
    soc_comm = "Факультет социокультурных коммуникаций"
    fil_soc = "Факультет философии и социальных наук"
    fiz = "Физический факультет"
    fil = "Филологический факультет"
    chem = "Химический факультет"
    econ = "Экономический факультет"
    law = "Юридический факультет"
    rel = "Факультет международных отношений"

    buis = "Институт бизнеса"
    eco = "Экологический институт"
    teo = "Институт теологии"
    chin = "Институт китаеведения"
    lyc = "Лицей БГУ"
    col = "Юридичекий колледж БГУ"


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=100, null=False, blank=False)
    surname = models.CharField(max_length=100, null=False, blank=False)
    patronymic = models.CharField(max_length=100, null=True, blank=True)
    photo = models.CharField(max_length=200, null=True, blank=True)
    faculty = EnumChoiceField(enum_class=Faculties, default=Faculties.famcs, null=True, blank=True)
    course = models.IntegerField(default=1, null=True, blank=True)
    group = models.IntegerField(default=1, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    telegram = models.CharField(max_length=100, null=True, blank=True)
    login = models.CharField(max_length=100, null=False, blank=False, unique=True)
    password = models.CharField(max_length=100, null=False, blank=False)
    role = models.ForeignKey(
        "Role",
        on_delete=models.SET_NULL,
        related_name="roles",
        null=True
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = ['password']

    def __str__(self):
        return self.name

    @property
    def token(self):
        return self._generate_jwt_token()

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_short_name(self):
        return self.name

    def _generate_jwt_token(self):
        dt = datetime.utcnow() + timedelta(days=1)

        token = jwt.encode({
            'id': self.pk,
            'exp': dt
        }, settings.SECRET_KEY, algorithm='HS256')

        return token


class Role(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    permissions = models.JSONField(null=False, blank=False)

    def __str__(self):
        return self.name
