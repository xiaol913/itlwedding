# _*_ coding=utf8 _*_
import xadmin

from .models import Know


class KnowAdmin(object):
    model_icon = 'fa fa-thumb-tack'
    list_display = ['label', 'desc', ]
    list_editable = ['label', 'desc', ]
    style_fields = {
        "desc": "ueditor"
    }


xadmin.site.register(Know, KnowAdmin)
