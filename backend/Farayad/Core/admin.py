from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Category, Course

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )
    search_fields = ('username', 'first_name', 'last_name', 'email')


admin.site.register(User, CustomUserAdmin)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display= ('header', 'author')
    list_filter= ('date_published', 'date_modified')
    search_fields = ('header',)

    class Meta:
        ordering = ('date_modified','header', 'author')
    
    def get_form(self, request, obj=None, **kwargs):
        form=super().get_form(request, obj, **kwargs)


        return form