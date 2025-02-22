from django import forms


class CategoryForm(forms.Form):
    name = forms.CharField(min_length=5, max_length=200, required=True, widget=forms.TextInput({
        'class': 'form-control',
        'placeholder': 'Enter name'
    }))


class ProductCreationForm(forms.Form):
    title = forms.CharField(min_length=5, max_length=200, required=True, widget=forms.TextInput({
        'class': 'form-control',
        'placeholder': 'Enter title'
    }))
    description = forms.CharField(min_length=1, max_length=200, required=False, widget=forms.TextInput({
        'class': 'form-control',
        'placeholder': 'Enter description'
    }))
    amount = forms.IntegerField(min_value=0, max_value=10000, required=True, widget=forms.TextInput({
        'class': 'form-control',
        'placeholder': 'Enter amount'
    }))
    price = forms.IntegerField(min_value=0, required=True, widget=forms.TextInput({
        'class': 'form-control',
        'placeholder': 'Enter price'
    }))


class ProductEditForm(forms.Form):
    title = forms.CharField(min_length=5, max_length=200, required=True, widget=forms.TextInput({
        'class': 'form-control',
        'placeholder': 'Enter title'
    }))
    description = forms.CharField(min_length=1, max_length=200, required=False, widget=forms.TextInput({
        'class': 'form-control',
        'placeholder': 'Enter description'
    }))
    amount = forms.IntegerField(min_value=0, max_value=10000, required=True, widget=forms.TextInput({
        'class': 'form-control',
        'placeholder': 'Enter amount'
    }))
    price = forms.IntegerField(min_value=0, required=True, widget=forms.TextInput({
        'class': 'form-control',
        'placeholder': 'Enter price'
    }))
    category_id = forms.IntegerField(min_value=1, required=True)






