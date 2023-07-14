from django.contrib import messages
from django.shortcuts import render,redirect

from .forms import UserRegisterForm
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,f'Sizning akauntingiz yaratildi!Hoziroq login qilib kirishingiz mumkun boladi.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form' : form})