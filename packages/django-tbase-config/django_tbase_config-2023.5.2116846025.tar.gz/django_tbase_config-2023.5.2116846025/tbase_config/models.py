from django.db import models
from django.contrib import admin
# Create your models here.
from solo.models import SingletonModel


class General(SingletonModel):
    """
    配置页面
    """
    site_title = models.CharField("Site Title",
                                  max_length=255,
                                  default='',
                                  null=True,
                                  blank=True)
    tagline = models.CharField("Tagline",
                               max_length=255,
                               default='',
                               null=True,
                               blank=True)
    index_title = models.CharField("Home Title",
                                   max_length=255,
                                   default='',
                                   null=True,
                                   blank=True)
    site_url = models.URLField("Site Address (URL)",max_length=255, default='', null=True, blank=True)
    enable_nav_sidebar = models.BooleanField(
        default=admin.AdminSite.enable_nav_sidebar)

    copyright = models.CharField("copyright",
                                 max_length=255,
                                 default='',
                                 null=True,
                                 blank=True)


    maintenance_mode = models.BooleanField("维护模式", default=False)
    admin_email = models.EmailField("Administration Email Address",
                                    max_length=32,
                                    null=True,
                                    blank=True)
    # DEBUG = models.BooleanField(default=False)
    header_script = models.TextField("在header部添加的全局代码html，js，css等等",
                                     blank=True)
    footer_script = models.TextField("在尾部添加的全局代码html，js，css等等", blank=True)

    api_thumbnail = models.CharField(
        "thumbnail api host",
        max_length=255,
        null=True,
        blank=True,
        default=None,
        help_text="thumbnail api host https://fast.maomihezi.com/")
    analytics_id = models.CharField(" Google分析",
                                    max_length=32,
                                    null=True,
                                    blank=True,
                                    default=None,
                                    help_text="G-3E8MSDBwww")

    def __str__(self):
        return "General Settings"

    class Meta:
        verbose_name = "General Settings"
