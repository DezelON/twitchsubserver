from django import forms
from django.utils.translation import ugettext as _

class UserLoginForm(forms.Form):
    nickname = forms.CharField(label=_(u'Ur nickname'), max_length=30, widget=forms.TextInput(attrs={'class': 'input input-group__field', 'value': '', 'autofocus': '', 'required': '', 'placeholder': 'New nickname'}))