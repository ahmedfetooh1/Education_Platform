from django.shortcuts import redirect, render , get_object_or_404
from .models import Subject ,Course
from .forms import CourseForm

# Create your views here.

def subject_courses_list(request):
    subjects = Subject.objects.prefetch_related('courses').all()
    return render(request,'course/subject_courses_list.html',context={'subjects':subjects})


def course_detail(request , slug):
    course = get_object_or_404(Course ,slug=slug)

    context = {
        'detail':course
    }
    return render(request,'course/course_detail.html',context)


def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.owner = request.user
            course.save()
            return redirect('courses:subject_courses_list')
    
    else :
        form = CourseForm()

    context = {
        'form' : form
    }
    return render(request,'course/add_course.html',context)
