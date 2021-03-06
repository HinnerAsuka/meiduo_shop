from django.db import models
from utils.models import BaseModel


# Create your models here.


class OAuthQQUser(BaseModel):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='用户')
    openid = models.CharField(max_length=64, db_index=True, verbose_name='openid')

    class Meta:
        db_table = 'lg_oauth_qq'
        verbose_name = 'QQ用户登陆数据'
        verbose_name_plural = verbose_name
