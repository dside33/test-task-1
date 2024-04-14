from django.contrib import admin
from .models import TestSet, Test

class TestInline(admin.TabularInline):
    model = Test
    extra = 1

class TestSetAdmin(admin.ModelAdmin):
    inlines = [TestInline]

admin.site.register(TestSet, TestSetAdmin)
