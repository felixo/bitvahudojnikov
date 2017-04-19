from django.contrib import admin
from .models import Artist, Partner, Sponsor, Task_1, Task_2, Task_3, Task_4, Task_5, Task_6, Task_7, Jury, Tasks, Vote

class Task_1Admin(admin.ModelAdmin):
    list_display = ('artist1', 'docfile','count')

class Task_2Admin(admin.ModelAdmin):
    list_display = ('artist1', 'docfile','count')

class Task_3Admin(admin.ModelAdmin):
    list_display = ('artist1', 'docfile','count')

class Task_4Admin(admin.ModelAdmin):
    list_display = ('artist1', 'docfile','count')

class Task_5Admin(admin.ModelAdmin):
    list_display = ('artist1', 'docfile','count')

class Task_6Admin(admin.ModelAdmin):
    list_display = ('artist1', 'docfile','count')

class Task_7Admin(admin.ModelAdmin):
    list_display = ('artist1', 'docfile','count')

class ArtistAdmin(admin.ModelAdmin):
    search_fields = ['email']

admin.site.register(Artist, ArtistAdmin)
admin.site.register(Partner)
admin.site.register(Sponsor)
admin.site.register(Tasks)
admin.site.register(Task_1, Task_1Admin)
admin.site.register(Task_2, Task_2Admin)
admin.site.register(Task_3, Task_3Admin)
admin.site.register(Task_4, Task_4Admin)
admin.site.register(Task_5, Task_5Admin)
admin.site.register(Task_6, Task_6Admin)
admin.site.register(Task_7, Task_7Admin)
admin.site.register(Jury)
admin.site.register(Vote)

# Register your models here.
