from django.db import models
from accounts.models import Accounts


class Company(models.Model):
    comp_name = models.CharField(max_length=100)
    comp_logo = models.ImageField(upload_to='company_logos/', blank=True, null=True,
                                  default='default_images/user.png'
                                  )

    class Meta:
        db_table = 'Company'

    def __str__(self):
        return self.comp_name


class Cars(models.Model):
    owner = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    model = models.CharField(max_length=100)
    milage = models.IntegerField()
    year_manufactured = models.IntegerField()
    about = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to='product_images', blank=True, null=True,
                              default='/default_images/car.png')

    class Meta:
        db_table = 'Cars'

    def __str__(self):
        return self.model


class Comments(models.Model):
    user = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    car = models.ForeignKey(Cars, on_delete=models.CASCADE)
    comment = models.TextField()

    class Meta:
        db_table = 'Comments'

    def __str__(self):
        return f"{self.user.username} {self.car.model}"
