
def convert_range(old_max, old_min, new_max, new_min, old_value):
    old_range = (old_max - old_min)  
    new_range = (new_max - new_min)  
    new_val = (((old_value - old_min) * new_range) / old_range) + new_min
    if new_val < new_min:
        return new_min
    
    if new_val > new_max:
        return new_max
    
    return new_val