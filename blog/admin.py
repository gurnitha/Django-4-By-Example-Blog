# Import django modules
from django.contrib import admin

# Import from locals
from .models import Post

# Register your models here.


admin.site.register(Post)