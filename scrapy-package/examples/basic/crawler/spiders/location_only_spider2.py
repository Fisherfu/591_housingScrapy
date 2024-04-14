from scrapy import Request
from scrapy_twrh.spiders.rental591 import Rental591Spider, util
from scrapy_twrh.items import RawHouseItem, GenericHouseItem


class LocationOnlySpider(Rental591Spider):
    #name = 'location-only'
    name = 'detail-generic-only2'

    def __init__(self):
        self.count_per_city = {}
        super().__init__(
            parse_list=self.my_parse_list, 
            parse_detail=self.my_parse_detail,
           # target_cities=['台北市','新北市','桃園市','新竹市','新竹縣',
           #                '苗栗縣','台中市','彰化縣','宜蘭縣','基隆市','嘉義縣',
           #                '嘉義市','雲林縣','台南市','高雄市','南投縣',
           #                '花蓮縣','臺東縣','屏東縣','澎湖縣','連江縣','金門縣']
           # target_cities=['新北市','桃園市','新竹市','新竹縣','苗栗縣','台中市','彰化縣','宜蘭縣','基隆市','嘉義縣',
           #                '嘉義市','雲林縣','台南市','高雄市','南投縣']

           # target_cities=['澎湖縣','連江縣','金門縣','桃園市','新竹市','新竹縣','苗栗縣','台中市','彰化縣','宜蘭縣','基隆市','嘉義縣',
           #                '嘉義市','雲林縣','台南市']               
            #target_cities=['花蓮縣','臺東縣','屏東縣','澎湖縣','連江縣','金門縣']
            
            target_cities=['台北市','新北市','桃園市']
           # '臺北市','新北市','桃園市','新竹市','新竹縣',
        )


    def my_parse_list(self, response):
        for item in self.default_parse_list(response):
            # allow only detail request to speedup entire process
            if isinstance(item, Request):
               yield item
               
               
                # meta = item.meta['rental']
                # if isinstance(meta, util.DetailRequestMeta):
                #     yield item

    # def my_parse_detail(self, response):
    #     for item in self.default_parse_detail(response):
    #         if isinstance(item, Request):
    #             # allow location page request
    #             yield item
    #         elif isinstance(item, GenericHouseItem):
    #             # ignore RawHouseItem
    #             # only yield item with rough_coordinate
    #             if 'rough_coordinate' in item and item['rough_coordinate'] is not None:
    #                 yield item

    def my_parse_detail(self, response):
         for item in self.default_parse_detail(response):
             if isinstance(item, GenericHouseItem):
                # ignore RawHouseItem
                yield item


            