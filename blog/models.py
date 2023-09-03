from django.db import models


class Post(models.Model):
    title = models.CharField(verbose_name="Title", max_length=200, blank=False)
    content = models.TextField(verbose_name="Content", blank=False)
    publish = models.BooleanField(verbose_name="Status", default=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    

class Review(models.Model):
    name = models.CharField(max_length=50, verbose_name="Name", blank=False)
    phone = models.CharField(max_length=10, verbose_name="Phone number", blank=False)
    content = models.TextField(max_length=3000, verbose_name="Review text", blank=False)
    publish = models.BooleanField(verbose_name="Status", default=False)
    date_added = models.DateTimeField(auto_now_add=True)
    grade = models.IntegerField(verbose_name="Grade", default=5, blank=False)

    def __str__(self) -> str:
        return f"{self.grade}"

class Appointment(models.Model):
    name = models.CharField(max_length=50, verbose_name="Name", blank=False)
    phone = models.CharField(max_length=10, verbose_name="Phone number", blank=False)
    email = models.TextField(max_length=50, verbose_name="Email address", blank=False)
    problem = models.TextField(max_length=3000, verbose_name="Problem text", blank=False)


    def __str__(self) -> str:
        return self.problem