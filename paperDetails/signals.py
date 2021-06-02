from django.db.models.signals import post_save
from .models import Faculty , Paper
from django.dispatch import receiver
from .Scraper import Scraper
import re
from random import randint
from time import sleep

@receiver(post_save, sender=Faculty)
def create_profile(sender, instance, created, **kwargs):
    print('fired')
    searchName = f'{instance.name} {instance.organisation}'
    scrapeAndUpdate(searchName , instance)
        


def scrapeAndUpdate(name , faculty):
    ''' function to scrape results for a faculty and update his info '''
    scraper = Scraper()
    result = scraper.scrape(name , faculty.organisation)
    for fac in result:
        if re.search( faculty.name.lower() ,fac['name'].lower()) or re.search(fac['name'].lower() , faculty.name.lower()):
            for paper in fac['papers']:
                author = faculty
                title = paper['title']
                link = paper['link']
                existCheck = Paper.objects.filter(title=title , link = link)
                authors = paper['author']
                publication = paper['publication']
                noOfCitations = paper['citations']['value']
                citation_id = paper['citations']['cites_id']
                citation_link = paper['citations']['link']
                year = paper['year']
                if year:
                    year = int(year)
                else:
                    year = 0

                if noOfCitations and noOfCitations[-1] == '*':
                    noOfCitations = noOfCitations[:-1]
                if noOfCitations:
                    noOfCitations = int(noOfCitations)
                else:
                    noOfCitations = 0

                if year>0 and noOfCitations>0:
                    paperObj = Paper(author = author , title = title, link = link, authors = authors, publication = publication, noOfCitations = noOfCitations, citation_id = citation_id, citation_link = citation_link, year = year)
                
                elif year>0:
                    paperObj = Paper(author = author , title = title, link = link, authors = authors, publication = publication, year = year)
                elif noOfCitations>0:
                    paperObj = Paper(author = author , title = title, link = link, authors = authors, publication = publication, noOfCitations = noOfCitations, citation_id = citation_id, citation_link = citation_link)
                else:
                    paperObj = Paper(author = author , title = title, link = link, authors = authors, publication = publication,)
                
                if len(existCheck)>0:
                    paperObj.id = existCheck[0].id
                
                paperObj.save()