from django import forms


class NewTicketForm(forms.Form):
    title = forms.CharField(max_length=60)
    description = forms.CharField(widget=forms.TextInput)