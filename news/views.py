from django.shortcuts import render

# Create your views here.
from news.forms import ApplicationForm
from news.models import Course, Teacher


def home(request):
    course = Course.objects.all()
    teacher = Teacher.objects.all()
    context = {
        'course': course,
        'teacher': teacher,
    }
    return render(request,'home.html',context)

def about_detail(request,pk):
    course = Course.objects.get(pk=pk)


    form = ApplicationForm(request.POST or None)
    is_success = False
    if request.method == 'POST' and form.is_valid():
        is_success = True
        form.save()
        form = ApplicationForm()



    context = {
        'course': course,
        'form': form,
        'is_success': is_success,
    }
    return render(request,'about_detail.html',context)


