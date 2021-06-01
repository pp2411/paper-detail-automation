from bs4 import BeautifulSoup
import requests
import re

class Scraper():
    HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}
    BASE_URL = "https://scholar.google.com"


    def makeUrl(self, name):
        return f"{self.BASE_URL}/citations?hl=en&view_op=search_authors&mauthors={name}&btnG="

    def makeUrlFit(self, name):
        ''' this function removes space if present in name and returns name[0]+name[1] else name'''
        name = name.split(" ")
        if len(name)>1:
            name = "+".join(name)
        else:
            name = name[0]
        return name

    def seePapers(self, faculty):
        url = self.BASE_URL+faculty['link']
        response = requests.get(url,headers = self.HEADERS)
        soup = BeautifulSoup(response.content , 'lxml')
        data = []
        for result in soup.select('.gsc_a_tr'):
            title = result.select('.gsc_a_at')[0].get_text()
            link = self.BASE_URL+result.select('a')[0]['data-href']
            author = result.select('.gs_gray')[0].get_text()
            publication = result.select('.gs_gray')[1].get_text()
            citations = {}
            citations['value'] = result.select('.gsc_a_c')[0].get_text()
            citations['link'] = result.select('a')[1]['href']
            citations['cites_id'] = citations['link'].split('=')[-1]
            year = result.select('.gsc_a_y')[0].get_text()
            dt = {}
            dt['title'] = title
            dt['link'] = link
            dt['author'] = author
            dt['publication'] = publication
            dt['citations'] = citations
            dt['year'] = year
            data.append(dt)
        return data

    def scrape(self, name, organisation):
        ''' takes the search term and returns the papers and theses details for this term '''
        name = self.makeUrlFit(name)
        url = self.makeUrl(name)
        response  = requests.get(url, headers = self.HEADERS)
        soup = BeautifulSoup(response.content,'lxml')
        linkMap = []
        for result in soup.select('.gsc_1usr'):
            affiliation = result.select('.gs_ai_aff')[0].get_text()
            email = result.select('.gs_ai_eml')[0].get_text()
            # print(affiliation)
            # print(email)
            if re.search(organisation.organisationName.lower(),affiliation.lower()) is not None:
                fac = result.select('h3')[0].get_text()
                link = result.select('a')[0]['href']
                # print(f"{fac} : {link}")
                mp = {}
                mp['name'] = fac
                mp['link'] = link
                linkMap.append(mp)

        # print(linkMap)    
        for faculty in linkMap:
            faculty['papers'] = self.seePapers(faculty)
        
        return linkMap
            