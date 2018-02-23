from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from horserace import forms
from django.contrib.auth.views import logout
from django.contrib.auth.decorators import login_required
from .models import Horse
from django.contrib.auth.models import User


# Create your views here.
# def handle_uploaded_image(f, path="/img"):
#    with open(path, 'wb+') as destination:
#        for chunk in f.chunks():
#            destination.write(chunk)


@login_required
def log_out(request):
    logout(request)
    return redirect('home')

def index(request):
    data = {}
    if request.method == "POST":
        var = request.POST.get('but')
        if var == 'Войти':
            form = forms.UserAuthForm(request.POST)
            # print(form)
            if form.is_valid():
                user = authenticate(username=form.cleaned_data['username'], password=request.POST.get('password'))
                # print(user)
                if user is not None:
                    login(request, user)
                    return redirect('main/1')
                else:
                    error = "Неправильный логин или пароль"
                    data.update({'errors': error})
            else:
                data.update({'errors': form.errors})
        elif var == 'Зарегистрировать':
            form = forms.UserRegForm(request.POST)
            # print(form.errors)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect('main/1')
            else:
                data.update({'errors': form.errors})
    auth_form = forms.UserAuthForm()
    reg_form = forms.UserRegForm()
    data.update({'auth_form': auth_form, 'reg_form': reg_form})
    return render(request, "index.html", data)

def index2(request):
    data = {}
    if request.method == "POST":
        var = request.POST.get('but')
        if var == 'Войти':
            log = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=log, password=password)
            if user is not None:
                login(request, user)
                return redirect('main/1')
            else:
                    error = "Неправильный логин или пароль"
                    data.update({'errors': error})
        elif var == 'Зарегистрировать':
            username = request.POST.get('username')
            password = request.POST.get('password')
            password_check = request.POST.get('password_check')
            email = request.POST.get('email')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            err = 0
            try:
                u = User.objects.get(username=username)
                data.update({'errors': "Логин уже существует"})
            except User.DoesNotExist:
                pass
            if (len(username) < 5):
                err += 1
                data.update({'errors': "Слишком маленький логин"})
            if (password != password_check):
                err += 1
                data.update({'errors': "Пароли не совпали"})
            if not (('@' in email) & ('.' in email)):
                err += 1
                data.update({'errors': "Неверно написана почта"})
            if (err == 0):
                u = User.objects.create(username=username, email=email, first_name=first_name, last_name=last_name)
                User.set_password(u, password)
                u.save()
                login(request, u)
                return redirect('main/1')
            else:
                pass
    return render(request, "index2.html", data)

@login_required
def main(request, page):
    horses = Horse.objects.all()
    print(horses)
    page_int = int(page)
    count = horses.count()
    horses = horses[(page_int-1)*8:page_int*8]
    data = {'horses': horses}
    if not(page_int == 1):
        data.update({'prev': page_int-1})
    if not(page_int*8 > count):
        data.update({'next': page_int+1})
    return render(request, 'main.html', data)

