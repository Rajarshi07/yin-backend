from django.contrib import admin
from .models import Contact, BlogPost, Tag, Catagory, Author, Comment, Advertisement
# Register your models here.

admin.site.register(Contact)
admin.site.register(BlogPost)
admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(Catagory)
admin.site.register(Comment)
admin.site.register(Advertisement)
