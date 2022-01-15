from django.db                  import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    
    def create_user(self, email, nickname, password):
        
        if not email:    
            raise ValueError('must have user email')
        
        if not nickname:    
            raise ValueError('must have user nickname')

        user = self.model(
                email       = self.normalize_email(email),
                nickname    = nickname
                )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staff(self, email, nickname, password):
        user = self.create_user(
                email,
                nickname = nickname,
                password = password
                )
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nickname, password):
        user = self.create_user(
                email,
                nickname = nickname,
                password = password
                )
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    
    email = models.CharField(
            verbose_name    = 'email',
            max_length      = 100,
            unique          = True
            )

    nickname = models.CharField(
            verbose_name    = 'nickname',
            max_length      = 10,
            unique          = True
            )

    is_active = models.BooleanField(
            verbose_name    = 'is_active',
            default         = True 
            )

    is_staff = models.BooleanField(
            verbose_name    = 'is_staff',
            default         = False
            )

    is_superuser = models.BooleanField(
            verbose_name    = 'is_superuser',
            default         = False
            )
    
    USERNAME_FIELD = 'email'

    objects = UserManager()

    class Meta:
        db_table = 'users'
