from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=32, unique=True, verbose_name='账号')
    password = models.CharField(max_length=32, verbose_name='密码')
    phone = models.CharField(max_length=32, verbose_name='手机号码')
    name = models.CharField(max_length=32, verbose_name='名字', unique=True)
    address = models.CharField(max_length=32, verbose_name='地址')
    email = models.EmailField(verbose_name='邮箱')

    class Meta:
        db_table = 'user'
        verbose_name_plural = '用户'
        verbose_name = '用户'

    def __str__(self):
        return self.name


class Tags(models.Model):
    name = models.CharField(max_length=32, verbose_name='标签')
    intro = models.TextField(blank=True, null=True, verbose_name='简介')

    class Meta:
        db_table = 'tags'
        verbose_name = '标签'
        verbose_name_plural = '标签'

    def __str__(self):
        return self.name


class Book(models.Model):
    tags = models.ForeignKey(
        Tags,
        on_delete=models.CASCADE,
        verbose_name='标签',
        related_name='tags',
        blank=True,
        null=True,
    )

    title = models.CharField(max_length=32, verbose_name='书名')
    author = models.CharField(max_length=32, verbose_name='作者')
    published_time = models.DateField(blank=True, null=True, verbose_name='出版时间')
    intro = models.TextField(verbose_name='描述')
    pic = models.FileField(verbose_name='封面图片', max_length=64, upload_to='book_cover')
    collect_num = models.IntegerField(verbose_name='收藏人数', default=0)
    rate_num = models.IntegerField(verbose_name='评分人数', default=0)
    like_num = models.IntegerField(verbose_name='评分人数', default=0)
    look_num = models.IntegerField(verbose_name='浏览量', default=0)
    is_show = models.BooleanField(default=True, verbose_name='是否显示')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    is_purchase = models.BooleanField(default=False, verbose_name='是否可购买')
    price = models.FloatField(default=66.66, verbose_name='单价')
    inventory = models.IntegerField(verbose_name='库存', default=9999, blank=True, null=True)
    purchase_num = models.IntegerField(verbose_name='销售数量', default=0, blank=True, null=True)

    class Meta:
        db_table = 'book'
        verbose_name = '图书'
        verbose_name_plural = '图书'

    def __str__(self):
        return self.title


class PurchaseList(models.Model):
    book = models.ForeignKey(
        Book,
        related_name='purchase_book',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name='图书id',
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name='用户id',
    )
    order_code = models.CharField(max_length=20, unique=True, verbose_name='订单号')
    create_time = models.DateTimeField(verbose_name='下单时间', auto_now_add=True)
    price = models.FloatField(default=66.66, verbose_name='单价')
    purchase_num = models.IntegerField(default=1, verbose_name='购买数量')
    all_price = models.FloatField(default=66.66, verbose_name='总价')
    phone = models.CharField(max_length=64, blank=True, null=True, verbose_name='手机号')
    address = models.TextField(blank=True, null=True, verbose_name='地址')
    order_status = models.CharField(max_length=10, default='0',
                                    choices=(
                                        ('0', '待支付'),
                                        ('1', '已支付'),
                                        ('2', '待收货'),
                                        ('3', '已收货'),
                                    ), verbose_name='订单状态')
    pay_time = models.DateTimeField(blank=True, null=True, verbose_name='支付时间')
    received_time = models.DateTimeField(blank=True, null=True, verbose_name='收货时间')

    class Meta:
        db_table = 'purchase_list'
        verbose_name = '购书清单'
        verbose_name_plural = verbose_name


class RateBook(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='rate_book',
        blank=True,
        null=True,
        verbose_name='图书id',
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name='用户id',
    )
    mark = models.FloatField(verbose_name='评分')
    create_time = models.DateTimeField(verbose_name='添加时间', auto_now_add=True)

    class Meta:
        db_table = 'rate_book'
        verbose_name = '评分信息'
        verbose_name_plural = verbose_name


class CollectBook(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='collect_book',
        blank=True,
        null=True,
        verbose_name='图书id',
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name='用户id',
    )
    is_delete = models.BooleanField(default=False, verbose_name='是否取消')
    create_time = models.DateTimeField(verbose_name='收藏时间', auto_now_add=True)

    class Meta:
        db_table = 'collect_book'
        verbose_name = '图书收藏'
        verbose_name_plural = verbose_name


class LikeBook(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='like_book',
        blank=True,
        null=True,
        verbose_name='图书id',
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name='用户id',
    )
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')
    create_time = models.DateTimeField(verbose_name='点赞时间', auto_now_add=True)

    class Meta:
        db_table = 'like_book'
        verbose_name = '图书点赞'
        verbose_name_plural = verbose_name


class CommentBook(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name='用户',
    )
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name='书籍',
    )
    content = models.TextField(verbose_name='内容')
    create_time = models.DateTimeField(verbose_name='评论时间', auto_now_add=True)
    like_num = models.IntegerField(verbose_name='点赞数', default=0)
    like_users = models.TextField(verbose_name='点赞用户', null=True, blank=True, default=None)
    is_show = models.BooleanField(verbose_name='是否显示', default=True)

    class Meta:
        db_table = 'comment_book'
        verbose_name = '图书评论'
        verbose_name_plural = verbose_name