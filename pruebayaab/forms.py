from django import forms


class Formularioyaab(forms.Form):

    nombre = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe tu nombre'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Escribe tu email'})
    )
    mensaje = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escribe tu mensaje', 'rows': 4})
    )
    telefonico = forms.CharField(
        max_length=10,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe tu numero telefonico', 'type':'tel'})
    )

