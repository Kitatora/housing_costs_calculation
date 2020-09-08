from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from app.forms import OwnHouseForm



class TopView(View):
    def get(self, request, *args, **kwargs):
        form = OwnHouseForm(request.POST or None)
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
            loan_info = form.cleaned_data['loan']
            interest_info = form.cleaned_data['interest']/100
            down_info = form.cleaned_data['down']
            repayment_info = form.cleaned_data['repayment']
            m_repayment = repayment_info*12
            m_loan = loan_info*12

        return render(request, 'app/calculation.html', {
            'form': form, #これがないと入力フォームのデータが計算のたびに消える
            'total_price' : price_info, #物件価格総額
            'total_RRF' : RRF_info*(repayment_info*120), #修繕積立総額
            'total_MMF' : MMF_info*(repayment_info*120), #管理費総額
            'total_OMF' : OMF_info*(repayment_info*120), #その他総額
            'total_interest' : (price_info*loan_info/12*(1+m_loan)**m_repayment/((1+m_loan)**m_repayment-1)*m_loan)-price_info, #ローン利息
            'vat' : price_info*0.1, #消費税
            'Miscellaneous' : price_info*0.001, #
            'Miscellaneous_if_loan' : price_info*0.0025, #ローン みずほ銀行ローンサイト諸経費より
            'property_tax' : price_info*0.004*(repayment_info*120), #固定資産税
        })

class AbtView(TemplateView):
    template_name = 'app/about.html'
    