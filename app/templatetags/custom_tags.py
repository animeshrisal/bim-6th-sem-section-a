from django import template

register = template.Library()

def get_yen(movie):
    return movie.get_yen()

register.filter('yen_equivalent', get_yen)