from django.forms import ModelForm

from .models import*


class MerchantForm(ModelForm):
    class Meta():
        model = Merchant
        fields = '__all__'


class OrderForm(ModelForm):
    class Meta():
        model = Percel
        fields = '__all__'        