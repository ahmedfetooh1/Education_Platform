from django.shortcuts import redirect, render
from .forms import SignUpForm
from django.contrib.auth import login ,logout , authenticate

# Create your views here.

def sign_up(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')


            user = authenticate(request ,username=username , password=password)
            if user is not None :
                login(request , user)
                return redirect('courses:subject_courses_list')
    context = {
        'form':form ,
    }
    return render(request,'accounts/sign_up.html',context)


def sign_out(request):
    logout(request)
    return redirect('accounts:sign_up')