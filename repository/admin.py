from django.contrib import admin
from repository.models import Company, User
# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'status')

admin.site.register(Company, CompanyAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_first_name', 'user_last_name', 'email')
    

admin.site.register(User, UserAdmin)
