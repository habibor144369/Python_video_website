from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import Video
from .models import Detail


# Register your models here.
admin.site.register(Detail)

class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Video, MyModelAdmin)
