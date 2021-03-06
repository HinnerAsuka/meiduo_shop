from django.urls import path
from apps.goods.views import IndexView, ListView, HotListView, SKUSearchView, DetailView, CategoryVisitCountView

urlpatterns = [
    # 商城首页
    path('index/', IndexView.as_view()),
    # 商品分类列表
    path('list/<category_id>/skus/', ListView.as_view()),
    # 热销商品列表
    path('hot/<category_id>/', HotListView.as_view()),
    # 搜索商品
    path('search/', SKUSearchView()),
    # 详情页面
    path('detail/<sku_id>', DetailView.as_view()),
    # 分类商品浏览统计
    path('detail/visit/<category_id>/', CategoryVisitCountView.as_view())
]