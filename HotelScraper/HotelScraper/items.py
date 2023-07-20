# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HotelscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

# class BaseItem(scrapy.Item):
#     unique_id = scrapy.Field()
#     error = scrapy.Field()

# class PlanItem(BaseItem):
#     plan = scrapy.Field()

# class RoomItem(BaseItem):
#     room = scrapy.Field()

class PlanItem(scrapy.Item):
    name = scrapy.Field()
    details = scrapy.Field()
    cancel_policy = scrapy.Field()
    rooms = scrapy.Field()
