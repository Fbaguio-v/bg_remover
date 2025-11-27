from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to='mysite_images/', null=True, blank=True)

    def __str__(self):
        return f'Process image {self.id}'
        
    def get_image_url(self):
        if self.image and hasattr(self.image, 'url'):
            url = self.image.url
            return url