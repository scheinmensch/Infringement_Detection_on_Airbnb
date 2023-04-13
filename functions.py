def license_duplicates(array):
    new_arr = []
    for license in array:
        if 'HUTB' in license:
            new_arr.append(license)
        elif 'HB' in license:
            new_arr.append(license)
        elif 'AJ' in license:
            new_arr.append(license)
    return new_arr

def is_valid_license(license):
    if license in license_duplicates:
        return 'reuse'
    if 'HUTB' in license:
        return 'ok'
    if 'HB' in license:
        return 'ok'
    if 'AJ' in license:
        return 'ok'
    elif 'exempt' in license.lower():
        return 'claims Exempt'
    else:
        return 'no license'
    
def multi_listings(listings):
    if listings == 1:
        return 'single listing'
    if listings > 1 and listings < 4:
        return '2-3 listings'
    if listings > 3 and listings < 6:
        return '4-5 listings'
    if listings > 5 and listings < 10:
        return '6-9 listings'
    if listings > 9 and listings < 20:
        return '10-19 listings'
    if listings > 19 and listings < 50:
        return '20-49 listings'
    if listings > 49:
        return '50 or more listings'