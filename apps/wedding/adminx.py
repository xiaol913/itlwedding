# -*- coding: utf-8 -*-
import xadmin
from .models import WeddingArea, WeddingInfo, WeddingLabel, WeddingInfoImage


class WeddingAreaAdmin(object):
    pass


class WeddingInfoAdmin(object):
    style_fields = {
        "hotel_info": "ueditor",
        "place_info": "ueditor",
        "server_info": "ueditor",
        "book_info": "ueditor",
    }

    class WeddingInfoImageInline(object):
        model = WeddingInfoImage
        exclude = ["add_time"]
        extra = 12

    inlines = [WeddingInfoImageInline]


class WeddingLabelAdmin(object):
    pass


class WeddingInfoImageAdmin(object):
    pass

xadmin.site.register(WeddingArea, WeddingAreaAdmin)
xadmin.site.register(WeddingInfo, WeddingInfoAdmin)
xadmin.site.register(WeddingLabel, WeddingLabelAdmin)
# xadmin.site.register(WeddingInfoImage, WeddingInfoImageAdmin)
