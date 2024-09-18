from django.contrib import admin

from task_tracker.models import Task, Tag, Comment, Project, Attachment


class CommentInline(admin.StackedInline):
    model = Comment
    class Meta:
        extra = 2


class TagMembershipInline(admin.TabularInline):
    model = Tag.tasks.through



@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = [ "id","title", "description","status","priority","view_created_at"]
    list_display_links = ["title"]
    # fields = ["title", "description",("status","priority")]
    exclude = ["height_level"]
    ordering = ["priority","status"]
    search_fields = ["title","description"]
    list_filter = ["status","priority"]
    list_editable = ("priority",)
    actions = ["create_close_status"]

    # list_per_page = 3

    @admin.action(description='Create close status')
    def create_close_status(modeladmin, request, queryset):
        queryset.update(status='cl')

    inlines = [
        CommentInline,
        TagMembershipInline
    ]


    @admin.display(empty_value="???")
    def view_created_at(self, obj):
        return f"data created: {obj.created_at}"


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(Attachment)
class AttachmentAdmin(admin.ModelAdmin):
    pass
