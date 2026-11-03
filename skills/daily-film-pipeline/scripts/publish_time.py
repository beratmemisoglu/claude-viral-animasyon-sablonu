"""Prints the publishAt timestamp (UTC, RFC 3339) for today's film: 17:00 Europe/London (owner decision 2026-10-15).
DST-safe (BST/GMT). If 17:00 UK today is less than 20 minutes away or already past, prints now + 20 min (UTC)
and a note on stderr, so the film still goes out today.
usage: python3 publish_time.py [--hour 17]
"""
import argparse, datetime as dt, sys
from zoneinfo import ZoneInfo

ap = argparse.ArgumentParser(); ap.add_argument('--hour', type=int, default=17); a = ap.parse_args()
uk = ZoneInfo('Europe/London')
now = dt.datetime.now(dt.timezone.utc)
target = dt.datetime.now(uk).replace(hour=a.hour, minute=0, second=0, microsecond=0).astimezone(dt.timezone.utc)
if target - now < dt.timedelta(minutes=20):
    target = (now + dt.timedelta(minutes=20)).replace(second=0, microsecond=0)
    print(f'note: {a.hour}:00 UK already passed or too close; publishing at {target.astimezone(uk):%H:%M} UK', file=sys.stderr)
print(target.strftime('%Y-%m-%dT%H:%M:%SZ'))
