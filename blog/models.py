from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib import auth
from django.utils.text import slugify
from datetime import datetime, date
from ckeditor.fields import RichTextField


# Create your models here.
class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,
                            null=False,
                            unique=False)
    text = RichTextField(blank=True, null=True)
    # text = models.TextField()
    publication_date = models.DateField(verbose_name='date published',
                                        auto_now_add=True)
    tag = models.CharField(max_length=255, default="coding")
    snippet = models.CharField(max_length=255)
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def totalLikes(self):
        return self.likes.count()

    def __str__(self):
        return f"{self.title} by {str(self.author)}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_update_url(self):
        return reverse('blog_post_update',
                       kwargs={'slug': self.slug})

    def get_absolute_url(self):
        # return reverse('home') - Returns to the homepage
        return reverse('blog-detail', args=[str(self.id)])


class Tag(models.Model):
    tag_name = models.CharField(max_length=255)

    def __str__(self):
        return self.tag_name

    def get_absolute_url(self):
        return reverse('home')
