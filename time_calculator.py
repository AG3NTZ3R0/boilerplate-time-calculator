import re

def add_time(start, duration, dow=""):
  """Add the duration time to the start time."""
  start_re = re.split(':', start)
  start_hours = int(start_re[0])
  start_re = re.split(' ', start_re[1])
  start_minutes = int(start_re[0])
  start_period = start_re[1]

  duration_re = re.split(':', duration)
  duration_hours = int(duration_re[0])
  duration_minutes = int(duration_re[1])

  final_hours = start_hours + duration_hours
  final_minutes = start_minutes + duration_minutes
  final_period = start_period
  final_dow = dow

  period = ['AM', 'PM']
  dow_lst = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
  day_add_count = 0

  while final_minutes >= 60:
    final_hours += 1
    final_minutes -= 60
  
  if final_minutes < 10:
    final_minutes = "0" + str(final_minutes)
  while final_hours > 12:
    day_add_count += 0.5
    final_hours -= 12
  if day_add_count % 1 != 0:
      if final_period == period[0]:
        final_period = period[1]
      elif final_period == period[1]:
        final_period = period[0]
  if final_hours == 12:
      if final_period == period[0]:
        final_period = period[1]
        days_added = day_add_count - 1
      elif final_period == period[1]:
        final_period = period[0]
        days_added = day_add_count + 1
  if final_hours != 12:
    days_added = day_add_count
  
  days_added_str = str(int(round(days_added, 0)))
  
  if dow:
    for index, value in enumerate(dow_lst):
      if value.lower() == dow.lower():
        if final_hours == 12:
          day_add_count += index + 1
        elif final_hours != 12:
          day_add_count += index
        while day_add_count > 7:
          day_add_count -= 7
        if day_add_count == 7:
          day_add_count = 0
        if day_add_count % 1 != 0:
          day_add_count += 1
        day_add_count = int(day_add_count)
        final_dow = dow_lst[day_add_count]
        break
    if (days_added == 1 and final_period == start_period) or (days_added == 0.5 and start_period == period[1]):
      new_time = str(final_hours) + ":" + str(final_minutes) + " " + final_period + ", " + final_dow + " (next day)"
    elif days_added > 0.5:
      new_time = str(final_hours) + ":" + str(final_minutes) + " " + final_period + ", " + final_dow + " (" + days_added_str + " days later)"
    else:
      new_time = str(final_hours) + ":" + str(final_minutes) + " " + final_period + ", " + final_dow
  else:
    if (days_added == 1 and final_period == start_period) or (days_added == 0.5 and start_period == period[1]):
      new_time = str(final_hours) + ":" + str(final_minutes) + " " + final_period + " (next day)"
    elif days_added > 0.5:
      new_time = str(final_hours) + ":" + str(final_minutes) + " " + final_period + " (" + days_added_str + " days later)"
    else:
      new_time = str(final_hours) + ":" + str(final_minutes) + " " + final_period

  return new_time
