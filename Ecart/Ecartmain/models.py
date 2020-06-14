from django.db import models

# Create your models here.

class product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=220)
    category=models.CharField(max_length=50,default="")
    Sub_category=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    image=models.ImageField(upload_to="Ecartmain/image",default="")
    product_desc=models.CharField(max_length=500,default="")

    pub_date=models.DateField()
    def __str__(self):
        return self.product_name
class KHOBOR(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=40)
    phone=models.CharField(max_length=60)
    Eid=models.CharField(max_length=50)
    query=models.CharField(max_length=3000)

    def __str__(self):
        return self.name

class orders(models.Model):
    order_id=models.AutoField(primary_key=True)
    item_json=models.CharField(max_length=65000,default='')
    name=models.CharField(max_length=90)
    email=models.CharField(max_length=111)
    Address=models.TextField(max_length=500)
    city=models.CharField(max_length=50)
    Zipcode=models.CharField(max_length=5000)
    state=models.CharField(max_length=5000)
    phone = models.CharField(max_length=60,default=0)

    def __str__(self):
       return "Orders from------>" +"  "+self.name


class orderupdate(models.Model):
    update_id=models.AutoField(primary_key=True)
    order_id=models.IntegerField(default="")
    update_desc=models.CharField(max_length=5000)
    timestamp=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7]+"...."

