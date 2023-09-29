from django.contrib import admin

from users.models import User
from baskets.admin import BasketAdmin


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = (BasketAdmin,)
    list_display = ('username', 'first_name', 'last_name', 'is_staff', 'is_active', 'date_joined')
    ordering = ('username',)
    search_fields = ('username',)
