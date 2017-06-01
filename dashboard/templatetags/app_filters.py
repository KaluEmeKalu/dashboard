from django import template
import json
from django.utils.safestring import mark_safe




register = template.Library()

# from ..models import Video


# from django.conf import settings
# try:
#     from django.contrib.auth import get_user_model
#     User = settings.AUTH_USER_MODEL
# except ImportError:
#     from django.contrib.auth.models import User

@register.filter
def to_char(value):
    return chr(96 + value)


@register.filter(is_safe=True)
def js(obj):
    return mark_safe(json.dumps(obj))



@register.simple_tag
def is_watched(video_id, user_id):
    """
    Tells if a video is watched
    """

    video = Video.objects.get(video_id)
    user = User.objects.get(user_id)

    completed_video = CompletedVideo.objects.filter(
        user=user, video=video)

    if len(completed_video) > 0:
        return "checked"
    else:
        return ""