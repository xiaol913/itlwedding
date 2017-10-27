import xadmin
from xadmin import views
from .models import EnjoyLabel, EnjoyInfo, EnjoyInfoImage


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSetting(object):
    site_title = "爱塔罗海外婚礼"
    site_footer = "成都爱塔罗文化传媒有限公司"
    # menu_style = "accordion"


class EnjoyLabelAdmin(object):
    model_icon = 'fa fa-eercast'
    list_display = ['name', 'label', ]
    list_editable = ['label', ]


class EnjoyInfoAdmin(object):
    model_icon = 'fa fa-photo'
    list_display = ['title', 'desc', 'get_images_nums', 'add_time', ]
    list_editable = ['title', 'desc', ]
    ordering = ['add_time', ]
    search_fields = ['title', ]
    style_fields = {
        "enjoy_info": "ueditor"
    }

    class EnjoyInfoImageInline(object):
        model = EnjoyInfoImage
        exclude = ["add_time"]
        extra = 3

    inlines = [EnjoyInfoImageInline]


class EnjoyInfoImageAdmin(object):
    pass

xadmin.site.register(EnjoyLabel, EnjoyLabelAdmin)
xadmin.site.register(EnjoyInfo, EnjoyInfoAdmin)

xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)
