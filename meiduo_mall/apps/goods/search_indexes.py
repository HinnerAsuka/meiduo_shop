from apps.goods.models import SKU
from haystack import indexes

"""
0. 我们需要在 模型所对应的 子应用中 创建 search_indexes.py 文件。以方便haystack来检索数据
1. 索引类必须继承自  indexes.SearchIndex, indexes.Indexable
2. 必须定义一个字段 document=True
    字段名 起什么都可以。 text只是惯例（大家习惯都这么做） 。
    所有的索引的 这个字段 都一致就行
3. use_template=True
    允许我们来单独设置一个文件，来指定哪些字段进行检索

    这个单独的文件创建在哪里呢？？？
    模板文件夹下/search/indexes/子应用名目录/模型类名小写_text.txt


 数据         <----------Haystack--------->             elasticsearch 

 运作： 我们应该让 haystack 将数据获取到 给es 来生成索引

    在虚拟环境下  python manage.py rebuild_index

"""

# 对SKU商品进行检索
class SKUIndex(indexes.SearchIndex, indexes.Indexable):  # 必须继承这两个类
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return SKU

    def index_queryset(self, using=None):
        # return SKU.objects.all()
        return self.get_model().objects.all()