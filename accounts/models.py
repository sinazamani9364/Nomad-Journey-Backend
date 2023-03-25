from django.db import models
from django.contrib.auth.models import AbstractUser , BaseUserManager
# Create your models here.

class UserManager(BaseUserManager):
    use_in_migrations = True
    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff' , True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),)
    User_birthdate = models.DateField(null=True)
    User_about_me = models.TextField(null=True)
    User_job = models.CharField(max_length=100 , null=True)
    User_education = models.CharField(max_length=100,null=True)
    User_nationality = models.CharField(max_length=100, null=True)
    User_address = models.TextField(blank=True , null=True)
    User_address_lat = models.FloatField(null=True)
    User_address_long = models.FloatField(null = True)
    User_gender = models.CharField(max_length=1, choices=GENDER_CHOICES , null=True)
    User_country_code = models.CharField(max_length=2 , null=True)
    User_country = models.CharField(max_length=100 , null=True)
    User_city = models.CharField(max_length=100 , null=True)
    User_postal_code = models.CharField(max_length=10 , null=True)
    User_phone_number = models.CharField(max_length=20 , null=True)
    # is_active = models.BooleanField(default=True)
    profile_photo = models.ImageField(upload_to='customer_photos' , null=True)
    image_code = models.TextField(null=True, blank=True)
    ssn = models.CharField(max_length=20 , null=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255 , unique=True)
    password = models.CharField(max_length=255)
    password_again = models.CharField(max_length=255)
    username = models.CharField(max_length=255 , unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.first_name+" "+self.last_name
    
class City(models.Model):
    city_name = models.CharField(max_length=100, primary_key=True)
    country = models.CharField(max_length=100)
    c_lat = models.FloatField()
    c_long = models.FloatField()
    abbrev_city = models.CharField(max_length=3)

    def __str__(self):
        return f"{self.cityName}: ({self.cLat}, {self.cLong})"
