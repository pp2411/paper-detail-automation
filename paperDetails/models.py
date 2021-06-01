from django.db import models
from users.models import Profile
# Create your models here.
class Faculty(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    empId = models.CharField(max_length=20)
    organisation = models.ForeignKey(Profile, on_delete = models.CASCADE)

    def __str__(self):
        return f'{self.name} {self.email}'

class Paper(models.Model):
    author = models.ForeignKey(Faculty, on_delete = models.CASCADE)
    title = models.CharField(max_length=100)
    link = models.URLField(null=True)
    authors = models.CharField(max_length=150 , null=True)
    publication = models.CharField(max_length=150 , null=True)
    noOfCitations = models.IntegerField(null=True)
    citation_id = models.CharField(max_length=30, null=True)
    citation_link = models.URLField( null=True)
    # year = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.title} by {self.author}'


class BulkRequest(models.Model):
    req = models.FileField(upload_to = 'Bulkrequests/')

    def __str__(self):
        return f'{str(self.req)}'