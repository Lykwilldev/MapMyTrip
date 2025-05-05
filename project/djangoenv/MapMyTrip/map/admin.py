from django.contrib import admin
from .models import Profile
from .models import Highlight
from .models import Photo
from .models import Comment


admin.site.register(Profile)
admin.site.register(Highlight)
admin.site.register(Photo)
admin.site.register(Comment)
# Register your models here.
