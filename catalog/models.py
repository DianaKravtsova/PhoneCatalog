from django.db import models

class Catalog(models.Model):
    Name = models.CharField(max_length=255)
    RegDate = models.DateTimeField(auto_now_add=True)
    Address = models.CharField(max_length=255)
    Phone = models.CharField(max_length=30)
    def __str__(self):
        return self.Name+"  "+self.Address + "  " +str(self.RegDate)+ "  "+self.Phone
# Create your models here.
