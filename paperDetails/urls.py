from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('',views.about, name='about'),
    path('home/', views.home, name = 'home'),
    path('update/',views.updatePage, name = 'updatePage'),
    path('updateThisFac/' , views.updateOneByOne, name = 'updateThisFac'),
    path('updateInBulk/' , views.updateInBulk, name = 'updateInBulk'),
    path('downloadFormat/' , views.downloadFormat, name = 'downloadFormat'),
    path('facultyList/', views.FacultyListView.as_view(), name = 'facultyList'),
    # path('facultyDetail/<int:pk>/',views.FacultyDetailsView.as_view(), name = 'faculty-details' ),
    path('facultyDetail/<int:pk>/',views.PaperDetailsView.as_view(), name = 'faculty-details' ),
    path('downloadData/' , views.downloadPapers , name = 'downloadData')
]