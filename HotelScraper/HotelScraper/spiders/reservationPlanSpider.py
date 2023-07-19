import scrapy


class ReservationplanspiderSpider(scrapy.Spider):
    name = "reservationPlanSpider"
    allowed_domains = ["go-fujita-kanko.reservation.jp"]
    start_urls = ["https://go-fujita-kanko.reservation.jp/ja/hotels/fkg008/plans"]

    def parse(self, response):
        planLinks = response.css("div.p-listLayout a::attr('href')").getall()
        planLinks = [s for s in planLinks if s != 'javascript:void(0)']
        print("***********", len(planLinks))

        for planLink in planLinks:
            yield response.follow(planLink, callback=self.parsePlanPage)
    
    def parsePlanPage(self, response):
        cancel_policy_items = response.css("ul.p-box-confirm-cancel li")
        cancel_policy = []
        for item in cancel_policy_items:
            dt = item.css("dl dt::text").get()
            dd = item.css("dl dd::text").get()
            cancel_policy.append(dt + " : " + dd)
        yield {
            'name': response.css("div.p-listLayout-wrapper div.p-listLayout-detail dt::text").get(),
            'details': response.css("p.detail-text > span.close + span.open::text").get(),
            'cancel_policy': cancel_policy
        } 
