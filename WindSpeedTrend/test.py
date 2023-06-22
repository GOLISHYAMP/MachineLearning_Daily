import datetime

date = datetime.datetime(2012, 1, 1, tzinfo=datetime.timezone.utc)
unix_time = int(date.timestamp())

print(unix_time)
# 973332