from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from .forms import BmiForm
from .utils import bmi_calculator

def home(request):
    bmi = ''
    year = datetime.now().year
    form = BmiForm()
    if request.method=='POST':
        form = BmiForm(request.POST)
        if form.is_valid():
            form_cd = form.cleaned_data
            h = float(form_cd.get('height'))
            w = float(form_cd.get('weight'))
            bmi, bmi_means = bmi_calculator(h, w)
    return render(request, 'index.html', locals())

