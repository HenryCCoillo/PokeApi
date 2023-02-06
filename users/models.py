from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)

        user.set_password(password)

        user.save()

        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("El superusuario necesita que is_staff sea verdadero")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("El superusuario necesita que is_superuser sea verdadero")

        return self.create_user(email=email, password=password, **extra_fields)


class User(AbstractUser):
    email = models.CharField(max_length=80, unique=True, default="no@email.com")
    username = models.CharField(max_length=45)
    date_of_birth = models.DateField(null=True)

    objects = CustomUserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email

class Servicio(models.Model):
    servicio = models.CharField(max_length=30)
    mondo = models.FloatField()

    def __str__(self):
        return self.servicio


class Pago(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    # servicio_pago = models.ForeignKey(Servicio,on_delete=models.RESTRICT)
    servicio_pago = models.CharField(max_length=30)
    fecha_pago = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user