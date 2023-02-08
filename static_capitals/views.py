from django.http import JsonResponse, request, HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, View
# Create your views here.
# 机房列表

class MachineRooms(TemplateView):
    template_name = 'machine_rooms_list.html'

