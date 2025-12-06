from django import template
import re
from datetime import timedelta, datetime

register = template.Library()

@register.filter
def is_not_empty(value):
    """ Returns True only if actual content exists (ignores tags, spaces, &nbsp;) """
    if not value:
        return False
    cleaned = re.sub(r'<[^>]*>', '', value)  # remove HTML tags
    cleaned = cleaned.replace("&nbsp;", "").strip()
    return bool(cleaned)


@register.filter
def add_days(value, days):
    if not value:
        return None

    # Ensure datetime object + timezone handle
    if hasattr(value, 'tzinfo') and value.tzinfo is None:
        value = value.replace(tzinfo=datetime.now().astimezone().tzinfo)

    return value + timedelta(days=int(days))

