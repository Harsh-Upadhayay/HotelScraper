import scrapy
from ..items import PlanItem

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

        room_items = response.css("dl.p-listLayout-reservation dd ol li")

        rooms = []
        for item in room_items:
            room_name = item.css("dl dd p::text").get()
            tag_items = item.css("dl dd ul li::text").getall()
            tags = tag_items if tag_items else []  # Convert to an empty list if no tags found
            price = item.css("div dl dd p.p-priceLayout span > strong.u-fontsize21::text").get()
            smoke = item.css("dd ul:not(.p-listLayout-reservationLabel) li:nth-child(1)::text").get()
            size = item.css("dd ul:not(.p-listLayout-reservationLabel) li:nth-child(2)::text").get()
            persons = item.css("dd ul:not(.p-listLayout-reservationLabel) li:nth-child(3)::text").get()
            if room_name is not None:
                room_data = {
                    'room_name': room_name,
                    'tags': tags,
                    'price': price,
                    'smoke': smoke,
                    'size': size,
                    'persons': persons
                }
                rooms.append(room_data)

        planItem = PlanItem()

        planItem['name'] = response.css("div.p-listLayout-wrapper div.p-listLayout-detail dt::text").get()
        planItem['details'] = response.css("p.detail-text > span.close + span.open::text").get()
        planItem['cancel_policy'] = cancel_policy
        planItem['rooms'] = rooms

        yield planItem
        
        # yield {
        #     'name': response.css("div.p-listLayout-wrapper div.p-listLayout-detail dt::text").get(),
        #     'details': response.css("p.detail-text > span.close + span.open::text").get(),
        #     'cancel_policy': cancel_policy,
        #     'rooms': rooms
        # } 

