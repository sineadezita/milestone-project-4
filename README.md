# Atelier Zero One
A full stack editorial platform covering the intersection of technology and fashion across Europe. Built with Django, the platform allows visitors to browse articles freely, registered users to save articles and leave comments, and premium subscribers to unlock exclusive long-form content via a Stripe powered subscription.

---

## Table of Contentss
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

Atelier Zero One fills a gap in the European market for focused, professional reposrting on technology as it applies to the fashion industry. Topics include AI-driven personalisations, wearable technology, sustainable supply chains, augmented reality retain, and digital fashion.

** Value to users:**
- Visitors can freely discover articles and assess whether the publication suits them
- Registered users get a personalised reading list they can engage via comments
- Premium subscribers unlock full access to in-depth reports and analysis

The purpose of the site is immediately evident on arrival: a clean editorial homepage communicates the publication'tration and focus, and the premium content lock clearly signals why registration and subscription add value.

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

## Data Models

Add ERD 

## Technologies Used
| Category | Technology |
|----------|------------|
| Backend framework | Django |
| Language | Python |
| Database | To be updated |
| Authentication | Django Allauth |
| Payments | Stripe Checkout + Webhooks |
| Frontend framework | Bootstrap 5 |
| JavaScript | To be updated |
| Image hosting | Cloudinary |
| Deployment | Heroku |
| Static files | Whitenoise |
| Version control | Git & GitHub |

---

## Setup & Installation

## Stripe Integration

This project uses **Stripe Checkout in test mode only**. No real payments are processed.

### Subscription Flow

1. A logged-in user clicks **Go Premium**
2. They are re-directed to Stripe-hosted checkout
3. On success, Stripe fires a 'checkout.session.completed' webhook
4. The webhook handler sets the user's 'Subscription.status' to 'active'
5. The user is redirected to a success page confirming access is unlocked

### User Feedback

| Outcome | Page shown | Message |
|---------|------------|---------|
| Payment successful | 

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

Deployed to **Heroku**.

## Credit & Attribution

### Libraries & Dependencies

### Code Attribution

### Design Inspiration

---

## Future Features

| Feature | Description |
|---------|-------------|



