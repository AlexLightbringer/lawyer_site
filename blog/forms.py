from django import forms

from .models import Post, Review, Appointment, BlogComment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]

class CommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ["comment",]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["name", "phone", "content", "grade"]

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ["name", "phone", "email", "problem"]