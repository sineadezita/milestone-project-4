# Atelier Zero One
A full stack editorial platform covering the intersection of technology and fashion across Europe. Built with Django, the platform allows visitors to browse articles freely, registered users to save articles and leave comments, and premium subscribers to unlock exclusive long-form content via a Stripe powered subscription.

---

## Table of Contents
- Project Purpose & Value
- Target Audience
- UX Design
- Features
- Apps & Structure
- Data Models & Schema
- Technologies Used
- Setup & Installation
- Environment Variables
- Stripe Integration
- Testing
- Deployment
- Credits & Attribution
- Future Features

## Project Purpose & Value

Atelier Zero One fills a gap in the European market for focused, professional reporting on technology as it applies to the fashion industry. Topics include AI-driven personalisation, wearable technology, sustainable supply chains, augmented reality retail, and digital fashion.

** Value to users:**
- Visitors can freely discover articles and assess whether the publication suits them
- Registered users get a personalised reading list they can engage via comments
- Premium subscribers unlock full access to in-depth reports and analysis

The purpose of the site is immediately evident on arrival: a clean editorial homepage communicates the publication's direction and focus, and the premium content lock clearly signals why registration and subscription add value.

---

## Target Audience

| Audience | Need |
|----------|------|
| Fashion industry professionals | Stay current on technology disrupting their sector|
| Tech professionals entering fashion | Understand the domain they are moving into |
| Students & Researchers | Access focused, reliable editorial content |
| Investors & analysts | Monitor trends in fashion technology across Europe |

---

## UX Design

### Design Principles

Atelier Zero One follows a minimal editorial aesthetic. The design priorities readability and content hierarchy over visual decoration, ensuring the purpose of the site is immediately clear to a new user.

Key UX decisions:

- **Information hierarchy**: Featured article leads the homepage, supported by category filtering, so users can orient themselves instantly
- **User Control:** Premium content is clearly signposted before a user reaches a paywall, so they are never surprised
- **Consistency:** The same card layout, typography, and spacing is used across all article listings
- **Feedback:** All user actions (login, save article, comment submit, subscription) produce clear success or error messages
- **Accessibility:** Semantic HTML, sufficient colour contrast and keyboard-navigable forms throughout

### User Stories

See User Stories for the full set of user stories used to plan this project.

> **Distinction upgrade:** Wireframes and mockups to be added here.

---

## Features

### Implemented

- User registration and login (available to anonymous users only)
- Password reset via email
- Save and unsave articles to a personal reading list
- Leave, edit, and delete own comments on articles
- Premium content locked for non-subscribers with clear messaging
- Stripe Checkout subscription (test mode)
- Subscription success and cancellation
- Subscription status shown in user profile
- Reponsive layout using Bootstrap 5
- Custom 403 and 404 error pages
- Django admin panel for content management

### CRUD Summary

| Model | Create | Read | Update | Delete |
|-------|--------|------|--------|--------|
| Article | Admin Panel | All users | Admin Panel | Admin panel |
| Comment | Registered users | All users | Comment author | Comment author |
| User Profile | Auto on registration | Profile owner | Profile owner | - |
| Saved Article | Registered users | Profile owner | - |
| Subscription | Via Stripe checkout | Profile owner | Via Stripe webhook | Via cancellation |

--- 

## Apps & Structure 
| App | Purpose |
|-----|---------|
| 'home' | Homepage view and featured content |
| 'articles' | Articles and category models,  views and template |
| 'events' | Event models, views and templates |
| 'accounts | User profiles, reading list, saved events |
| 'subscriptions' | Stripe checkout, webhook, subscription model |
| 'comments' | Comment model, add/edit/delete views |
| 'audit_log' | Security logging for user actions |

## Data Models

Add ERD 

## Technologies Used
| Category | Technology |
|----------|------------|
| Backend framework | Django |
| Language | Python |
| Database | SQLite (development) / PostgreSQL (production) |
| Authentication | Django Allauth |
| Payments | Stripe Checkout + Webhooks |
| Frontend framework | Bootstrap 5 |
| JavaScript | Vanilla JS for flash message dismissal and delete confirmation |
| Image hosting | Cloudinary |
| Deployment | Heroku |
| Static files | Whitenoise |
| Version control | Git & GitHub |


---

## Setup & Installation

1. Clone the repository: 'git clone https://github.com/sineadezita/milestone-project-4'
2. Create a virtual environment: 'python -m venv .venv'
3. Activate it: 'source .venv/bin/activate'
4. Install dependencies: 'pip install -r requirements.txt'
5. Create 'env.py' in the root directory with the required environment variables (see below)
6. Run migrations: 'python3 manage.py migrate'
7. Create a superuser: 'python3 manage.py createsuperuser'
8. Run the server: 'python3 manage.py runserver'

