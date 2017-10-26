# -*- coding: utf-8 -*-
import xadmin
from .models import PhotoLabel, PhotoInfo, PhotoInfoImage


class PhotoLabelAdmin(object):
    pass


class PhotoInfoAdmin(object):
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
# xadmin.site.register(PhotoInfoImage, PhotoInfoImageAdmin)
