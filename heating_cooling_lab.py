def heating_cooling(actual_temp, desired_temp):
    if actual_temp > desired_temp:
        print('Running A/C')
        while actual_temp > desired_temp:
            actual_temp = actual_temp - 1
            print(f'Temperature is now {actual_temp}.')
    elif actual_temp < desired_temp:
        print('Running heat')
        while actual_temp < desired_temp:
            actual_temp = actual_temp + 1
            print(f'Temperature is now {actual_temp}.')
    else:
        print('Standby')

def convert_temp(temp_celsius, target_unit):
    converted_temp = ((temp_celsius + 273.15) if target_unit.upper() == 'K'
                       else ((temp_celsius * 1.8) + 32) if target_unit.upper() == 'F'
                       else temp_celsius)
    return converted_temp

heating_cooling(46, 60)
print(convert_temp(27, 'F'))
