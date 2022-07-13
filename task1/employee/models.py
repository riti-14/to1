from django.db import models



# Create your models here.

class empregister_model(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=20)
    confirm_password=models.CharField(max_length=20)


class empleave_model(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    from1=models.DateField()
    to1=models.DateField()
    day=models.CharField(max_length=1,
        choices=(
            ('H','Half day') ,
            ('F','Full day'),
            )
            )

    reason=models.TextField()  

    def __str__(self):
        return self.name



class status_model(models.Model):
    status=models.CharField(max_length=30)







