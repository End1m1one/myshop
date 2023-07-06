from django.contrib import admin

from account.models import CustomUser

class UserAdmin(admin.ModelAdmin):
    list_display = ('email',)

admin.site.register(CustomUser, UserAdmin)
