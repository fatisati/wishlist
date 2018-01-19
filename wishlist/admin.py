from django.contrib import admin

from .models import wish
from .models import user


admin.site.register(wish)
admin.site.register(user)