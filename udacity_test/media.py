# -*- coding:utf-8 -*-

class Movie():
    """movie实体类"""

    def __init__(self, title, poster_image_url, trailer_url):
        """
        Input: title => 电影名称
               poster_image_url => 电影海报链接
               trailer_url => 电影播放youtube地址
        """
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_url = trailer_url

    def toString(self):
        """打印对象的属性值"""
        print(self.title + ">>>" + self.poster_image_url + ">>>" + self.trailer_url)
