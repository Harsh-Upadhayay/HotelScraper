import scrapy


class ReservationplanspiderSpider(scrapy.Spider):
    name = "reservationPlanSpider"
    allowed_domains = ["go-fujita-kanko.reservation.jp"]
    start_urls = ["https://go-fujita-kanko.reservation.jp/ja/hotels/fkg008/plans"]

    def parse(self, response):
        planLinks = response.css("div.main >  div.p-listLayout-wrapper > div.p-listLayout  a::attr('href')").getall()
        planLinks = [s for s in planLinks if s != 'javascript:void(0)']
        print("***********", len(planLinks))

        for planLink in planLinks:
            yield response.follow(planLink, callback=self.parsePlanPage)
    
    def parsePlanPage(self, response):
        yield {
            'name': response.css("div.p-listLayout-wrapper  div.p-listLayout-detail dt::text").get()
        }
