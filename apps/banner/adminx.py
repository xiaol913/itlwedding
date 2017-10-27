# -*- coding: utf-8 -*-
import xadmin

from .models import Banner


class BannerAdmin(object):
    pass


xadmin.site.register(Banner, BannerAdmin)
