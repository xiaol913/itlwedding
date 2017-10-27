# -*- coding: utf-8 -*-
import xadmin
from .models import WeddingArea, WeddingInfo, WeddingLabel, WeddingInfoImage


class WeddingAreaAdmin(object):
    model_icon = 'fa fa-location-arrow'
    list_display = ['name', 'desc', 'add_time', ]
    list_editable = ['name', 'desc', ]


class WeddingInfoAdmin(object):
    model_icon = 'fa fa-bars'
    list_display = ['name', 'area_id', 'desc', 'get_images_nums', 'add_time', ]
    list_editable = ['name', 'desc', ]
    search_fields = ['name', ]
    list_filter = ['area_id', ]
    ordering = ['add_time', ]
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
    model_icon = 'fa fa-venus-mars'
    list_display = ['name', 'label', ]
    list_editable = ['label', ]


class WeddingInfoImageAdmin(object):
    pass


xadmin.site.register(WeddingLabel, WeddingLabelAdmin)
xadmin.site.register(WeddingArea, WeddingAreaAdmin)
xadmin.site.register(WeddingInfo, WeddingInfoAdmin)
