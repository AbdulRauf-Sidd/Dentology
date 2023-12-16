from django.shortcuts import render, redirect
from .models import Dentist, Patient
from django.urls import reverse

# Create your views here.
def login(request):
    if request.POST:
        email = request.POST["email"];
        password = request.POST['password'];
        try:
            dent = Dentist.objects.get(email=email, password=password);
            request.session['id'] = dent.id;
            return redirect('http://127.0.0.1:8000/search/' + str(dent.id));
            #return search(request, dent.id);
            #absolute_url = reverse('mainapp:search/' + str(dent.id))
            #return redirect(absolute_url);
        except:
            context = {"message":"Error 404 (not really)"}
            return render(request, 'login.html', context);
    else:
        return render(request, 'login.html', {});


def home(request):
    try:
        if request.session["id"] == False:
            raise Exception;
        context = {"key": request.session["id"]};
        return render(request, 'home.html', context);
    except:
        return redirect('http://127.0.0.1:8000/login/');

def test(request):
    request.session['id'] = False;
    return render(request, 'test.html', {});

def search(request, tid):
    return render(request, 'search.html', {"tid":tid});

def patientlist(request, tid):
    data = Patient.objects.all();
    return render(request, 'patientlist.html', {"data":data})