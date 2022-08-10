from django.contrib import admin

from api.models import Post, Comment  # @CHANGE

admin.site.register(Post)
admin.site.register(Comment)  # @CHANGE
