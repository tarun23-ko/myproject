from django.db import models

# Create your models here.
class post(models.Model):
    post_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=250)
    Head0 = models.CharField(max_length=250,)
    contentHead0 = models.CharField(max_length=250,default="")
    Head1 = models.CharField(max_length=250)
    contentHead1 = models.CharField(max_length=250,default="")
    Head2 = models.CharField(max_length=250)
    contentHead2 = models.CharField(max_length=250,default="")
    pub_date=models.DateField()
    image=models.ImageField(upload_to="Ecartblog/image",default="")
    def __str__(self):
        return self.title

