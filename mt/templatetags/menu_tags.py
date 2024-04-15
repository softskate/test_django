from django import template
from mt.models import MenuItem

register = template.Library()

@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    current_url = context['request'].path
    menu_items = MenuItem.objects.filter(menu_name=menu_name, parent=None)
    active_item = get_active_item(menu_items, current_url)
    print(menu_items)
    return render_menu(menu_items, active_item)

def get_active_item(menu_items, current_url):
    for item in menu_items:
        if item.get_absolute_url() == current_url:
            return item
        active_child = get_active_item(item.children.all(), current_url)
        if active_child:
            return active_child
    return None

def render_menu(menu_items, active_item, level=0):
    output = ""
    for item in menu_items:
        is_active = item == active_item or active_item in item.get_descendants(include_self=True)
        output += f"<li class={'active' if is_active else ''}>"
        output += f"<a href='{item.get_absolute_url()}'>{item.name}</a>"
        if item.children.exists():
            output += "<ul>" + render_menu(item.children.all(), active_item, level+1) + "</ul>"
        output += "</li>"
    return output