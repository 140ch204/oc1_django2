from django.contrib import admin

# Register your models here.


from .models import Booking, Album, Artist


admin.site.register(Booking)


admin.site.register(Album)

admin.site.register(Artist)
