from django.contrib import admin
from .models import Resume, Education, Project, Skill, Certification

# This makes your data show up in the admin panel
admin.site.register(Resume)
admin.site.register(Education)
admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Certification)