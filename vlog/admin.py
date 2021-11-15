from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import *


admin.site.register(TzUser)
admin.site.register(Post)
admin.site.register(Comments, MPTTModelAdmin)


# Register your models here.
