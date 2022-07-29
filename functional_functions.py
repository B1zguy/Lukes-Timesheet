import collections
from datetime import datetime, timedelta
import pytz
### currently scratchpad until I move it across to the bot

# '%Y-%m-%d %H:%M:%S'
datetime_Format = '%a %d %b %H:%M'

def extractor (Call_shifts):
    extracted_Shifts = []
    #next_Shifts = collections.defaultdict(list)
    for i in Call_shifts:
        next_Shifts = collections.defaultdict(list)

        start = epoch_Converter(i['start'])
        finish = epoch_Converter(i['finish'])

        next_Shifts['begin'].append(start)
        next_Shifts['end'].append(finish)
        extracted_Shifts.append(dict(next_Shifts))
        #next_Shifts.clear()

    #extracted_Shifts = defaultdict_Converter(extracted_Shifts)

    return extracted_Shifts
# Keeping for now
'''def defaultdict_Converter(ddict):
    for i in ddict:
        dict(ddict[i])
    return ddict'''
'''def ddict2dict(d):
    for k, v in d.items():
        if isinstance(v, dict):
            d[k] = ddict2dict(v)
    return dict(d)'''



'''def epoch_Converte2r(time):
    # converted_Time = datetime.fromtimestamp(time).strftime(datetime_Format)
    converted_Time = datetime.fromtimestamp(time)

    # Timezoning
    Zone = pytz.timezone('Australia/Perth')
    utc = pytz.utc
    Perth_Time = utc.localize(converted_Time).astimezone(Zone).strftime(datetime_Format)

    return Perth_Time'''

def epoch_Converter(time):
    Zone = pytz.timezone('Australia/Melbourne')
    converted_Time = datetime.fromtimestamp(time, Zone).strftime(datetime_Format)

    return converted_Time



datetime_object = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')

def next_7(id):
    day_Format = '%d %b %y'
    #today = datetime.today().replace(microsecond=0,second=0,minute=0)-timedelta(hours=1)
    today = datetime.today().date()
    #.strftime(datetime_Format)
    #print(type(today))
    week = today + timedelta(days=7)

    input_Obj = {
        'user_id': id,
        'from': today.strftime(datetime_Format),
        'to': week.strftime(datetime_Format)
    }
   ## print('==-====', today, week)
    return input_Obj