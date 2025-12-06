from django import template
from bs4 import BeautifulSoup

register = template.Library()

@register.filter(name='strip_spans_and_marks')
def strip_spans_and_marks(value):
    """
    <span> (inline styles सहित) और <mark class="marker-..."> को हटाकर
    साफ़ टेक्स्ट/HTML लौटाता है.
    """
    if not value:
        return value
    try:
        soup = BeautifulSoup(value, "html.parser")

        # <mark> unwrap
        for mk in soup.find_all("mark"):
            mk.unwrap()

        # <span> unwrap
        for sp in soup.find_all("span"):
            sp.unwrap()

        # किसी भी टैग के inline style हटाओ
        for tag in soup.find_all(True):
            tag.attrs.pop("style", None)

        # पुराना <font> भी unwrap कर दो (सुरक्षा हेतु)
        for ft in soup.find_all("font"):
            ft.unwrap()

        return str(soup)
    except Exception:
        return value
