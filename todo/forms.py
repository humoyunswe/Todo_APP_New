from django.forms import ModelForm, DateTimeInput

from .models import Todo

class AddTodo(ModelForm):
    class Meta:
        model = Todo
        fields = ['title','link','end','link']
        widgets = {
            'end':DateTimeInput(attrs={'type':'datetime-local'})
        }