from django import forms
from pages.models import Message

class newMessage(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('title', 'body', 'author')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-textinput'}),
            'body': forms.Textarea(attrs={'class': 'form-textinput'}),
            'author':  forms.TextInput(attrs={'class': 'form-hiddeninput', 'id': 'author', 'hidden': 'hidden'}),
        }
        labels = {
            'title': 'Заголовок',
            'body': 'Текст сообщения',
            'author': 'Автор',
        }
