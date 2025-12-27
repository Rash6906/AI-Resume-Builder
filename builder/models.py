from django.db import models
from django.contrib.auth.models import User

class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    objective = models.TextField()
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    template_style = models.CharField(max_length=20, default='ats')

class Skill(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='skills') # Changed for consistency
    category = models.CharField(max_length=50, choices=[('Technical', 'Technical'), ('Soft', 'Soft')], default='Technical')
    skill_name = models.CharField(max_length=100)
class Education(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='education_details')
    institution = models.CharField(max_length=500) 
    degree = models.CharField(max_length=500)
    score = models.CharField(max_length=100)
    start_year = models.CharField(max_length=20)
    end_year = models.CharField(max_length=20)

class Project(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='projects') # Changed for consistency
    title = models.CharField(max_length=500)
    date = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()
class Experience(models.Model):
    resume = models.ForeignKey(Resume, related_name='experiences', on_delete=models.CASCADE)
    company = models.CharField(max_length=300, blank=True, null=True)
    role = models.CharField(max_length=300, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    start_date = models.CharField(max_length=100, blank=True, null=True)
    end_date = models.CharField(max_length=100, blank=True, null=True)

class Certification(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='certifications')
    title = models.CharField(max_length=500)
    issuing_organization = models.CharField(max_length=500)
    date_obtained = models.CharField(max_length=100, null=True, blank=True)

class Hobby(models.Model):
    resume = models.ForeignKey(Resume, related_name='hobbies', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)