from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from user.models import User


@admin.register(User)
# Register your models here.
class FastWalletUser(UserAdmin):
    pass
