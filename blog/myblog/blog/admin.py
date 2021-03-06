from django.contrib import admin

from .models import Post, Comment, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "author", "publish", "status", "get_tags")
    list_filter = ("status", "created", "publish", "author")
    search_fields = ("title", "body", "tags")
    prepopulated_fields = {"slug": ("title",)}
    raw_id_fields = ("author",)
    date_hierarchy = "publish"
    ordering = ["status", "publish"]
    filter_horizontal = ("tags",)
    view_on_site = True

    def get_tags(self, obj):
        return ",".join([str(tag) for tag in obj.tags.all()])


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "post", "created", "active")
    list_filter = ("active", "created", "updated")
    search_fields = ("name", "email", "body")


# admin.site.register(Post, PostAdmin)
admin.site.register(Tag)


