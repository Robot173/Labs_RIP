from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from horserace import forms
from django.contrib.auth.views import logout
from django.contrib.auth.decorators import login_required
from .models import Horse

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
            if form.is_valid():
                user = authenticate(username=form.cleaned_data['username'], password=request.POST.get('password'))
                # print(request.POST.get('username'), request.POST.get('password') )
                if user is not None:
                    login(request, user)
                    return redirect('main/1')
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


def main(request, page):
    if not request.user.is_authenticated:
        return HttpResponseRedirect("/")
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


def add(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect("/")
    if request.method == "POST":
        form = forms.HorseForm(request.POST, request.FILES)
        if form.is_valid():
            hor = form.save()
            return HttpResponseRedirect('/horse/id='+str(hor.id))
            # handle_uploaded_image(request.FILES['file'])
        else:
            pass  # Вызов исключения
    else:
        form = forms.HorseForm()
        return render(request, 'add.html', {'form': form})


def horse_view(request, hid):
    if not request.user.is_authenticated:
        return HttpResponseRedirect("/")
    horse = Horse.objects.get(id=hid)
    if request.method == "POST":
        user_id = request.user.id
        horse.users.add(user_id)
    users = horse.users.all()
    # print(users)
    return render(request, 'horse.html', {'horse': horse, 'users': users})
