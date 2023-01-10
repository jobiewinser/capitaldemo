from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView
import requests
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import random
import re 
@method_decorator(csrf_exempt, name="dispatch")
class DemoView(TemplateView):
    template_name='demo.html'
    def get(self, request, *args, **kwargs):
        if request.META.get("HTTP_HX_REQUEST", 'false') == 'true':
            self.template_name = "demo_card_contents.html"
        return super().get(request, *args, **kwargs)
    def get_context_data(self, **kwargs):
        context = super(DemoView, self).get_context_data(**kwargs)    
        response_json = requests.get(url="https://countriesnow.space/api/v0.1/countries/capital").json().get('data', [])
        random_choice = random.choice(response_json)
        context['country'] = random_choice.get('name')
        return context
    def post(self, request):
        context = {}
        request_country = request.POST.get('country', '')
        request_capital = request.POST.get('capital', '')
        if request_capital:
            response_json = requests.get(url="https://countriesnow.space/api/v0.1/countries/capital").json().get('data', [])
            capital_key_dict = {}
            country_key_dict = {}
            for dict in response_json:
                dict_capital = dict.get('capital', '').lower()
                dict_country = dict.get('name', '').lower()
                if dict_capital and dict_country:
                    capital_key_dict[dict_capital] = dict_country
                    country_key_dict[dict_country] = dict_capital
            if capital_key_dict.get(request_capital.lower().replace(" ", ""), 'NOT A COUNTRY') == request_country.lower().replace(" ", ""):
                context['correct'] = True
            else:
                context['correct'] = False
            context['request_country'] = request_country
            context['request_capital'] = request_capital
            context['correct_capital'] = country_key_dict.get(request_country.lower(), '')
            context['country'] = random.choice(response_json).get('name')
            return render(request, "demo_card_contents.html", context)

        context['error'] = "Please enter a capital"
        context['country'] = request_country
        return render(request, "demo_card_contents.html", context)