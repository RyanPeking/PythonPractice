# 插入

import pymongo
client = pymongo.MongoClient('192.168.1.15', 27017)
db = client.TBTL_tea
post = {
    'name': 'liudana',
    'age': 'M',
    'age': '18',
    'class': ['DB', 'Python', 'Java', 'Math', '数据分析', 'linux'],
    'income': '1000000'
}

posts = db.posts
post_id = posts.insert_one(post).inserted_id
print("post id is:", post_id)

