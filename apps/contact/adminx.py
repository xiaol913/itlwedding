# _*_ coding=utf8 _*_
import xadmin

from .models import Contact


class ContactAdmin(object):
    model_icon = 'fa fa-tty'
    list_display = ['desc', ]
    list_editable = ['desc', ]
    style_fields = {
        "desc": "ueditor"
    }


xadmin.site.register(Contact, ContactAdmin)
