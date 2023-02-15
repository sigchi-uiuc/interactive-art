
def convert_range(old_max, old_min, new_max, new_min, old_value):
    old_range = (old_max - old_min)  
    new_range = (new_max - new_min)  
    new_val = (((old_value - old_min) * new_range) / old_range) + new_min

    if new_val < new_min:
        return_val = new_min
    elif new_val > new_max:
        return_val = new_max
    else:
        return_val = new_val
    
    return int(return_val)