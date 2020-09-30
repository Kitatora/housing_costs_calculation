from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

class OwnHouseForm(forms.Form):
    price = forms.IntegerField(label='物件価格', validators=[MinValueValidator(0), MaxValueValidator(1000000000)])
    RRF = forms.IntegerField(label='修繕積立', validators=[MinValueValidator(0), MaxValueValidator(100000)])
    MMF = forms.IntegerField(label='管理費', validators=[MinValueValidator(0), MaxValueValidator(100000)])
    OMF = forms.IntegerField(label='その他', validators=[MinValueValidator(0), MaxValueValidator(100000)])
    loan = forms.IntegerField(label='ローン借入額', validators=[MinValueValidator(0), MaxValueValidator(1000000000)])
    interest = forms.FloatField(label='金利')
    down = forms.IntegerField(label='頭金', validators=[MinValueValidator(0), MaxValueValidator(1000000000)])
    term = forms.IntegerField(label='返済期間', validators=[MinValueValidator(1), MaxValueValidator(50)])
    rent_fee = forms.IntegerField(label='賃貸価格', validators=[MinValueValidator(0), MaxValueValidator(1000000000)])
    mnt = forms.IntegerField(label='管理費', validators=[MinValueValidator(0), MaxValueValidator(100000)])
    r_other = forms.IntegerField(label='その他', validators=[MinValueValidator(0), MaxValueValidator(100000)])
    r_term = forms.IntegerField(label='賃貸期間', validators=[MinValueValidator(1), MaxValueValidator(50)])
    # first_name = forms.CharField(max_length=30, label='姓')


