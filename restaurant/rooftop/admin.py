from django.contrib import admin

# Register your models here.
from rooftop.models import sage
admin.site.register(sage)

from rooftop.models import reserve
admin.site.register(reserve)

from rooftop.models import comment
admin.site.register(comment)