from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from new_app.forms import EducationFormSet

from new_app.forms import CandidateForm, EducationForm
from new_app.models import Candidate, Education


# Create your views here.

def indexx(request):
    return render(request, "indexx.html")

def join(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        courses = request.POST.getlist('course[]')
        universities = request.POST.getlist('university[]')
        years = request.POST.getlist('year[]')

        candidate = Candidate.objects.create(name=name, email=email)

        for i in range(len(courses)):
            course = courses[i]
            university = universities[i]
            year = years[i]
            Education.objects.create(candidate=candidate, course=course, university=university, year=year)

        return HttpResponse('Candidate and Education objects created successfully.')
    else:
        return render(request, 'join.html')

def save_candidate(request):
    print("Save candidate view called")

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']

        candidate = Candidate.objects.create(name=name, email=email)

        courses = request.POST.getlist('course[]')
        universities = request.POST.getlist('university[]')
        years = request.POST.getlist('year[]')

        for i in range(len(courses)):
            Education.objects.create(candidate=candidate, course=courses[i], university=universities[i], year=years[i])

        return JsonResponse({'status': 'success'})

    return JsonResponse({'status': 'error'})

def education(request):
    data = Education.objects.all().select_related('candidate')
    return render(request, 'education.html', {'data': data})

def view(request):
    data = Education.objects.all()
    return render(request, 'view.html', {'data': data})



def delete(request,id):
    wm = Education.objects.get(id=id)
    wm.delete()
    return redirect("education")








