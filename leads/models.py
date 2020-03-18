from django.db import models

# Create your models here.


class LeadSolution(models.Model):
    location_enum = ((0, 'Country'), (1, 'City'), (2, 'Zip'))
    first_name=models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    mobile = models.IntegerField(unique=True)
    email = models.CharField(max_length=50,unique=True)
    location_type = models.PositiveIntegerField(default=1,choices=location_enum)
    location_string=models.CharField(max_length=20)

    class Meta:
        managed = True

    def __str__(self):
        return str(self.id)


