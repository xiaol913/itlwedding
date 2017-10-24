# -*- coding: utf-8 -*-
import xadmin
from .models import WeddingArea, WeddingInfo, WeddingLabel


class WeddingAreaAdmin(object):
    pass


class WeddingInfoAdmin(object):
    style_fields = {
        "hotel_info": "ueditor",
        "place_info": "ueditor",
        "server_info": "ueditor",
        "book_info": "ueditor",
    }


class WeddingLabelAdmin(object):
    pass


xadmin.site.register(WeddingArea, WeddingAreaAdmin)
xadmin.site.register(WeddingInfo, WeddingInfoAdmin)
xadmin.site.register(WeddingLabel, WeddingLabelAdmin)