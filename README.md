# Legal Agency

This Django project implements a site for a legal agency. It allows users to view blog posts, create new posts, read reviews, and schedule appointments. The blog also includes user registration and login functionality.

## Table of Contents

- [Project Structure](#project-structure)
- [Models](#models)
- [Forms](#forms)
- [Views](#views)
- [URLs](#urls)
- [Installation](#installation)
- [Usage](#usage)

## Project Structure

The project's main components are organized as follows:

- `blog` app: Contains models, forms, views, and templates for the blog functionality.
- `users` app: Handles user registration and authentication.
- Templates: HTML templates for rendering pages.
- Static Files: CSS, JavaScript, and image files.

## Models

### Post

- `title`: The title of the blog post.
- `content`: The content of the blog post.
- `publish`: A boolean field indicating whether the post is published.
- `date_added`: The date and time when the post was created.

### Review

- `name`: The name of the reviewer.
- `phone`: The phone number of the reviewer.
- `content`: The content of the review.
- `publish`: A boolean field indicating whether the review is published.
- `date_added`: The date and time when the review was created.
- `grade`: The grade or rating given by the reviewer.

### Appointment

- `name`: The name of the person scheduling the appointment.
- `phone`: The phone number of the person scheduling the appointment.
- `email`: The email address of the person scheduling the appointment.
- `problem`: A description of the problem or reason for the appointment.

## Forms

- `PostForm`: Form for creating and editing blog posts.
- `ReviewForm`: Form for creating and editing reviews.
- `AppointmentForm`: Form for scheduling appointments.

## Views

The project includes views for the following functionality:

- Home view
- Prices view
- List reviews view
- Create review view
- Posts view
- New post view
- Appointment view
- User registration and authentication views

## URLs

The project defines URL patterns for routing requests to the appropriate views.


## Installation

1. Clone this repository to your local machine.
2. Create a virtual environment: `python -m venv venv`.
3. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS and Linux: `source venv/bin/activate`
4. Install the required packages: `pip install -r requirements.txt`.
5. Run migrations: `python manage.py migrate`.

## Usage

1. Start the development server: `python manage.py runserver`.
2. Access the application in your web browser at `http://localhost:8000`.
