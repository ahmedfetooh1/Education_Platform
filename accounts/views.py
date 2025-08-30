from django.shortcuts import get_object_or_404, redirect, render
from .forms import SignUpForm , InstructorProfileForm
from django.contrib.auth import login ,logout , authenticate
from .models import InstructorProfile
from django.contrib.auth.decorators import login_required

# Create your views here.

def sign_up(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            InstructorProfile.objects.create(user=user)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')


            user = authenticate(request ,username=username , password=password)
            if user is not None :
                login(request , user)
                return redirect('accounts:view_profile')
    context = {
        'form':form ,
    }
    return render(request,'accounts/sign_up.html',context)


def sign_out(request):
    logout(request)
    return redirect('accounts:sign_in')


def sign_in(request):
    ERROR = None
    if request.user.is_authenticated :
        return redirect('courses:subject_courses_list')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None :
            login(request,user)
            return redirect('accounts:view_profile')
        else :
            ERROR = 'Invalid credeticats!, Password or Username is invalid!'

    context = {
        'error':ERROR
    }

    return render(request,'accounts/sign_in.html',context)

@login_required(login_url='accounts:view_profile')
def view_profile(request):
    profile =get_object_or_404(InstructorProfile,user=request.user)
    context = {
        'profile':profile
    }
    return render(request,'accounts/view_profile.html',context)



@login_required(login_url='accounts:edit_profile')
def edit_profile(request):
    profile = get_object_or_404(InstructorProfile,user = request.user)
    form = InstructorProfileForm(instance=profile)
    if request.method == 'POST':

        form = InstructorProfileForm(request.POST,request.FILES , instance=profile)
        if form.is_valid():
            form.save()
            return redirect('accounts:view_profile')
    
    context = {
        'form':form
    }
    return render(request,'accounts/edit_profile.html',context)


