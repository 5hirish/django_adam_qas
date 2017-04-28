from django import forms


class QInputForm(forms.Form):

    question = forms.CharField(label='',
                               widget=forms.TextInput(
                                   attrs={
                                       'placeholder': 'Ask me...',
                                       'required': 'true'
                                   }
                               ))
