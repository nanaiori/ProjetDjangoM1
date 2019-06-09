from django import forms
from .models import Livre

class ContactForm(forms.Form):
    sujet = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    envoyeur = forms.EmailField(label="Votre adresse e-mail")
    renvoi = forms.BooleanField(help_text="Cochez si vous souhaitez obtenir une copie du mail envoyé.", required=False)

class LivreForm(forms.ModelForm):
    class Meta:
        model = Livre
        fields = '__all__'
        photo = forms.ImageField()
