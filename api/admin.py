from django.contrib import admin

from .models import User, Operation, Record

admin.site.register([User, Operation, Record])
