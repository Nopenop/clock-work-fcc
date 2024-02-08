def parse_minutes(minutes: int) -> tuple[int, int]:
  return (minutes // 60, minutes % 60)


def parse_hours(hours: int) -> tuple[int, int]:
  return (hours // 24, hours % 24)


def parse_days_to_hours(day: str) -> int:
  day_to_val = {
      "monday": 0,
      "tuesday": 1,
      "wednesday": 2,
      "thusday": 3,
      "friday": 4,
      "saturday": 5,
      "sunday": 6,
      "": 0
  }
  return day_to_val[day] * 24


def parse_val_to_time(hours_after: int, minutes_after: int) -> str:
  hours_in_day = str(hours_after%12)
  minutes_in_day = '{:02d}'.format(minutes_after)
  if hours_after % 24 == 0:
    return "12:" + minutes_in_day + " AM"
  elif hours_after % 24 > 12:
    return hours_in_day + ":"+ minutes_in_day + " PM"
  elif hours_after % 24 == 12:
    return "12:" + minutes_in_day + " PM"
  return hours_in_day + ":" + minutes_in_day + " AM"


def parse_day_int_to_string(days_after: int) -> str:
  val_to_day = [
      "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",
      "Sunday"
  ]
  return val_to_day[days_after % 7]


def parse_string_time(time: str,
                      am_or_pm: str = "AM",
                      day: str = "") -> tuple[int, int]:
  hours_from_days = parse_days_to_hours(day)
  hour_str = ""
  min_str = ""
  cur = ""
  for char in time:
    if char == ':':
      hour_str = cur
      cur = ""
      continue
    cur += char
  min_str = cur
  new_hour = int(hour_str)
  new_min = int(min_str)
  if am_or_pm == "PM":
    new_hour += 12

  return (new_hour + hours_from_days, new_min)


def add_time(start: str, time_added: str, day: str = "") -> str:
  hours_started, minutes_started = parse_string_time(start[0:-2], start[-2:],
                                                     day.lower())
  hours_added, minutes_added = parse_string_time(time_added)
  days_initial, _ = parse_hours(hours_started)
  hours_after, minutes_after = parse_minutes(minutes_started + minutes_added)
  days_after, hours_after = parse_hours(hours_after + hours_added +
                                        hours_started)
  difference = days_after - days_initial
  retString = ""
  retString += parse_val_to_time(hours_after, minutes_after)
  if day != "":
    retString += ", " + parse_day_int_to_string(days_after)
  if difference == 1:
    retString += " (next day)"
  if difference > 1:
    retString += f' ({difference} days later)'
  return retString
