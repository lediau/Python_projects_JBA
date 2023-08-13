import json
import re
from collections import defaultdict
from datetime import datetime

EXPECTED_DATA = [
    ('bus_id', 'int', 1),
    ('stop_id', 'int', 1),
    ('stop_name', 'str', 1),
    ('next_stop', 'int', 1),
    ('stop_type', 'str', 0),
    ('a_time', 'str', 1)
]
EXPECTED_FORMAT = {
    'stop_name': re.compile("([A-Z][a-z]+ )+(Road|Avenue|Boulevard|Street)$"),
    'stop_type': re.compile("(S|O|F)?$"),
    'a_time': re.compile("([01][0-9]|2[0-4]):[0-5][0-9]$")
}
STOP_TYPES = {
    'S': 'Start',
    'T': 'Transfer',
    'F': 'Finish'
}

type_errors, format_errors = defaultdict(int), defaultdict(int)
lines, arrivals, buses_by_stops = defaultdict(list), defaultdict(list), defaultdict(list)
stops_by_type = defaultdict(set)
arrival_errors = []
on_demand_errors = set()
data = json.loads(input())


def type_validator(field, _type, required, payload):
    if field not in payload:
        return False
    if required and not str(payload[field]):
        return False
    if not isinstance(payload[field], eval(_type)):
        return False
    if field == 'stop_type' and len(payload[field]) > 1:
        return False
    return True


def format_validator(pattern, value):
    return pattern.match(value)


def lines_validator(lines):
    for line, stops in lines.items():
        if not ("S" in stops and "F" in stops):
            print("There is no start or end stop for the line", line)
            return False
    return True


def arrivals_validator(bus_id, stops, errors):
    last_stop_time = datetime.strptime("00:00", "%H:%M")
    for a_time, name in stops:
        a_time = datetime.strptime(a_time, "%H:%M")
        if last_stop_time > a_time:
            errors.append(f'bus_id line {bus_id}: wrong time on station {name}')
            break
        else:
            last_stop_time = a_time


for payload in data:
    lines[payload['bus_id']].append(payload['stop_type'])
    buses_by_stops[payload['stop_name']].append(payload['bus_id'])
    stops_by_type[payload['stop_type']].add(payload['stop_name'])
    arrivals[payload['bus_id']].append((payload['a_time'], payload['stop_name']))
    for field, _type, required in EXPECTED_DATA:
        if not type_validator(field, _type, required, payload):
            type_errors[field] += 1
        if field in EXPECTED_FORMAT:
            if not format_validator(EXPECTED_FORMAT[field], payload[field]):
                format_errors[field] += 1


print('Type and required field validation:', sum(type_errors.values()))
for field, *_ in EXPECTED_DATA:
    print(field, type_errors[field], sep=": ")

print('Format validation:', sum(format_errors.values()), 'errors')
for field in EXPECTED_FORMAT:
    print(field, format_errors[field], sep=": ")

print('Line names and number of stops:')
for line, stops in lines.items():
    print('bus_id:', line, 'stops:', len(stops))

if lines_validator(lines):
    stops_by_type['T'] = {
        stop_name for stop_name, bus_ids in
        buses_by_stops.items() if len(bus_ids) > 1
    }
    for sign, type_name in STOP_TYPES.items():
        on_demand_errors.update(stops_by_type['O'].intersection(stops_by_type[sign]))
        names = sorted(list(stops_by_type[sign]))
        print(f"{type_name} stops: {len(names)} {names}")

print('Arrival time test:')
for bus_id, stops in arrivals.items():
    arrivals_validator(bus_id, stops, arrival_errors)
if arrival_errors:
    print(*arrival_errors, sep='\n')
else:
    print('OK')

print('On demand stops test:')
if on_demand_errors:
    print(f'Wrong stop type: {sorted(list(on_demand_errors))}')
else:
    print('OK')
