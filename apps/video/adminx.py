# -*- coding: utf-8 -*-
import xadmin
from .models import VideoInfo, VideoLabel


class VideoInfoAdmin(object):
    model_icon = 'fa fa-video-camera'
    list_display = ['title', 'video_url', 'go_to', 'add_time', ]
    list_editable = ['title', 'video_url', ]
    search_fields = ['title', 'video_url', ]
    ordering = ['add_time', ]
    import_excel = True


class VideoLabelAdmin(object):
    model_icon = 'fa fa-television'
    list_display = ['name', 'label', ]
    list_editable = ['label', ]


xadmin.site.register(VideoLabel, VideoLabelAdmin)
xadmin.site.register(VideoInfo, VideoInfoAdmin)
