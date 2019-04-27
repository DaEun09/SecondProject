from django import forms
from .models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = {'name', 'age', 'major', 'grade', 'hometown',}

# class PostForm(forms.Form):
    # title = forms.CharField(label='제목', max_length=100)
    # text = forms.CharField(label='제목', widget=forms.Textarea)