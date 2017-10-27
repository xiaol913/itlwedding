# -*- coding: utf-8 -*-
import xadmin

from .models import Banner


class BannerAdmin(object):
    model_icon = 'fa fa-object-group'
    list_display = ['title', 'label', 'add_time', ]
    list_editable = ['title', 'label', ]


xadmin.site.register(Banner, BannerAdmin)
