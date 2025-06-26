from crum import get_current_request
from openedx.core.djangoapps.lang_pref import LANGUAGE_KEY
from openedx.core.djangoapps.user_api.preferences.api import set_user_preference

from .models import ExtraInfo


def set_acl_user_pref_lang_cookie(sender, **kwargs):
    user = kwargs.get("user")
    request = get_current_request()
    lang_code = ExtraInfo.objects.get(user=user).preferred_language
    set_user_preference(user, LANGUAGE_KEY, lang_code)
    request.COOKIES["openedx-language-preference"] = lang_code
    request._anonymous_user_cookie_lang = lang_code
