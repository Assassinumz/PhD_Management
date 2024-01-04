import pyrebase
from .models import User
import os

from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test, login_required
from django.views.decorators.http import require_http_methods

config = {
  "apiKey": "AIzaSyDV3dMnayHIM1UlyTqJTh_KPJmdx8AmI8k",
  "authDomain": "phd-paper.firebaseapp.com",
  "databaseURL": "https://databaseName.firebaseio.com",
  "storageBucket": "phd-paper.appspot.com",
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()
# Create your views here.

def user_login(request):
    if request.user.is_authenticated:
        if(request.user.is_superuser):
            return redirect('admin:index')
    
        return redirect('user_dashboard')

    error = False
    if request.method == "POST":
        try:
            username = request.POST['username']
            password = request.POST['password']
            
            user = authenticate(request, username=username, password=password)
            login(request, user)

            if(request.user.is_superuser):
                return redirect('admin')
            else:
                return redirect('user_dashboard')
        except:
            error = True

    return render(request, 'home.html', {'error':error})


def paperUpload(req, paper):
    with open(f"./media/{paper.name}", 'wb+') as destination:
        for chunk in paper.chunks():
            destination.write(chunk)

    storage.child(f"{req.user.username}/{paper.name}").put(f"./media/{paper.name}")
    if os.path.isfile(f"./media/{paper.name}"):
       os.remove(f"./media/{paper.name}")
    return storage.child(f"{req.user.username}/{paper.name}").get_url(token='1')


@login_required
@require_http_methods(['POST'])
def delete_paper(request):
    try:
        request.POST['paper_1']
        User.objects.filter(id=request.user.id).update(paper_1=None)
    except:
        pass
    try:
        request.POST['paper_2']
        User.objects.filter(id=request.user.id).update(paper_2=None)
    except:
        pass
    try:
        request.POST['paper_3']
        User.objects.filter(id=request.user.id).update(paper_3=None)
    except:
        pass
    try:
        request.POST['cv']
        User.objects.filter(id=request.user.id).update(cv=None)
    except:
        pass
    try:
        request.POST['paper_4']
        User.objects.filter(id=request.user.id).update(paper_4=None)
    except:
        pass
    try:
        request.POST['paper_5']
        User.objects.filter(id=request.user.id).update(paper_5=None)
    except:
        pass
    try:
        request.POST['aps']
        User.objects.filter(id=request.user.id).update(aps=None)
    except:
        pass
    try:
        request.POST['paper_6']
        User.objects.filter(id=request.user.id).update(paper_6=None)
    except:
        pass
    try:
        request.POST['pre_synopsis']
        User.objects.filter(id=request.user.id).update(pre_synopsis=None)
    except:
        pass
    try:
        request.POST['paper_7']
        User.objects.filter(id=request.user.id).update(paper_7=None)
    except:
        pass
    try:
        request.POST['thesis']
        User.objects.filter(id=request.user.id).update(thesis=None)
    except:
        pass
    try:
        request.POST['pdc']
        User.objects.filter(id=request.user.id).update(pdc=None)
    except:
        pass
    
    return redirect('user_dashboard')


@login_required
def user_dashboard(request):
    if request.method == "POST":
        try:
            link = paperUpload(request, request.FILES['paper_1'])
            User.objects.filter(id=request.user.id).update(paper_1=link)
            user = User.objects.get(id=request.user.id)
            if(user.pub_1_check == 'rejected'):
                User.objects.filter(id=request.user.id).update(pub_1_check='pending')
        except:
            pass
        
        try:
            user = User.objects.get(id=request.user.id)
            if user.pub_1_check:
                link = paperUpload(request, request.FILES['paper_2'])
                User.objects.filter(id=request.user.id).update(paper_2=link)
                user = User.objects.get(id=request.user.id)
                if(user.pub_2_check == 'rejected'):
                    User.objects.filter(id=request.user.id).update(pub_2_check='pending')
        except:
            pass
        
        try:
            user = User.objects.get(id=request.user.id)
            if user.pub_2_check:
                link = paperUpload(request, request.FILES['paper_3'])
                User.objects.filter(id=request.user.id).update(paper_3=link)
                user = User.objects.get(id=request.user.id)
                if(user.pub_3_check == 'rejected'):
                    User.objects.filter(id=request.user.id).update(pub_3_check='pending')
        except:
            pass
        
        try:
            user = User.objects.get(id=request.user.id)
            #if user.pub_3_check:
            link = paperUpload(request, request.FILES['cv'])
            User.objects.filter(id=request.user.id).update(cv=link)
            if(user.cv_check == 'rejected'):
                User.objects.filter(id=request.user.id).update(cv_check='pending')
        except:
            pass
        
        try:
            user = User.objects.get(id=request.user.id)
            if user.pub_3_check:
                link = paperUpload(request, request.FILES['paper_4'])
                User.objects.filter(id=request.user.id).update(paper_4=link)
                if(user.pub_4_check == 'rejected'):
                    User.objects.filter(id=request.user.id).update(pub_4_check='pending')
        except:
            pass
        
        try:
            user = User.objects.get(id=request.user.id)
            if user.pub_4_check:
                link = paperUpload(request, request.FILES['paper_5'])
                User.objects.filter(id=request.user.id).update(paper_5=link)
                if(user.pub_5_check == 'rejected'):
                    User.objects.filter(id=request.user.id).update(pub_5_check='pending')
        except:
            pass
        
        try:
            user = User.objects.get(id=request.user.id)
            #if user.pub_5_check:
            link = paperUpload(request, request.FILES['aps'])
            User.objects.filter(id=request.user.id).update(aps=link)
            if(user.aps_check == 'rejected'):
                User.objects.filter(id=request.user.id).update(aps_check='pending')
        except:
            pass
        
        try:
            user = User.objects.get(id=request.user.id)
            if user.pub_5_check:
                link = paperUpload(request, request.FILES['paper_6'])
                User.objects.filter(id=request.user.id).update(paper_6=link)
                if(user.pub_6_check == 'rejected'):
                    User.objects.filter(id=request.user.id).update(pub_6_check='pending')
        except:
            pass
        
        try:
            user = User.objects.get(id=request.user.id)
            #if user.pub_6_check:
            link = paperUpload(request, request.FILES['pre_synopsis'])
            User.objects.filter(id=request.user.id).update(pre_synopsis=link)
            if(user.pre_synopsis == 'rejected'):
                User.objects.filter(id=request.user.id).update(pre_synopsis_check='pending')
        except:
            pass
        
        try:
            user = User.objects.get(id=request.user.id)
            if user.pub_6_check:
                link = paperUpload(request, request.FILES['paper_7'])
                User.objects.filter(id=request.user.id).update(paper_7=link)
                if(user.pub_7_check == 'rejected'):
                    User.objects.filter(id=request.user.id).update(pub_7_check='pending')
        except:
            pass
        
        try:
            user = User.objects.get(id=request.user.id)
            #if user.pre_synopsis_check:
            link = paperUpload(request, request.FILES['thesis'])
            User.objects.filter(id=request.user.id).update(thesis=link)
            if(user.thesis_check == 'rejected'):
                User.objects.filter(id=request.user.id).update(thesis_check='pending')
        except:
            pass
        
        try:
            user = User.objects.get(id=request.user.id)
            if user.thesis_check:
                link = paperUpload(request, request.FILES['pdc'])
                User.objects.filter(id=request.user.id).update(pdc=link)
                if(user.pdc_check == 'rejected'):
                    User.objects.filter(id=request.user.id).update(pdc_check='pending')
        except:
            pass
    
    user = User.objects.get(id=request.user.id)
    
    context = {
        'user':user
    }
    return render(request, 'user_dashboard.html', context)


@login_required
def profile(request):
    if request.method == "POST":
        user = User.objects.get(id=request.user.id)

        try:
            picture = request.FILES['profile_picture']
            link = paperUpload(request, picture)
            user.profile_picture = link
        except:
            pass
        
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.roll_number = request.POST['roll_number']
        user.mobile_number = request.POST['mobile_number']
        user.father_name = request.POST['father_name']
        user.mother_name = request.POST['mother_name']
        user.guardian_name = request.POST['guardian_name']
        user.address = request.POST['address']
        user.gender = request.POST['gender']
        user.research_area = request.POST['research_area']
        user.save()

    user = User.objects.get(id=request.user.id)
    context = {
        'user':user
    }
    return render(request, 'profile.html', context)

@login_required
@require_http_methods(['POST'])
def remove_publication(request):
    user = User.objects.get(id=request.user.id)
    key = request.POST['key']
    publications = user.publications
    del publications[key]
    user.publications = publications
    user.save()
    return redirect('achievements')

@login_required
@require_http_methods(['POST'])
def remove_conference(request):
    user = User.objects.get(id=request.user.id)
    key = request.POST['key']
    conferences = user.conference
    del conferences[key]
    user.conference = conferences
    user.save()
    return redirect('achievements')


@login_required
@require_http_methods(['POST'])
def remove_patent(request):
    user = User.objects.get(id=request.user.id)
    key = request.POST['key']
    patents = user.patent
    del patents[key]
    user.patent = patents
    user.save()
    return redirect('achievements')


@login_required
def achievements(request):
    user = User.objects.get(id=request.user.id)
    if request.method == "POST":
        try:
            pub_name = request.POST['publication_name']
            pub_link = request.POST['publication_link']
            if(pub_name != "" or pub_link != ""):
                user.publications[pub_name] = pub_link
                user.save()
        except:
            pass
        try:
            con_name = request.POST['conference_name']
            con_link = request.POST['conference_link']
            
            if(con_name != "" or con_link != ""):
                user.conference[con_name] = con_link
                user.save()
        except:
            pass
        try:
            pat_name = request.POST['patent_name']
            pat_link = request.POST['patent_link']
            if(pat_name != "" or pat_link != ""):
                user.patent[pat_name] = pat_link
                user.save()
        except:
            pass
        

    context = {
        'user':user
    }
    return render(request, 'achievements.html', context)

@login_required
def time_table(request):
    user = User.objects.get(id=request.user.id)
    context = {
        'tt':user.time_table
    }
    return render(request, 'time_table.html', context)

def logout_user(request):
    try:
        logout(request)
    except:
        pass
    return redirect('login')