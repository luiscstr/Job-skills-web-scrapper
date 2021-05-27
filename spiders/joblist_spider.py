""
#Created on Sun Nov 15 23:11:51 2020

#@author: lcast

import scrapy
from scrapy.crawler import CrawlerProcess




class JobsItem(scrapy.Item):
   title=scrapy.Field()
   company=scrapy.Field()
   #description=scrapy.Field()
   link_jobs=scrapy.Field()
 
jobs=JobsItem()

class JobsSpider(scrapy.Spider):
    name = "jobs"
    start_urls=["https://www.simplyhired.com/search?q=data+science+tableau&l=Weehawken%2C+NJ&job=fkS5PwZzDZBLqPVki0SoNixp6D6kR9Yc7ZXtD6FjKEtrRq-lGpfqCg"]
        
        
    def parse(self,response):
       
       for link in response.xpath("//div/div/h3[@class='jobposting-title']/a/@href"):
           full_link=response.urljoin(link.extract())  
           yield scrapy.Request(url=full_link,callback=self.parse_jobs)  

       next_page=response.urljoin(response.xpath("//div/nav[@class='pagination Pagination Pagination--withTotalJobCounts']/ul/li/a/@href")[-1].extract())
       yield scrapy.Request(url=next_page,callback=self.parse)
 
  
    def parse_jobs(self,response):
        yield {
            'Title':response.xpath("//header/div/div/div[@class='viewjob-jobTitle h2']/text()").extract(),
            'Company': response.xpath("//div//div/div/div[@class='viewjob-labelWithIcon']/text()")[0].extract(),
            'Location':response.xpath("//div//div/div/div[@class='viewjob-labelWithIcon']/text()")[1].extract(),
            'Salary': response.xpath("//div/div[@class='viewjob-jobDetails']/span[@class='viewjob-labelWithIcon viewjob-salary']/text()").extract(),
            'Description':response.xpath("//div//div/div[@class='p']/text()").extract(),
            'Link':response.url
            }
        
        
        
        
        
        
        
        
        #Indeed
        #if response.xpath("//div/div[@class='icl-u-lg-mr--sm icl-u-xs-mr--xs'][1]/a/text()").extract():
         #   company=response.xpath("//div/div[@class='icl-u-lg-mr--sm icl-u-xs-mr--xs'][1]/a/text()").extract()
        #else: 
         #   company=response.xpath("//div/div[@class='icl-u-lg-mr--sm icl-u-xs-mr--xs'][1]/text()").extract()
        #yield {
         #   'Title':response.xpath("//div/h1/text()").extract(),
          #  'Company': response.xpath("//div/a/div/div/div[@class='jobsearch-CompanyReview--heading']/text()").extract(),
           # 'Company2':company,
            #'Link':response.url
            #}
  
       # jobs['title']=response.xpath("//div/h1/text()").extract()
        #jobs['company']=response.xpath("//div/a/div/div/div[@class='jobsearch-CompanyReview--heading']/text()").extract()
        #jobs['description']=response.xpath("//div/div[@class='jobsearch-jobDescriptionText']").extract()
        #jobs['link_jobs']=response.url
        #yield jobs
        
   
        
#process=CrawlerProcess()
#process.crawl(JobsSpider)     
#process.start(stop_after_crawl=False)





