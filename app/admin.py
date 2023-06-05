from django.contrib import admin
from .models import MyModel, MyFile
from .forms import MyFileFormSet

class MyFileInline(admin.TabularInline):
    model = MyFile
    formset = MyFileFormSet

class MyModelAdmin(admin.ModelAdmin):
    inlines = [MyFileInline]

admin.site.register(MyModel, MyModelAdmin)