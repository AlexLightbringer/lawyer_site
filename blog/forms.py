from django import forms

from .models import Post, Review, Appointment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["name", "phone", "content", "grade"]

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ["name", "phone", "email", "problem"]

