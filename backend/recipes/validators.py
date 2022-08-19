import re
from django.core.exceptions import ValidationError
 
def validate_tag_color(value):
    match = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', value)
    if not match:
        raise ValidationError('Цвет должен передаваться в HEX-формате')
    return value