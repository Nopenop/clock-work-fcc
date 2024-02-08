
from numpy import diff


def total_add(start_hours:int, hours_added:int, start_minutes:int, minutes_added:int, start_day:int) -> tuple[int, int]:
    start_hours+= hours_added + start_day * 24
    start_minutes += minutes_added
    return (start_hours, start_minutes)


def string_to_time(time:str)->tuple[int,int]:
    new_hour = 0
    new_minutes = 0
    cur_string = ""
    for char in time:
        if char == ':':
            new_hour = int(cur_string)
            cur_string = ""
            continue
        cur_string+= char
    new_minutes = int(cur_string)
    return (new_hour, new_minutes)



def time_to_string(new_hours:int, new_minutes:int, day:str="")->str:
    num_to_day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    ret_string = ""
    ret_string += str(new_hours%12 + new_minutes//60) + ":" + "{:02d}".format(new_minutes%60)
    day_to_num = {
        'monday': 0,
        'tuesday': 1,
        'wednesday': 2,
        'thursday': 3,
        'friday': 4,
        'saturday': 5, 
        'sunday': 6,
        '': 0
    }
    if (new_hours%24)//12== 1 and new_hours%24 == 1:
        ret_string += " PM"
    else:
        ret_string += " AM"
    if day != "" or new_hours//24 > 0:
        difference = (new_hours + new_minutes//60)//24 - day_to_num[day.lower()] 
        if day == "":
            if difference == 1:
                ret_string += " (next day)"
            else:
                ret_string += f'({difference} days later)'
        else:
            if difference == 1:
                ret_string += f' {num_to_day[(day_to_num[day.lower()] + difference)%7]} (next day)'
            else:
                ret_string += f' {num_to_day[(day_to_num[day.lower()] + difference)%7]} ({difference} days later)'
    return ret_string

def add_time(start, duration, day = ""):
    day_to_num = {
        'monday': 0,
        'tuesday': 1,
        'wednesday': 2,
        'thursday': 3,
        'friday': 4,
        'saturday': 5, 
        'sunday': 6,
        '': 0
    }
    am_pm  = start[-2:]
    # print(start[0:-2])
    start_hours,start_minutes = string_to_time(start[0:-2])
    print(am_pm)
    if am_pm == "PM" and start != 12:
        start_hours += 12
    hours_added,minutes_added = string_to_time(duration)
    new_hours, new_minutes = total_add(start_hours, hours_added, start_minutes, minutes_added, day_to_num[day.lower()])

    return time_to_string(new_hours, new_minutes, day)

print(add_time("11:59 PM", "24:05", "Wednesday"))