# serializers.py
from rest_framework import serializers

from .models import AboutMe
from .models import TopSkills
from .models import Certifications
from .models import Experience
from .models import Education

class AboutMeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AboutMe
        fields = ('title', 'aboutText')

class TopSkillsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TopSkills
        fields = ('skillName', 'company')

class CertificationsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Certifications
        fields = ('name', 'year', 'imageName')

class ExperienceSerializer(serializers.HyperlinkedModelSerializer):
    top_skills = serializers.StringRelatedField(many=True)
    class Meta:
        model = Experience
        fields = ('company', 'year', 'jobTitle', 'description', 'top_skills')

class EducationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Education
        fields = ('course','school', 'year')