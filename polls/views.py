from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from polls.models import Job
import requests

# Create your views here.   


def index(request):
    job_display = Job.objects.all()
    context = {'job_display': job_display}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    href = get_object_or_404(Job, pk=question_id)
    return render(request, 'polls/detail.html', {'href': href})