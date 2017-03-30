### 0.setting environment
sudo apt-get install python-django

### 1.update backend
https://github.com/django-admin-bootstrap/django-admin-bootstrap
pip install bootstrap-admin

modify settings.py
```
INSTALLED_APPS = (
    'boostrap_admin',
    'django.contrib.admin'
    #
)

from django.conf import global_settings
TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.request',
)
BOOTSTRAP_ADMIN_SIDEBAR_MENU = True
```

### 2.config webpack
https://github.com/owais/django-webpack-loader/

### 3.dashboard
https://github.com/talpor/django-dashing/
pip install dashing
```
INSTALLED_APP = (
    'dashing',
)
```
### 4.debug
https://django-debug-toolbar.readthedocs.io/en/stable/installation.html

pip install django-debug-toolbar

### 5.seo
