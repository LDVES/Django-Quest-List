from django import forms

class AddQuestForm(forms.Form):
    quest_title = forms.CharField(label='Title', max_length=50)
    quest_body = forms.CharField(label='Body', max_length=100)
