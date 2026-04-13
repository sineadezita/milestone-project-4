# Testing

## Manual Testing

### Navigation
| Feature | Expected | Result | Pass/Fail |
|---------|----------|--------|-----------|
| Logo Click | Returns to homepage | Works as expected | Pass |
| Articles link | Opens article list | Works as expected | Pass |
| Events link | Opens events list | Works as expected | Pass |
| Go Premium link | Opens subscription page | Works as expected | Pass |
| Footer social links | Opens social placeholders | Works as expected | Pass |

### Authentication
| Feature | Expected | Result | Pass/Fail |
|---------|----------|--------|-----------|
| Register new account | Creates account and logs in | Works as expected | Pass |
| Login with correct credentials | Logs user in | Works as expected | Pass |
| Login with wrong credentials | Shows error message | Works as expected | Pass |
| Logout | Logs user out and redirects | Works as expected | Pass |

### Articles
| Feature | Expected | Result | Pass/Fail |
|---------|----------|--------|-----------|
| View article list | Shows all published articles | Works as expected | Pass |
| Click article | Opens article detail | Works as expected | Pass |
| Premium article logged out | Shows lock message | Works as expected | Pass |
| Premium article logged in no subscription | Shows lock message | Works as expected | Pass |
| Premium article with active subscription | Shows full content | Works as expected | Pass |
| Save article | Adds to reading list | Works as expected | Pass |
| Unsave article | Removes from reading list | Works as expected | Pass |

### Comments
| Feature | Expected | Result | Pass/Fail |
|---------|----------|--------|-----------|
| Submit comment | Shows awaiting approval message | Works as expected | Pass |
| Edit own comment | Updates comment | Works as expected | Pass |
| Delete own comment | Shows confirmation then deletes | Works as expected | Pass |

### Events
| Feature | Expected | Result | Pass/Fail |
|---------|----------|--------|-----------|
| View event list | Shows all published events | Works as expected | Pass |
| Click event | Opens event details | Works as expected | Pass |
| Save event | Adds to saved events | Works as expected | Pass |
| Unsave event | Removes from saved events | Works as expected | Pass |

### Subscriptions & Payments
| Feature | Expected | Result | Pass/Fail |
|---------|----------|--------|-----------|
| Click Go Premium | Redirects to Stripe checkout | Works as expected | Pass |
| Complete payment with test card | Creates subscription | Works as expected | Pass |
| Success page shown after payment | Displays welcome message | Works as expected | Pass |
| Premium content accessible after payment | Full article shown | Works as expected | Pass |

### User Profile
| Feature | Expected | Result | Pass/Fail |
|---------|----------|--------|-----------|
| View profile | Shows user details | Works as expected | Pass |
| Subscription status shown | Shows Premium or Free | Works as expected | Pass |
| View reading list | Shows saved articles | Works as expected | Pass |
| View saved events | Shows saved events | Works as expected | Pass |

### Test Card Details
Card number : 4242 4242 4242 4242
Expiry      : Any future date (e.g. 12/29)
CVC         : Any 3 digits (e.g. 123)
Name        : Any name

---

## Browser Compatibility
| Browser | Result |
|---------|--------|
| Chrome | Pass |
| Firefox | Pass |
| Safari | Pass |

---

## Responsive Design
| Device | Result |
|--------|--------|
| Desktop | Pass |
| Tablet | Pass |
| Mobile | Pass |

---

## Validator Testing

### HTML Validation
All pages were validated using the [W3C HTML Validator](https://validator.w3.org/) by viewing page source on the live Heroku site and pasting into the validator.

**Homepage**
![Homepage before](docs/testing/homepage_before.png)
![Homepage after](docs/testing/homepage_after.png)

**Articles List**
![Articles](docs/testing/articles.png)

**Events**
![Events](docs/testing/events.png)

**About**
![About](docs/testing/about.png)

**Login**
![Login](docs/testing/login.png)

**Logout**
![Logout](docs/testing/logout.png)

**Register**
![Register before](docs/testing/register_before.png)
![Register after allauth errors noted](docs/testing/register_after_allauth_errors.png)

**Profile**
![Profile](docs/testing/profile.png)

**Reading List**
![Reading List](docs/testing/reading_list.png)

**Saved Events**
![Saved Events](docs/testing/saved_events.png)

**Subscription Page**
![Subscription](docs/testing/subscription.png)

---

### CSS Validation
All CSS files were validated using the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/). One error was found in accounts.css and fixed.

