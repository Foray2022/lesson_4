from sys import argv

script, output_hours, rate_per_hour, bonus = argv

try:
    output_hours, rate_per_hour, bonus = map(float, argv[1:])
    salary = output_hours * rate_per_hour + bonus
    print(f'staff salary:,{salary}')
except TypeError:
    print('incorrect value type')
