from django.forms import ModelForm, TextInput, DateTimeField, Textarea
from .models import News


class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['title', 'intro', 'text', 'date']

        widgets = {
            'title': TextInput(attrs={
                'id': "title",
                'class': "form-control txt item-bl-bg newses",
                'placeholder': "Ввидите название"
            }),
            'intro': TextInput(attrs={
                'id': "intro",
                'class': "form-control txt item-bl-bg newses",
                'placeholder': "Ввидите краткое содержание"
            }),
            'text': Textarea(attrs={
                'id': "text",
                'class': "form-control txt item-bl-bg newses",
                'placeholder': "Ввидите полное содержание"
            })
        }
