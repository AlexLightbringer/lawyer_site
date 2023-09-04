from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Post, Review, Appointment
from .forms import PostForm, ReviewForm, AppointmentForm


def home(request):
    print(request)
    return render(request, "blog/home.html")


def prices(request):
    print(request)
    return render(request, "blog/prices.html")

def list_reviews(request):
    reviews = Review.objects.filter(publish=True)
    context = {"reviews": reviews}
    return render(request, "blog/reviews.html", context=context)


def create_review(request):
    if request.method != 'POST':
        form = ReviewForm()
    else:
        print(request.POST)
        form = ReviewForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your review has been added!")
            return redirect('/reviews')
    context = {"form": form}
    return render(request, "blog/create_review.html", context=context)


def posts(request):
    posts = Post.objects.filter(publish=True)
    context = {"posts": posts}
    return render(request, "blog/blog.html", context=context)

def detail_page(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'blog/detail.html', {'post': post})

def new_post(request):
    if request.method != 'POST':
        form = PostForm()
    else:
        form = PostForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/blog')
    context = {"form": form}
    return render(request, "blog/new_post.html", context=context)


def appointment(request):
    if request.method != 'POST':
        form = AppointmentForm()
    else:
        form = AppointmentForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your request for consultation has been accepted! We will contact you soon!")
            return redirect('/')
    context = {"form": form}
    return render(request, "blog/appointment.html", context=context)
