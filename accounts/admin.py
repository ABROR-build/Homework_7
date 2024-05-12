from django.contrib import admin
from . import models


class AccountsAdmin(admin.ModelAdmin):
    list_display = ['username', 'age', 'profile_picture', 'bio']


admin.site.register(models.Accounts, AccountsAdmin)
