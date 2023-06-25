from django.contrib import admin
from music.models import *


admin.site.register(public)
admin.site.register(private_file_name)
admin.site.register(protected_file_name)

