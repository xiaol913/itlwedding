# -*- coding: utf-8 -*-
import xadmin
from .models import PhotoLabel, PhotoInfo


class PhotoLabelAdmin(object):
    pass


class PhotoInfoAdmin(object):
    style_fields = {
        "photo_info": "ueditor",
    }


xadmin.site.register(PhotoLabel, PhotoLabelAdmin)
xadmin.site.register(PhotoInfo, PhotoInfoAdmin)