from django.db import models
from ckeditor.fields import  RichTextField
# Create your models here.

# Create your models here.
class Complaint(models.Model):
    author  = models.ForeignKey("auth.User",on_delete= models.CASCADE,verbose_name="YAZAR")
    title = models.CharField(max_length=100,verbose_name="BAŞLIK")
    content = RichTextField(verbose_name="ŞİKAYET & ÖNERİ")
    created_date = models.DateTimeField(auto_now_add= True,verbose_name="OLUŞTURMA TARİHİ")

    def __str__ (self):
        return self.title