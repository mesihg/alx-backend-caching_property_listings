from django_redis import get_redis_connection
import logging



logger = logging.getLogger(__name__)

def get_all_properties():
    from django.core.cache import cache
    from .models import Property
    properties = cache.get('all_properties')
    if not properties:
        properties = list(Property.objects.all())
        cache.set('all_properties', properties, 3600)  # cache for 1 hour
    return properties