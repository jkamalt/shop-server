from django import forms

from users.forms import UserRegistrationForm, UserProfileForm
from users.models import User
from products.models import Product, ProductCategory


class UserAdminRegistrationForm(UserRegistrationForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'image', 'first_name', 'last_name', 'password1', 'password2')


class UserAdminProfileForm(UserProfileForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control py-4'}))


class ProductAdminCreateForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'placeholder': 'Введите название продукта'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите описание продукта'}), required=False)
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}))
    price = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control py-4', 'placeholder': 'Введите цену'}), max_digits=8, decimal_places=2, min_value=0)
    quantity = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control py-4', 'placeholder': 'Введите количество'}), min_value=0)
    category = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control py-2 form-select'}), queryset=ProductCategory.objects.all(), empty_label=None)

    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'price', 'quantity', 'category')


class ProductCategoryAdminCreateForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'placeholder': 'Введите название категории'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите описание категории'}), required=False)

    class Meta:
        model = ProductCategory
        fields = ('name', 'description')
