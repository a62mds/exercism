#!/usr/bin/env python
from datetime import datetime, timedelta

gigasecond = timedelta(seconds = 10**9)

def add_gigasecond(date):
    return date + gigasecond
