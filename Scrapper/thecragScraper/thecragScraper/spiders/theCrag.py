from gc import callbacks
import scrapy
from thecragScraper.items import ThecragscraperItem

class TheCragSpider(scrapy.Spider):
    name = 'crag'
    start_urls = ['https://www.thecrag.com/en/climbing/canada/routes']


    def parse(self, response):
        item = ThecragscraperItem()
        for spots in response.css('tr.actionable'):
            
            item['name'] = spots.css('span.route a::text').get(),
            item['grade'] = spots.css('span.pull-right::text').get(),
            item['tags'] = spots.css('span.tags::text').get(),
            try:
                item['description'] = spots.css('div.markdown p::text').get()
            except:
                item['description'] = "Not available!"


        
                
            yield item

            
        # next_page = response.css('li.next a').attrib['href']

        # if next_page is not None:
        #     yield response.follow(next_page, callback=self.parse)