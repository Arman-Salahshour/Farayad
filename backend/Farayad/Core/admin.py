from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Category, GeneralCategory, Course, Season, Comment, News, Payment

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


@admin.register(GeneralCategory)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class SubCategoryAdmin(admin.ModelAdmin):
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
        print(obj)
        if obj == None:
            form.base_fields['author'].queryset = User.objects.filter(username=request.user.username)
        else:
            form.base_fields['author'].queryset = User.objects.filter(username=obj.author.username)
        return form

@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    list_display= ('header', 'course')
    list_filter= ('date_published', 'date_modified')
    search_fields = ('header', 'course')

    class Meta:
        ordering = ('course','date_modified')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display= ('course', 'user')
    list_filter= ('date_published',)
    search_fields = ('course', 'user')

    class Meta:
        ordering = ('date_published','course')



@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display= ('header', 'author')
    list_filter= ('date_published', 'date_modified')
    search_fields = ('header',)

    class Meta:
        ordering = ('date_modified','header', 'author')
    
    def get_form(self, request, obj=None, **kwargs):
        form=super().get_form(request, obj, **kwargs)
        print(obj)
        if obj == None:
            form.base_fields['author'].queryset = User.objects.filter(username=request.user.username)
        else:
            form.base_fields['author'].queryset = User.objects.filter(username=obj.author.username)
        return form


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display= ('course', 'purchaser')
    list_filter= ('date_purchased',)
    search_fields = ('course', 'purchaser')

    class Meta:
        ordering = ('date_purchased','course')

