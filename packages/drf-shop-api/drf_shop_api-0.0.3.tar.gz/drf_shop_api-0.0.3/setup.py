# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['drf_shop_api',
 'drf_shop_api.customers',
 'drf_shop_api.migrations',
 'drf_shop_api.orders',
 'drf_shop_api.products']

package_data = \
{'': ['*']}

install_requires = \
['Django>=4.2.1,<5.0.0',
 'django-filter>=23.2,<24.0',
 'djangorestframework>=3.14.0,<4.0.0',
 'drf-yasg>=1.21.5,<2.0.0',
 'rest-framework-simplejwt>=0.0.2,<0.0.3']

setup_kwargs = {
    'name': 'drf-shop-api',
    'version': '0.0.3',
    'description': 'Standalone shop app, that you can add to your project',
    'long_description': '# Features\n\nFeatures:\n\n- Products\n  - products (multiple images + main image, title, description, etc.)\n  - products categories (parent/child categories)\n  - product dynamic stats\n  - product comments\n  - search for products/categories\n  - filter for products in the category\n- Customers\n  - wish lists\n  - cart\n  - compare lists\n  - bonuses wallet\n  - customer support request\n- Settings\n  - taxes\n  - currencies\n- Orders\n  - orders\n  - order reports (view and generation of pdf)\n  - shipping\n  - statuses of order / payment / shipment\n\n## Installation\n\n- Install library\n\n```bash\npip install drf-shop-api\n```\n\n- Add to installed apps\n\n  ```python\n\n  INSTALLED_APPS = [\n    ...\n    \'drf_shop_api\'\n  ]\n  ```\n\n- Add api path to you root urls.py\n\n```python\n   urlpatterns = [\n    ...\n    path("shop/", include("drf_shop_api.urls")),\n]\n```\n\n- Use `create_shop_profile` decorator on create_user method of your UserManager\n\n```python\nfrom django.contrib.auth.base_user import BaseUserManager\n\nfrom drf_shop_api.decorators import create_shop_profile\n\n\nclass UserManager(BaseUserManager):\n    @create_shop_profile\n    def create_user(self, email, password=None):\n        if not email:\n            raise ValueError("Enter the email")\n        user = self.model(email=self.normalize_email(email))\n        user.set_password(password)\n        user.save(using=self._db)\n        return user\n```\n\n- Setup `AUTH_USER_MODEL` in settings.py\n\n- Run `python manage.py makemigrations` and `python manage.py migrate` (Due to optional Payment model from root project)\n- Optional settings:\n  - `DRF_SHOP_PAGE_SIZE` on will be default 10\n  - `DRF_SHOP_PAYMENT_MODEL` = "projects.payments.models.Payment"\n  - `DRF_SHOP_PAYMENT_STATUS_CHOICES` = "project.payments.choices.PaymentStatus"\n  - `DRF_SHOP_BONUS_RATE` = percentage value for each order that will go to bonus wallet\n\n## Dependencies\n\n    django\n    drf\n    drf-yasg 1.21.5\n    rest_framework_simplejwt\n    mixer\n    django-filter\n\n### TODO\n\n- Add DB indexes\n- Task for currency rate update\n- Review permissions\n',
    'author': 'Oleksandr Korol',
    'author_email': 'oleksandr.korol@coaxsoft.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
