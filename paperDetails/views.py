from django.shortcuts import render
from .forms import FacultyInfoUpdateForm
from django.views.generic import ListView, DetailView
from .models import Paper,Faculty, BulkRequest
from users.models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.list import MultipleObjectMixin
from django.contrib import messages
from .Scraper import Scraper
import re
import mimetypes
from django.http import HttpResponse
import pandas as pd
from tablib import Dataset
from random import randint
from time import sleep
from .resources import PaperResource
# Create your views here.

def about(request):
    return render(request, 'paperDetails/index.html')

@login_required
def home(request):
    return render(request , 'paperDetails/home.html')

@login_required
def updatePage(request):
    fac_form = FacultyInfoUpdateForm()
    return render(request , 'paperDetails/updateInfo.html' , {'fac_form':fac_form})

@login_required
def updateOneByOne(request):
    fac_form = FacultyInfoUpdateForm(request.POST)
    if fac_form.is_valid():
        name = fac_form.cleaned_data.get('name')
        email = fac_form.cleaned_data.get('email')
        empId = fac_form.cleaned_data.get('empId')
        obj = Faculty.objects.filter(name = name , email = email , empId = empId)
        profile = Profile.objects.filter(user= request.user)[0]
        if(len(obj)<1):
            facObj = Faculty(name = name , email=email , empId=empId , organisation=profile)
            facObj.save()
            messages.success(request, f'{name} has been created under {profile} and Info Updated...')
        else:
            facObj = obj[0]
            facObj.save()
            messages.warning(request, f'Info for {name} Updated')
        # searchName = f'{name} {profile}'
        # scrapeAndUpdate(searchName , facObj)
        return render(request , 'paperDetails/home.html')


@login_required
def updateInBulk(request):
    upFile = request.FILES.get('bulkFile')
    reqObj = BulkRequest.objects.create(req = upFile)
    df = pd.read_csv(rf'{reqObj.req.path}')
    # print(df.columns)
    names = df['Name']
    emails = df['email']
    empIds = df['empId']
    try:        
        for name , email, empId in zip(names , emails,empIds):
            obj = Faculty.objects.filter(name = name , email = email , empId = empId)
            profile = Profile.objects.filter(user= request.user)[0]
            if(len(obj)<1):
                facObj = Faculty(name = name , email=email , empId=empId , organisation=profile)
                facObj.save()
            else:
                facObj = obj[0]
                facObj.save()
                
            # searchName = f'{name} {profile}'
            # scrapeAndUpdate(searchName , facObj)
            sleep(randint(5,20))
        messages.success(request,f'All the profiles updated')
    except Exception as e:
        print(str(e))
        messages.warning(request,f'There were some errors in some files. Please check the file again.')

    BulkRequest.objects.filter(id = reqObj.id).delete()
    return render(request , 'paperDetails/home.html')


@login_required
def downloadFormat(request):
    fl_path = 'media\Format\Format.csv'
    filename = 'format.csv'
    fl = open(fl_path, 'r')
    mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response

@login_required
def downloadPapers(request):
    organisation = request.user.profile
    authors = Faculty.objects.filter(organisation=organisation)
    queryset = Paper.objects.filter(author__in  = authors).order_by("author" ,"noOfYr")
    dataset = PaperResource().export(queryset)
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="FacultyDetails.csv"'
    return response


class FacultyListView(ListView, LoginRequiredMixin):
    template_name = 'paperDetails\FacultyList.html'
    context_object_name = 'faculties'
    paginate_by = 5
    def get_queryset(self):
        # print(self.request.user.profile)
        queryset = Faculty.objects.filter(organisation = self.request.user.profile).order_by('name')
        return queryset
    

# class FacultyDetailsView( LoginRequiredMixin, UserPassesTestMixin, DetailView):
#     model = Faculty
#     paginate_by = 5
#     def test_func(self):
#         faculty = self.get_object()
#         return self.request.user == faculty.organisation.user
            

#     def get_context_data(self, **kwargs):
#         print(self.kwargs['pk'])
#         context = super().get_context_data(**kwargs)
#         context['papers'] = Paper.objects.filter(author=context['object'].id).order_by('noOfYr')
#         return context

class PaperDetailsView(LoginRequiredMixin , UserPassesTestMixin , ListView):
    template_name = 'paperDetails\Faculty_detail.html'
    paginate_by = 5
    context_object_name = 'papers'
    def test_func(self):
        faculty = Faculty.objects.filter(pk = self.kwargs['pk'])[0]
        return self.request.user == faculty.organisation.user

    def get_queryset(self):
        faculty = Faculty.objects.filter(pk = self.kwargs['pk'])[0]
        queryset = Paper.objects.filter(author=faculty).order_by('-noOfCitations')
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = Faculty.objects.filter(pk = self.kwargs['pk'])[0]
        return context






# def scrapeAndUpdate(name , faculty):
#     ''' function to scrape results for a faculty and update his info '''
#     scraper = Scraper()
#     result = scraper.scrape(name)
#     for fac in result:
#         if re.search( faculty.name.lower() ,fac['name'].lower()) or re.search(fac['name'].lower() , faculty.name.lower()):
#             for paper in fac['papers']:
#                 author = faculty
#                 title = paper['title']
#                 link = paper['link']
#                 existCheck = Paper.objects.filter(title=title , link = link)
#                 authors = paper['author']
#                 publication = paper['publication']
#                 noOfCitations = paper['citations']['value']
#                 citation_id = paper['citations']['cites_id']
#                 citation_link = paper['citations']['link']
#                 year = paper['year']
#                 if year:
#                     year = int(year)
#                 else:
#                     year = 0

#                 if noOfCitations and noOfCitations[-1] == '*':
#                     noOfCitations = noOfCitations[:-1]
#                 if noOfCitations:
#                     noOfCitations = int(noOfCitations)
#                 else:
#                     noOfCitations = 0

#                 if year>0 and noOfCitations>0:
#                     paperObj = Paper(author = author , title = title, link = link, authors = authors, publication = publication, noOfCitations = noOfCitations, citation_id = citation_id, citation_link = citation_link, year = year)
                
#                 elif year>0:
#                     paperObj = Paper(author = author , title = title, link = link, authors = authors, publication = publication, year = year)
#                 elif noOfCitations>0:
#                     paperObj = Paper(author = author , title = title, link = link, authors = authors, publication = publication, noOfCitations = noOfCitations, citation_id = citation_id, citation_link = citation_link)
#                 else:
#                     paperObj = Paper(author = author , title = title, link = link, authors = authors, publication = publication,)
                
#                 if len(existCheck)>0:
#                     paperObj.id = existCheck[0].id
                
#                 paperObj.save()