from django import forms
from .models import Resume, Education, Project, Skill, Certification, Experience, Hobby

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['full_name', 'email', 'phone', 'address', 'linkedin', 'github', 'objective', 'profile_pic', 'template_style']
        # 'user' is handled automatically in the view
        exclude = ['user']
        widgets = {
            'objective': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write a brief professional summary...'}),
            'address': forms.Textarea(attrs={'rows': 2, 'placeholder': 'City, Country or Full Address'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make specific fields optional
        self.fields['profile_pic'].required = False
        self.fields['linkedin'].required = False
        self.fields['github'].required = False
        
        # Add Bootstrap classes to all fields for consistent styling
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

# Standardized Formsets used in views.py
# 'extra=1' ensures one blank row is shown by default
EducationFormSet = forms.inlineformset_factory(Resume, Education, fields='__all__', extra=1, can_delete=True)
ExperienceFormSet = forms.inlineformset_factory(Resume, Experience, fields='__all__', extra=1, can_delete=True)
SkillFormSet = forms.inlineformset_factory(Resume, Skill, fields='__all__', extra=1, can_delete=True)
ProjectFormSet = forms.inlineformset_factory(Resume, Project, fields='__all__', extra=1, can_delete=True)
CertificationFormSet = forms.inlineformset_factory(Resume, Certification, fields='__all__', extra=1, can_delete=True)
HobbyFormSet = forms.inlineformset_factory(Resume, Hobby, fields='__all__', extra=1, can_delete=True)