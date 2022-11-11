from django.db import models

# Create your models here.
class Employee(models.Model):
    eid=models.IntegerField()
    ename=models.CharField(max_length=20)
    eemail=models.EmailField(max_length=50)
    econtact=models.CharField(max_length=20)


    def __str__(self):
        return "%s" %(self.ename)

    class Meta:
        db_table='Employee'
