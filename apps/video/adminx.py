# -*- coding: utf-8 -*-
import xadmin
from .models import VideoInfo, VideoLabel


class VideoInfoAdmin(object):
    pass


class VideoLabelAdmin(object):
    pass


xadmin.site.register(VideoLabel, VideoLabelAdmin)
xadmin.site.register(VideoInfo, VideoInfoAdmin)