from django.shortcuts import render
from django.views.generic import TemplateView
from . models import *
# Create your views here.
class CloudView(TemplateView):
    template_name = "cloud_capitals.html"

    def create_cloud_product(self, reqest):
        cloud_product = CloudCapitals.objects.all()

        return render(reqest, 'cloud_capitals.html', locals())

class CloudCreateView(TemplateView):
    template_name = "cloud_create.html"



