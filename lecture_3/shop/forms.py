from django import forms


class ProductCreationForm(forms.Form):
    title = forms.CharField(min_length=5, max_length=200, required=True)
    description = forms.CharField(min_length=1, max_length=200, required=False)
    amount = forms.IntegerField(min_value=0, max_value=10000, required=True)
    price = forms.IntegerField(min_value=0, required=True)






