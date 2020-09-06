from django import forms

class OwnHouseForm(forms.Form):
    # Own or rentalのどちらかを選ぶ選択肢」
    # 戸建て or マンションのどちらかを選ぶ選択肢
    price = forms.IntegerField(max_length=10, label='物件価格')
    RRF = forms.IntegerField(max_length=7, label='修繕積立')
    MMF = forms.IntegerField(max_length=7, label='管理費')
    OMF = forms.IntegerField(max_length=7, label='その他')
    #ローンの有無を選ぶ選択肢
    loan = forms.IntegerField(max_length=10, label='ローン借入額')
    interest = forms.FloatField(max_length=5, label='金利')
    down = forms.IntegerField(max_length=10, label='頭金')
    repayment = forms.IntegerField(max_length=3, label='返済期間')
    #入力情報に合わせて変数を設定