from django.urls import path, re_path

from . import views

urlpatterns = [
    path("", views.index, name="index"),  # 首页
    path("login/", views.login, name="login"),  # 登录
    path("register/", views.register, name="register"),  # 注册
    path("logout/", views.logout, name="logout"),  # 退出
    path("modify_pwd/", views.modify_pwd, name="modify_pwd"),  # 修改密码
    path("search/", views.search, name="search"),  # 搜索
    path("all_book/", views.all_book, name="all_book"),  # 所有书籍
    path("book/<int:book_id>/", views.book, name="book"),  # 具体的书籍
    path("score/<int:book_id>/", views.score, name="score"),  # 评分
    path("comment/<int:book_id>/", views.comment, name="comment"),  # 评论
    path("comment_like/<int:comment_id>/", views.comment_like, name="comment_like"),  # 给评论点赞
    path("collect/<int:book_id>/", views.collect, name="collect"),  # 收藏
    path("like/<int:book_id>/", views.like, name="like"),  # 点赞
    path("new_book/", views.new_book, name="new_book"),  # 新书速递
    path("hot_book/", views.hot_book, name="hot_book"),  # 热门书籍
    path("sort_book/", views.sort_book, name="sort_book"),  # 图书分类
    path("recommend_book/", views.recommend_book, name="recommend_book"),  # 猜你喜欢
    path("purchase_index/", views.purchase_index, name="purchase_index"),  # 购买书籍首页
    path("purchase_check/<int:book_id>/", views.purchase_check, name="purchase_check"),  # 查看购买书籍详情
    path("purchase/", views.purchase, name="purchase"),  # 立即购买书籍
    path("purchase_pay/", views.purchase_pay, name="purchase_pay"),  # 支付
    path("add_shop_list/", views.add_shop_list, name="add_shop_list"),  # 添加到购物车
    path("sub_shop_list/", views.sub_shop_list, name="sub_shop_list"),  # 移除购物车书籍
    path("shop_list_pay/", views.shop_list_pay, name="shop_list_pay"),  # 购物车结算
    path("shop_list/", views.shop_list, name="shop_list"),  # 购物车
    path("personal/", views.personal, name="personal"),  # 个人中心
    path("my_like/", views.my_like, name="my_like"),  # 获取我的点赞
    path("my_collect/", views.my_collect, name="my_collect"),  # 获取我的收藏
    path("my_rate/", views.my_rate, name="my_rate"),  # 我打分过的书籍
    path("my_comments/", views.my_comments, name="my_comments"),  # 我的评论
    path("delete_rate/<int:rate_id>", views.delete_rate, name="delete_rate"),  # 取消评分
    path("delete_comment/<int:comment_id>", views.delete_comment, name="delete_comment"),  # 取消评论
]