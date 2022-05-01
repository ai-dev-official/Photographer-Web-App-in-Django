from django.contrib import admin

# Register your models here.
from .models import Photo, Category  # , Comment

# Register your models here.
# class CommentInline(admin.TabularInline):
#     model = Comment
#     extra = 0


class PhotoAdmin(admin.ModelAdmin):
    pass
    # inlines = [
    #     CommentInline,
    # ]

# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('author', 'comment', 'url', 'body', 'photo', 'created_on', 'active')
#     list_filter = ('active', 'created_on')
#     search_fields = ('photo', 'email', 'comment')
#     actions = ['approve_comments']

#     def approve_comments(self, request, queryset):
#         queryset.update(active=True)


admin.site.register(Category)
admin.site.register(Photo, PhotoAdmin)
# admin.site.register(Comment)
