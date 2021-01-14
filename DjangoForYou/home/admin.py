from django.contrib import admin
from home.models import Post, BlogComment, Contact, Subscriber

admin.site.register(BlogComment)
admin.site.register(Post)
admin.site.register(Contact)
admin.site.register(Subscriber)
