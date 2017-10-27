import xadmin
from xadmin import views
from .models import EnjoyLabel, EnjoyInfo, EnjoyInfoImage


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSetting(object):
    site_title = "Itlwedding"
    site_footer = "iiiiiii"
    menu_style = "accordion"


class EnjoyLabelAdmin(object):
    pass


class EnjoyInfoAdmin(object):
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
