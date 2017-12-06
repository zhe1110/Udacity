# -*- coding:utf-8 -*-


# 创建对象
from udacity_test import media, fresh_tomatoes

movieShawshank = media.Movie("The Shawshank Redemption",
                             "https://upload.wikimedia.org/wikipedia/zh/a/af/Shawshank_Redemption_ver2.jpg",
                             "https://www.youtube.com/watch?v=spEPXHfKiCs")
movieGump = media.Movie("Forrest Gump", "https://upload.wikimedia.org/wikipedia/zh/a/ad/Forrestgumppost.jpg",
                        "https://www.youtube.com/watch?v=bLvqoHBptjg")
movieTruman = media.Movie("The Truman Show", "https://upload.wikimedia.org/wikipedia/zh/c/cd/Trumanshow.jpg",
                          "https://www.youtube.com/watch?v=oY_FcMif5bQ")

# 打印对象属性
movieShawshank.toString()
movieGump.toString()
movieTruman.toString()

# 把对象组成集合
movies = [movieShawshank, movieGump, movieTruman]

# 调用页面工具方法
fresh_tomatoes.open_movies_page(movies)
