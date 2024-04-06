from decimal import Decimal
from django import template

register = template.Library()


@register.filter(name="dms")
def decimal_to_dms(decimal_coord):
    if decimal_coord is None:
        return ""
    if decimal_coord >= 0:
        direction = "N"
    else:
        direction = "S"
    abs_coord = abs(decimal_coord)

    degrees = int(abs_coord)
    minutes = int((abs_coord - degrees) * 60)
    seconds = (abs_coord - Decimal(degrees) - Decimal(minutes) / Decimal(60)) * Decimal(3600)
    return f"{degrees}°{minutes}'{seconds:.2f}\"{direction}"
