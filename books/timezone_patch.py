from datetime import tzinfo, timedelta
from django.utils import timezone

class DummyUTC(tzinfo):
    def utcoffset(self, dt): return timedelta(0)
    def dst(self, dt): return timedelta(0)
    def tzname(self, dt): return "UTC"

timezone.get_default_timezone = lambda: DummyUTC()
timezone.get_current_timezone = lambda: DummyUTC()
