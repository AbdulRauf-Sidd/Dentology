from django.shortcuts import render, redirect
from .models import Dentist, Patient
from django.db.models import Q
from django.urls import reverse

# Create your views here.
def login(request):
    if request.POST:
        email = request.POST["email"];
        password = request.POST['password'];
        try:
            dent = Dentist.objects.get(email=email, password=password);
            request.session['id'] = dent.id;
            return redirect('http://127.0.0.1:8000/home/');
            #return search(request, dent.id);
            #absolute_url = reverse('mainapp:search/' + str(dent.id))
            #return redirect(absolute_url);
        except:
            context = {"message":"Error 404 (not really)"}
            return render(request, 'login.html', context);
    else:
        return render(request, 'login.html', {});


def home(request):
    #try:
        if request.session["id"] == False:
            raise Exception;
        dent = Dentist.objects.get(id=request.session["id"]);
        context = {"ID": dent.first_name};
        return render(request, 'home.html', context);
    #except:
        return redirect('http://127.0.0.1:8000/login/');

def test(request):
    request.session['id'] = False;
    return render(request, 'test.html', {});

def search(request, tid):
    key = request.GET.get("search", "");
    if key != "":
        results = Patient.objects.filter(Q(first_name__icontains=key) | Q(last_name__icontains=key)
                                        | Q(phone__icontains=key));
    
        context = {
            'results': results,
        }
        return render(request, "search-results.html", context);
    else:
        return render(request, 'search.html', {});

def patientlist(request, tid):
    data = Patient.objects.all();
    return render(request, 'patientlist.html', {"data":data})

def edittooth1(request, pid):
    if request.POST:
        history = request.POST["history"];
        scheduled = request.POST["scheduled"];
        image = request.POST["image"];
        
    else:
        return render(request, "teethlist.html", {});


def edittooth2(request, pid, tid):
    return render(request, "edittooth.html", {});