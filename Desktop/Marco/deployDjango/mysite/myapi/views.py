from rest_framework import viewsets

from .serializers import AboutMeSerializer
from .serializers import TopSkillsSerializer
from .serializers import CertificationsSerializer
from .serializers import ExperienceSerializer
from .serializers import EducationSerializer

from .models import AboutMe
from .models import TopSkills
from .models import Certifications
from .models import Experience
from .models import Education


class AboutMeViewSet(viewsets.ModelViewSet):
    queryset = AboutMe.objects.all().order_by('title')
    serializer_class = AboutMeSerializer

class TopSkillsViewSet(viewsets.ModelViewSet):
    queryset = TopSkills.objects.all().order_by('skillName')
    serializer_class = TopSkillsSerializer

class CertificationsViewSet(viewsets.ModelViewSet):
    queryset = Certifications.objects.all().order_by('name')
    serializer_class = CertificationsSerializer

class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all().order_by('-id')
    serializer_class = ExperienceSerializer

class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all().order_by('-year')
    serializer_class = EducationSerializer