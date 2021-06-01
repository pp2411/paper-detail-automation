from import_export import resources
from .models import Faculty, Paper

class FacultyResource(resources.ModelResource):
    class Meta:
        model = Faculty

class PaperResource(resources.ModelResource):
    class Meta:
        model = Paper
        fields = ('author__name', 'title' , 'link', 'authors' ,'publication', 'noOfCitations' , 'noOfYr')
        export_order = ('author__name' , 'title' , 'authors' , 'publication' , 'noOfYr' , 'noOfCitations', 'link')