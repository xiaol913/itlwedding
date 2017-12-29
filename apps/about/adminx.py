# _*_ coding=utf8 _*_
import xadmin

from .models import About


class AboutAdmin(object):
    model_icon = 'fa fa-info-circle'
    list_display = ['desc', ]
    list_editable = ['desc', ]
    style_fields = {
        "desc": "ueditor"
    }


xadmin.site.register(About, AboutAdmin)
