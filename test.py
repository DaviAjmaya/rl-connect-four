data = {
'date-time': {
    'date-time':0
}
}

def read_timetable(key_to_read):
    param = data['date-time']
    return param[key_to_read]

param_link = {
    'date_time': lambda: param['date_time']
}

print(param_link['date-time'])
