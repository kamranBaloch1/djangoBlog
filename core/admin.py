from django.contrib import admin

# Register your models here.

from .models import Blog,BlogComment,Contact

admin.site.register(Blog)
admin.site.register(BlogComment)
admin.site.register(Contact)
