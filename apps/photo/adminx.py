# -*- coding: utf-8 -*-
import xadmin
from .models import PhotoLabel, PhotoInfo, PhotoInfoImage


class PhotoLabelAdmin(object):
    model_icon = 'fa fa-camera'
    list_display = ['name', 'label', ]
    list_editable = ['label', ]


class PhotoInfoAdmin(object):
    model_icon = 'fa fa-newspaper-o'
    list_display = ['name', 'desc', 'get_images_nums', 'add_time', ]
    list_editable = ['name', 'desc', ]
    ordering = ['add_time', ]
    search_fields = ['name', ]
    style_fields = {
        "photo_info": "ueditor",
    }

    class PhotoInfoImageInline(object):
        model = PhotoInfoImage
        exclude = ["add_time"]
        extra = 3

    inlines = [PhotoInfoImageInline]


class PhotoInfoImageAdmin(object):
    pass

xadmin.site.register(PhotoLabel, PhotoLabelAdmin)
xadmin.site.register(PhotoInfo, PhotoInfoAdmin)
