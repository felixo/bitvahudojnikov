from django.contrib import admin
from .models import Artist, Partner, Sponsor, Task_1, Task_2, Jury, Tasks

admin.site.register(Artist)
admin.site.register(Partner)
admin.site.register(Sponsor)
admin.site.register(Tasks)
admin.site.register(Task_1)
admin.site.register(Task_2)
admin.site.register(Jury)

# Register your models here.
