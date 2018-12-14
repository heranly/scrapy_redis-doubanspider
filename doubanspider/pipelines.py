# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from doubanspider.items import MusicItem, MusicReviewItem
from doubanspider.items import VideoItem,VideoReviewItem
from pymongo import MongoClient


class DoubanspiderPipeline(object):
    def process_item(self, item, spider):
        mongocli = MongoClient(host="127.0.0.1", port=27017)
        db = mongocli['musics']
        db2=mongocli['movies']
        collection1 = db['music']
        collection2 = db['music_comments']
        col_mo11=db2['movies']
        col_mo12=db2['movies_comments']
        if isinstance(item, MusicItem):
            contents = {
                'music_name': item.get('music_name'),
                'music_alias': item.get('music_alias'),
                'music_singer': item.get('music_singer'),
                'music_time': item.get('music_time'),
                'music_rating': item.get('music_rating'),
                'music_votes': item.get('music_votes'),
                'music_tags': item.get('music_tags'),
                'music_url': item.get('music_url')
            }
            collection1.insert(contents)
        elif isinstance(item, MusicReviewItem):
            contents = {
                'review_title': item['review_title'],
                'review_content': item['review_content'],
                'review_author': item['review_author'],
                'review_music': item['review_music'],
                'review_time': item['review_time'],
                'review_url': item['review_url'],
            }
            collection2.insert(contents)
            
        elif isinstance(item, VideoItem):
            contents = {
            'video_name' :item['video_name'],
            'video_alias' :item['video_alias'],
            'video_actor' :item['video_actor'],
            'video_year' :item['video_vear'],
            'video_time' :item['video_time'],
            'video_rating' :item['video_rating'],
            'video_votes' :item['video_votes'],
            'video_tags' :item['video_tags'],
            'video_url' :item['video_url'],
            'video_director' :item['video_director'],
            'video_type' :item['video_type'],
            'video_bigtype' :item['video_bigtype'],
            'video_area' :item['video_area'],
            'video_language' :item['video_language'],
            'video_length' :item['video_length'],
            'video_writer' :item['video_writer'],
            'video_desc' :item['video_desc'],
            'video_episodes' :item['video_episodes'],
            }
            col_mo11.insert(contents)
        elif isinstance(item, VideoReviewItem):
            contents = {
                    'review_title' :item.get('review_title'),
                    'review_content' :item.get('review_content'),
                    'review_author' :item.get('review_author'),
                    'review_video' :item.get('review_video'),
                    'review_time' :item.get('review_time'),
                    'review_url' :item.get('review_url'),
            }
            col_mo12.insert(contents)

        return item
