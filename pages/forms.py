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

class logs(forms.Form):
    log = forms.CharField(label='', widget=forms.Textarea(attrs={'readonly': 'readonly', 'id': 'logtext', 'hidden': 'hidden'}))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        f = open("debug.log", "r")
        text = f.read()
        self.fields['log'].initial = text
