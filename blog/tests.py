import pytest
from django.urls import reverse
from django.contrib.messages import get_messages
from blog.models import Review, Post
from blog.forms import ReviewForm, PostForm, AppointmentForm
from django.contrib.auth.models import User

@pytest.fixture
def user():
    return User.objects.create_user(username='testuser', password='testpassword')

@pytest.fixture
def client_logged_in(client, user):
    client.login(username='testuser', password='testpassword')
    return client

@pytest.fixture
def review_data():
    return {'title': 'Test Review', 'content': 'This is a test review', 'publish': True}

@pytest.fixture
def post_data():
    return {'title': 'Test Post', 'content': 'This is a test post', 'publish': True}

@pytest.fixture
def appointment_data():
    return {'name': 'John Doe', 'email': 'johndoe@example.com', 'message': 'Test message'}

def test_home_view(client):
    url = reverse('home')
    response = client.get(url)
    assert response.status_code == 200

def test_prices_view(client):
    url = reverse('prices')
    response = client.get(url)
    assert response.status_code == 200

def test_list_reviews_view(client):
    url = reverse('list_reviews')
    response = client.get(url)
    assert response.status_code == 200

def test_create_review_view(client_logged_in, review_data):
    url = reverse('create_review')
    response = client_logged_in.post(url, review_data, follow=True)
    assert response.status_code == 200
    messages = list(get_messages(response.wsgi_request))
    assert len(messages) == 1
    assert str(messages[0]) == "Your review has been added!"

def test_posts_view(client):
    url = reverse('posts')
    response = client.get(url)
    assert response.status_code == 200

def test_new_post_view(client_logged_in, post_data):
    url = reverse('new_post')
    response = client_logged_in.post(url, post_data, follow=True)
    assert response.status_code == 200

def test_appointment_view(client_logged_in, appointment_data):
    url = reverse('appointment')
    response = client_logged_in.post(url, appointment_data, follow=True)
    assert response.status_code == 200
    messages = list(get_messages(response.wsgi_request))
    assert len(messages) == 1
    assert str(messages[0]) == "Your request for consultation has been accepted! We will contact you soon!"