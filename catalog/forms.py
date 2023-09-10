from django import forms
from .models import BlogPost, Product, Version
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Сохранить'))


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Сохранить'))

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')

        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        for word in forbidden_words:
            if word in name.lower() or word in description.lower():
                raise forms.ValidationError(f"Нельзя добавлять слово '{word}' в название или описание продукта.")


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = ['product', 'version_number', 'version_name', 'is_current']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Сохранить'))
