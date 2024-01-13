from django.shortcuts import render, redirect
from .models import Dentist, Patient, Tooth
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
    return render(request, 'test.html', {});

def addpatient(request):
    if request.POST:
        lname = ""
        fname = ""
        dent = Dentist.objects.get(id=request.session["id"]);
        name = request.POST["name"].split();
        if len(name) > 1:
            fname = str(name[0]);
            lname = "".join(name[1:]);
        else:
            fname = name;
        gender = request.POST["gender"];
        email = request.POST["email"];
        group = request.POST["group"];
        age = request.POST["age"];
        phone = request.POST["phone"];
        history = request.POST["history"];
        obj = Patient(first_name=fname, last_name=lname, gender=gender, email=email, phone=phone, group=group, history=history, dentist=dent);
        obj.save();
        return redirect('http://127.0.0.1:8000/home/')
    else:
        return render(request, 'addPatients2.html', { 'ID' : request.session['id']})

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
    if request.POST:
        obj = Patient.objects.get(id=pid);
        new = Tooth.objects.get(patient_id = pid, tooth_number = tid);
        new.patient_id = obj
        new.tooth_number = tid;
        new.history = request.POST["history"];
        new.scheduled = request.POST["future"];
        new.note = "";
        if len(request.FILES) != 0:
            new.image = request.FILES["image"];
        new.save();
        return render(request, 'tooth-detail.html', {});
    else:
        obj = Tooth.objects.get(patient_id = pid, tooth_number = tid);
        context = {"name": request.session["id"], "item": obj.image, "number": obj.tooth_number, "history": obj.history, "future": obj.scheduled};
        return render(request, "tooth-detail.html", context);