## Environment Variables

Create an 'env.py' file in the root directory:
'''python
import os

os.environ['SECRET_KEY"] = 'your-secret-key'
os.environ['DEBUG"] = 'True'
os.environ['STRIPE_PUBLIC_KEY'] = 'your-strip-public-key'
os.environ['STRIPE_SECRET_KEY'] = 'your-stripe-secret-key'
os.environ['STRIPE_PRICE_ID'] = 'your-stripe-price-id'
os.environ['STRIPE_WEBHOOK_SECRET'] = 'your-stripe-webhook-secret'
os.environ['CLOUDINARY_CLOUD_NAME'] = 'your-cloud-name'
os.environ['CLOUDINARY_API_KEY'] = 'your-api-key'
os.environ['CLOUDINARY_API_SECRET'] = 'your-api-secret'

## Stripe Integration

This project uses **Stripe Checkout in test mode only**. No real payments are processed.

| Payment successful | /subscriptions/succes/ | Welcome to Premium |
| Payment cancelled | /subscriptions/cancel/ | Subscription cancelled |
| Already subscribed | /subscriptions/ | You are already a premium member |

### Subscription Flow

1. A logged-in user clicks **Go Premium**
2. They are re-directed to Stripe-hosted checkout
3. On success, Stripe fires a 'checkout.session.completed' webhook
4. The webhook handler sets the user's 'Subscription.status' to 'active'
5. The user is redirected to a success page confirming access is unlocked

### User Feedback

| Outcome | Page shown | Message |
|---------|------------|---------|
| Payment successful | '/subscriptions/success/' | Welcome to Atelier Zero One Premium! |
| Payment cancelled | '/subscriptions/cancel/' | Subscription cancelled. |
| Already subscribed | '/subscriptions/' | You are already a premium member |
| Checkout error | '/subscriptions/' | Something went wrong: [errir detail] |

### Stripe Test Card

```
Card number : 4242 4242 4242 4242
Expiry      : Any future date
CVC         : Any 3 digits
```

---

## Testing

Full testing documentation is in ADD FILE HERE.

## Deployment

This project is deployed to **Heroku** using the following steps:

1. Open Heroku website and create an account or login.
2. Create a new Heroku app
3. Add **Heroku Postgre** add-on (Essential-0)
4. Set all environment variables in Heroku Config Vars:
    - 'SECRET_KEY'
    - 'STRIPE_PUBLIC_KEY'
    - 'STRIPE_SECRET_KEY'
    - 'STRIPE_PRICE_ID'
    - 'STRIPE_WEBHOOK_SECRET'
    - 'CLOUDINARY_CLOUD_NAME'
    - 'CLOUDINARY_API_KEY'
    - 'CLOUDINARY_API_SECRET'
5. Create a 'Procfile': 'web: gunicorn atelier_01.wsgi:application'
6. Create 'runtime.txt': ''python-3.12.8'
7. Push to GitHub and deploy via Heroku dashboard
8. Run migrations: 'heroku run python manage.py migrate --app your-app-name'
9. Create superuser: 'heroku run python manage.py createsuperuser --app your-app-name'
10. Run collectstatic: 'heroku run python manage.py collectstatic --app your-app-name'

**Live URL:**
**GitHub:**


## Credit & Attribution

### Libraries & Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| Django | 6.0.2 | Core web framework |
| django-allauth | 65.14.3 | User authentication and registration |
| stripe | 14.4.0 | Payment processing and webhooks |
| cloudinary | 1.44.1 | Image hosting and delivery |
| django-cloudinary-storage | 0.3.0 | Cloudinary integration for Django |
| dj-databse-url | 3.1.2 | Database URL configuration for Heroku |
| psycopg2-binary | 2.9.11 | PostgreSQL database adapter |
| gunicorn | 25.1.0 | WSGI server for Heroku deployment |
| whitenoise | 6.12.0 | Static file serving in production |
| requests | 2.32.5 | HTTP library |
| asgiref | 3.11.1 | Django async support |
| sqlparse | 0.5.5 | SQL query formatting |


### Code Attribution

### Design Inspiration

---

## Future Features

| Feature | Description |
|---------|-------------|
| Category filtering | Filter articles by category on a list page |
| Search | Full text search across multiple articles |
| Author profiles | Public author pages with article history |
| Newsletter | Email newsletter for premium subscribers |
| Data journalism | Sentiment analysis features |