**base.css**
![base.css](docs/testing/base_css.png)

**home.css**
![home.css](docs/testing/home_css.png)

**articles.css**
![articles.css](docs/testing/articles_css.png)

**accounts.css**
One error was found — `font-size: 300` was missing a unit. Fixed to `font-size: 28px`.

Before fix:
![accounts.css before](docs/testing/accounts_css_before.png)

After fix:
![accounts.css after](docs/testing/accounts_css_after.png)

**subscriptions.css**
![subscriptions.css](docs/testing/subscription_css.png)

---

### JavaScript (JSHint)
JavaScript was validated using [JSHint](https://jshint.com/).

A `/* jshint esversion: 6 */` comment was added to the top of the file to indicate ES6 syntax is in use.

**Before adding esversion comment:**
![JS before](docs/testing/js_before.png)

**After adding esversion comment:**
![JS after](docs/testing/js_after.png)

---

### Python (PEP8)
All Python files were validated using [CI Python Linter](https://pep8ci.herokuapp.com/). All files returned no errors.

**accounts**
![accounts/admin.py](docs/testing/accounts_admin.png)
![accounts/apps.py](docs/testing/accounts_apps.png)
![accounts/models.py](docs/testing/accounts_models.png)
![accounts/urls.py](docs/testing/accounts_urls.png)
![accounts/views.py](docs/testing/accounts_views.png)

**articles**
![articles/admin.py](docs/testing/articles_admin.png)
![articles/apps.py](docs/testing/articles_apps.png)
![articles/models.py](docs/testing/articles_models.png)
![articles/urls.py](docs/testing/articles_urls.png)
![articles/views.py](docs/testing/articles_views.png)

**audit_log**
![audit_log/admin.py](docs/testing/audit_log_admin.png)
![audit_log/apps.py](docs/testing/audit_log_apps.png)
![audit_log/models.py](docs/testing/audit_log_models.png)
![audit_log/signals.py](docs/testing/audit_log_signals.png)
![audit_log/utils.py](docs/testing/audit_log_utils.png)

**comments**
![comments/admin.py](docs/testing/comments_admin.png)
![comments/apps.py](docs/testing/comments_apps.png)
![comments/models.py](docs/testing/comments_models.png)
![comments/urls.py](docs/testing/comments_urls.png)
![comments/views.py](docs/testing/comments_views.png)

**events**
![events/admin.py](docs/testing/events_admin.png)
![events/apps.py](docs/testing/events_apps.png)
![events/models.py](docs/testing/events_models.png)
![events/urls.py](docs/testing/events_urls.png)
![events/views.py](docs/testing/events_views.png)

**home**
![home/apps.py](docs/testing/home_apps.png)
![home/urls.py](docs/testing/home_urls.png)
![home/views.py](docs/testing/home_views.png)

**subscriptions**
![subscriptions/admin.py](docs/testing/subscriptions_admin.png)
![subscriptions/apps.py](docs/testing/subscriptions_apps.png)
![subscriptions/models.py](docs/testing/subscriptions_models.png)
![subscriptions/urls.py](docs/testing/subscriptions_urls.png)
![subscriptions/views.py](docs/testing/subscriptions_views.png)

**atelier_01**
![settings.py](docs/testing/atelier01_settings.png)
![wsgi.py](docs/testing/atelier01_wsgi.png)
![asgi.py](docs/testing/atelier01_asgi.png)

---

## Lighthouse Testing

![Lighthouse Results](docs/testing/lighthouse.png)

| Page | Performance | Accessibility | Best Practices | SEO |
|------|-------------|---------------|----------------|-----|
| Homepage | See screenshot | 96 | 58 | 100 |


---

## Known Bugs
- Register page has minor HTML validation errors caused by Django Allauth's built-in form rendering (`{{ form.as_p }}`). These are generated by the third-party library and are outside the project's control.
- Login/logout pages use default allauth styling — custom templates planned as a future feature.
- Search bar currently searches articles only, not events.