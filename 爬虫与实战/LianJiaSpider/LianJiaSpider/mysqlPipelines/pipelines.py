from LianJiaSpider.items import LianjiaSpiderItem
from mysqlPipelines.sql import Sql

class LianjiaPipelines():
    def process_item(self, item, spider):
        if isinstance(item, LianjiaSpiderItem):
            house_title = item['house_title']
            ret = Sql.select_name(house_title)
            if ret[0] == 1:
                print("已经存在啦")
            else:
                house_title = item['house_title']
                house_href = item['house_href']
                house_name = item['house_name']
                house_num = item['house_num']
                house_price = item['house_price']
                house_style = item['house_style']
                house_room = item['house_room']
                house_size = item['house_size']
                house_toward = item['house_toward']
                house_imgdir = item['house_imgdir']

                Sql.insert_db_lianjia(house_title,house_href,house_name,house_num,house_price,house_style,house_room,house_size,house_toward,house_imgdir)