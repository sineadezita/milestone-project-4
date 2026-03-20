# Testing

## Manual Testing

### Navigation
| Feature | Expected | Result | Pass/Fail |
|---------|----------|--------|-----------|
| Logo Click | Returns to homepage |
| Articles link | Opens article list |
| Events link | Opens events list |
| Go Premium link | Opens subscription page |
| Footer social links | Opens social placeholders|

### Authentication
| Feature | Expected | Result | Pass/Fail |
|---------|----------|--------|-----------|
| Register new account | Creates account and logs in | Works as expected | Pass |
| Login with correct credentials | Logs user in | Works as expected | Pass |
| Login with wrong credentials | Shows error message |  Works as expected | Pass |
| Logout | Logs user out and redirects | Works as expected | Pass |

### Article
| Feature | Expected | Result | Pass/Fail |
|---------|----------|--------|-----------|
| View article list | Show all published articles | Works as expected | Pass |
| Click article | Opens article detail | Works as expected | Pass |
| Premium article logged out | Shows lock message | Works as expected | Pass |
| Premium article logged in no subscription | Shows lock message | Works as expected | Pass |
| Premium article with actice subscription | Shows full content | Works as expected | Pass |
| Save article | Adds to reading list | Works as expected | Pass |
|Unsave article | Removes from reading list | Works as expected | Pass |

### Comments
| Feature | Expected | Result | Pass/Fail |
| Submit comment | Shows awaiting approval comment |
| Edit own comment | Updates comment |
| Delete own comment | Shows confirmation then deletes |

### Events
| Feature | Expected | Result | Pass/Fail |
|---------|----------|--------|-----------|
| View event list| Shows all published events |
| Click event | Opens event details |
| Save event | Adds to saved events|

### Subscriptions & Payments 
| Feature | Expected | Result | Pass/Fail |
|---------|----------|--------|-----------|
| Click Go Premium | Redirects to Stripe checkout |
| Complete payment with test card | Creates subscription |
| Success page shown after payment | Displays welcome message |
| Prmeium content accessible after payment | Full article shown |

### User Profile
| Feature | Expected | Result | Pass/Fail |
|---------|----------|--------|-----------|
| View profile | Shows user details |
| View reading list | Shows saved articles |
| View saved events | Shows saved events |

## Browser Compatibility
| Broweser | Result |
|----------|--------|
| Chrome |
| Firefix |
| Safari |
| Edge |

## Responsive Design
| Device | Result |
|--------|--------|
| Desktop |
| Tablet |
| Mobile |

## Validator Testing
- HTML: To be completed
- CSS: To be completed
- Python (PEP8): To be completed
- JS: To be completed

## Known Bugs
- events.css returns 404 on Heroku - events page still displays correctly using base.css
- Webhook requires exact matching Stripe API keys to function correctly