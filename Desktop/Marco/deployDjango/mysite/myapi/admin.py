from django.contrib import admin
from .models import AboutMe
from .models import TopSkills
from .models import Certifications
from .models import Experience
from .models import Education

# Register your models here.
admin.site.register(AboutMe)
admin.site.register(TopSkills)
admin.site.register(Certifications)
admin.site.register(Experience)
admin.site.register(Education)
