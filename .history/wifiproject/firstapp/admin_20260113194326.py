# core/admin.py
from django.contrib import admin
from .models import Job, Result, Admitcard, Govtupdate, Boxname 


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active", "status", "published_date")
    search_fields = ("title",)        # last me comma zaroori hai
    list_filter = ("is_active", "status",)      # last me comma zaroori hai
    prepopulated_fields = {"slug": ("title",)}

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active", "status", "published_date")
    search_fields = ("title",)        # last me comma zaroori hai
    list_filter = ("is_active", "status",)      # last me comma zaroori hai
    prepopulated_fields = {"slug": ("title",)}

@admin.register(Admitcard)
class AdmitcardAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active", "status", "published_date")
    search_fields = ("title",)        # last me comma zaroori hai
    list_filter = ("is_active", "status", )  # last me comma zaroori hai
    prepopulated_fields = {"slug": ("title",)}

@admin.register(Govtupdate)
class GovtupdateAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active", "status", "published_date")
    search_fields = ("title",)        # last me comma zaroori hai
    list_filter = ("is_active", "status",)      # last me comma zaroori hai
    prepopulated_fields = {"slug": ("title",)}

@admin.register(Boxname)
class BoxnameAdmin(admin.ModelAdmin):
    list_display = ("title", )
    search_fields = ("title",)        # last me comma zaroori hai



#comment

from django.contrib import admin
from .models import JobComment, ResultComment, AdmitcardComment, GovtupdateComment

@admin.register(JobComment)
class JobCommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'job', 'comment', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at', 'user')
    search_fields = ('user__username', 'comment')

@admin.register(ResultComment)
class ResultCommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'result', 'comment', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at', 'user')
    search_fields = ('user__username', 'comment')

@admin.register(AdmitcardComment)
class AdmitcardCommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'admitcard', 'comment', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at', 'user')
    search_fields = ('user__username', 'comment')

@admin.register(GovtupdateComment)
class GovtupdateCommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'govtupdate', 'comment', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at', 'user')
    search_fields = ('user__username', 'comment')



# # subscriber

# @admin.register(Subscriber)
# class SubscriberAdmin(admin.ModelAdmin):
#     list_display = ('email','created_at')
#     search_fields = ('email',)



#subsciber

from django.contrib import admin
from .models import Subscriber

admin.site.register(Subscriber)
