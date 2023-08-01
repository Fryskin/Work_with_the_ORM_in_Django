from django import forms

from main.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'description', 'category', 'date_of_creation', 'date_of_last_change', 'price')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_title(self):
        cleaned_title = self.cleaned_data.get('title')
        cleaned_description = self.cleaned_data.get('description')
        black_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for black_list_word in black_list:
            if black_list_word in cleaned_title:
                raise forms.ValidationError("Bruh. It's forbidden title.")
            if black_list_word in cleaned_description:
                raise forms.ValidationError("Bruh. It's forbidden description.")

        return cleaned_title
