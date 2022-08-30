from django.contrib import admin
# from rest_framework.authtoken.models import Token
from rest_framework.authtoken.models import TokenProxy
from account.models import *



class UserAdmin(admin.ModelAdmin):
    list_display = ('username',)
    radio_fields = {'role': admin.HORIZONTAL , 'status': admin.HORIZONTAL}


admin.site.register(User,UserAdmin)
class MealAdmin(admin.ModelAdmin):
    list_display = ('type','status','date')
    radio_fields = {'status': admin.HORIZONTAL}

admin.site.register(Meal, MealAdmin)

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name','user','type')
    radio_fields = {'user': admin.HORIZONTAL}

admin.site.register(Item, ItemAdmin)
admin.site.register(UserRelation)


