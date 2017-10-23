import xadmin
from xadmin import views
from .models import EnjoyLabel


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSetting(object):
    site_title = "Itlwedding"
    site_footer = "iiiiiii"
    menu_style = "accordion"


class EnjoyLabelAdmin(object):
    pass


xadmin.site.register(EnjoyLabel, EnjoyLabelAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)