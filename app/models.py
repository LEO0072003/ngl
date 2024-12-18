from django.db import models

# Create your models here.

class App(models.Model):
    """Model to store all the apps"""
    pic = models.ImageField(upload_to='app/', default='app/default.png')
    app_name = models.CharField(max_length=20)
    app_link = models.URLField()
    sub_category = models.ForeignKey("SubCategory", related_name="apps", on_delete=models.PROTECT)
    points = models.IntegerField(default = 100)


class Category(models.Model):
    """Model to store all the app categories"""
    category_name = models.CharField(max_length=20)

    def __str__(self):
        return self.category_name

class SubCategory(models.Model):
    """Model to store all the app sub-categories"""
    sub_category_name = models.CharField(max_length=20)
    category = models.ForeignKey(Category, related_name="sub_category", on_delete=models.PROTECT)

    def __str__(self):
        return self.category.category_name + "   |  "+ self.sub_category_name
