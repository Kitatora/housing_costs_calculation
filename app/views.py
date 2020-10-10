from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from app.forms import OwnHouseForm


class TopView(View):
    def get(self, request, *args, **kwargs):
        form = OwnHouseForm(
            request.POST or None,
            initial={
                'price': "0",
                'RRF': "0",
                'MMF': "0",
                'OMF': "0",
                'loan': "0",
                'interest': "0",
                'down': "0",
                'term': "0",
                'rent_fee': "0",
                'mnt': "0",
                'r_other': "0",
                'r_term': "0",
            }
        )

        return render(request, 'app/calculation.html', {
            'form': form,
        })

    def post(self, request, *args, **kwargs):
        form = OwnHouseForm(request.POST or None)
        if form.is_valid():
            price_info = form.cleaned_data['price']
            RRF_info = form.cleaned_data['RRF']
            MMF_info = form.cleaned_data['MMF']
            OMF_info = form.cleaned_data['OMF']
            loan_info = form.cleaned_data['loan']  # 借入額
            interest_info = form.cleaned_data['interest']/100  # ローン利率（年利）
            down_info = form.cleaned_data['down']
            term_info = form.cleaned_data['term']  # 年数
            rent_info = form.cleaned_data['rent_fee']  # 賃貸価格
            mnt_info = form.cleaned_data['mnt']  # 管理費(メンテ)
            r_other_info = form.cleaned_data['r_other']  # その他
            r_term_info = form.cleaned_data['r_term']  # 賃貸期間
        else:
            print(form.errors)
            return redirect('about') 
            # 数値検証がエラーとなった場合、aboutを返す

        form = OwnHouseForm(
            request.POST or None,
            initial={
                'price': "0",
                'RRF': "0",
                'MMF': "0",
                'OMF': "0",
                'loan': "0",
                'interest': "0",
                'down': "0",
                'term': "0",
                'rent_fee': "0",
                'mnt': "0",
                'r_other': "0",
                'r_term': "0",
            }
        )
        # 戸建て計算
        m_term = term_info*12  # 返済回数(月数)
        m_interest = interest_info/12  # ローン利息(月利)
        price_info = price_info  # 物件価格
        total_RRF = RRF_info*m_term  # 修繕積立金
        total_MMF = MMF_info*m_term  # 管理費
        total_OMF = OMF_info*m_term  # その他費用
        total_interest = round(((m_interest*(1+m_interest)**m_term)/((1+m_interest)**m_term-1))*loan_info)*m_term-loan_info #ローン利息総額
        vat = round(price_info*0.1)  # 消費税10%
        miscellaneous = round(price_info*0.001)  # 火災保険や登記非（一般的に物件価格の0.1%）
        miscelleneous_if_loan = round(price_info*0.025) # ローン保険等（みずほ銀行ローン計算からテスト20回行った結果）
        total_property_tax = round(price_info*0.004)*term_info  # 所得税/年
        grand_total = price_info+total_RRF+total_MMF+total_OMF+total_interest+vat+miscellaneous+miscelleneous_if_loan+total_property_tax
        initial = down_info+vat+miscellaneous+miscelleneous_if_loan
        variable = price_info+total_RRF+total_MMF+total_OMF+total_interest+total_property_tax
        p_li = []
        for i in range(term_info+1):
            p_li.append(str(initial+(variable/term_info)*i))
        p_li = ','.join(p_li)
        t_li = []
        for i in range(term_info):
            t_li.append(str(i+1))
        t_li = ','.join(t_li)

        # 賃貸計算
        r_m_term = r_term*12 #賃貸期間（月）
        total_rent_fee = rent_fee*r_term #賃貸期間（月）
        total_mnt = mnt*r_m_term #賃貸期間（月）
        total_r_other = r_m_other*r_term #賃貸期間（月）
        r_initial = rent_fee*2#敷金礼金(1ヶ月ずつ)
        grand_r_total = total_rent_fee+total_mnt+total_r_other+r_initial

        return render(request, 'app/calculation.html', {
            'form': form,
            'total_price': price_info,
            'total_RRF': total_RRF,
            'total_MMF': total_MMF,
            'total_OMF': total_OMF,
            'total_interest': total_interest,
            'vat': vat,
            'miscellaneous': miscellaneous,
            'miscellaneous_if_loan': miscelleneous_if_loan,  # ローン みずほ銀行ローンサイト諸経費より
            'property_tax': total_property_tax,  # 固定資産税
            'grand_total': grand_total, #総計
            'p_li': p_li,
            't_li': t_li
        })

class AbtView(TemplateView):
    template_name = 'app/about.html'

# class View(View):
#     get(self, request, *args, **kwargs):
