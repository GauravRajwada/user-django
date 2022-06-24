from multiprocessing import context
from django.shortcuts import redirect, render

# Create your views here.
from .forms import UserCreate
from .models import User

def user_create(request):
    if request.method == 'POST':
        user_form=UserCreate(request.POST)
        user_form.save()
        context={
            'all_data':User.objects.all(),
        }
        return render(request,'user/userOutput.html',context=context)

    user_form=UserCreate()
    return render(request,'user/user.html',{'form':user_form})

def show_data(request):
    context={
        'all_data':User.objects.all(),
    }
    return render(request,'user/userOutput.html',context=context)



