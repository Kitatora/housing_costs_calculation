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
                'repayment': "0",
            }
        )
        return render(request, 'app/calculation.html', {
            'form': form
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
        else:
            print(form.errors)
            return redirect('about')

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
                'repayment': "0",
            }
        )
        m_term = term_info*12  # 返済回数(月数)
        m_interest = interest_info/12  # ローン利息(月利)
        print(m_interest)
        price_info = price_info  # 物件価格
        total_RRF = RRF_info*m_term  # 修繕積立金/年
        total_MMF = MMF_info*m_term  # 管理費/年
        total_OMF = OMF_info*m_term  # その他費用/年
        # total_interest = round(((m_interest(1+m_interest)**m_term)/((1+m_interest)**m_term-1))*loan_info-loan_info) #ローン利息総額
        total_interest = price_info/10 #ローン利息総額
        vat = round(price_info*0.1)  # 消費税10%
        miscellaneous = round(price_info*0.001)  # 火災保険や登記非（一般的に物件価格の0.1%）
        # ローン保険等（みずほ銀行ローン計算からテスト20回行った結果）
        miscelleneous_if_loan = round(price_info*0.025)
        total_property_tax = round(price_info*0.004)*term_info  # 所得税/年
        m_payment = (loan_info*m_interest*(1+m_interest)**m_term) / \
            ((1+m_interest)**m_term-1)  # 元利均等返済における毎月返済額

        # p_li = []
        # for i in range(m_loan):
        #     p_li.append()

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
            'grand_total': price_info+total_RRF+total_MMF+total_OMF+total_interest+vat+miscellaneous+miscelleneous_if_loan+total_property_tax,
        })


class AbtView(TemplateView):
    template_name = 'app/about.html'
