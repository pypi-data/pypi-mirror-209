# Features

Features:

- Products
  - products (multiple images + main image, title, description, etc.)
  - products categories (parent/child categories)
  - product dynamic stats
  - product comments
  - search for products/categories
  - filter for products in the category
- Customers
  - wish lists
  - cart
  - compare lists
  - bonuses wallet
  - customer support request
- Settings
  - taxes
  - currencies
- Orders
  - orders
  - order reports (view and generation of pdf)
  - shipping
  - statuses of order / payment / shipment

## Installation

- Install library

```bash
pip install drf-shop-api
```

- Add to installed apps

  ```python

  INSTALLED_APPS = [
    ...
    'drf_shop_api'
  ]
  ```

- Add api path to you root urls.py

```python
   urlpatterns = [
    ...
    path("shop/", include("drf_shop_api.urls")),
]
```

- Use `create_shop_profile` decorator on create_user method of your UserManager

```python
from django.contrib.auth.base_user import BaseUserManager

from drf_shop_api.decorators import create_shop_profile


class UserManager(BaseUserManager):
    @create_shop_profile
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Enter the email")
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user
```

- Setup `AUTH_USER_MODEL` in settings.py

- Run `python manage.py makemigrations` and `python manage.py migrate` (Due to optional Payment model from root project)
- Optional settings:
  - `DRF_SHOP_PAGE_SIZE` on will be default 10
  - `DRF_SHOP_PAYMENT_MODEL` = "projects.payments.models.Payment"
  - `DRF_SHOP_PAYMENT_STATUS_CHOICES` = "project.payments.choices.PaymentStatus"
  - `DRF_SHOP_BONUS_RATE` = percentage value for each order that will go to bonus wallet

## Dependencies

    django
    drf
    drf-yasg 1.21.5
    rest_framework_simplejwt
    mixer
    django-filter

### TODO

- Add DB indexes
- Task for currency rate update
- Review permissions
