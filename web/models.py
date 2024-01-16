from django.db import models

# Create your models here.


class BlogDetail(models.Model):
  image = models.ImageField(upload_to='media')
  name = models.CharField(max_length=255)
  slug = models.SlugField(unique=True)
  date = models.DateField()
  content = models.TextField()

  def __str__(self):
      return self.name



class MenuCategory(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def get_products(self):
        return Menu.objects.filter(category=self)

    def __str__(self):
        return self.name


class Menu(models.Model):
    category = models.ForeignKey(
        "web.MenuCategory",
        verbose_name="menu Category",
        related_name="menu_category",
        on_delete=models.CASCADE,
    )
    image = models.ImageField(
        upload_to="media/", help_text="supporting fale....", blank=True, null=True
    )
    name = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
       return self.name
    

class Testimonial(models.Model):
   image = models.ImageField(upload_to='media')
   name = models.CharField(max_length=255)
   content = models.CharField(max_length=255)

   def __str__(self):
       return self.name
   

class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=120, blank=True, null=True)
    subject = models.CharField(max_length=120, blank=True, null=True)
    message = models.TextField()

    def __str__(self):
        return str(self.name)