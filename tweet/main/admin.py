from django.contrib import admin
from main.models import User, Tweet

class UserAdmin(admin.ModelAdmin):
	list_display = ('nick_name', 'first_name', 'last_name', 'password', 'email', 'location', 'image_profile','biography', 'birth_date',)
	search_field = ('nick_name',)
	readonly_fields=('nick_name',)


class TweetAdmin(admin.ModelAdmin):
	list_display = ('owner', 'status',)



admin.site.register(User, UserAdmin)
admin.site.register(Tweet, TweetAdmin)