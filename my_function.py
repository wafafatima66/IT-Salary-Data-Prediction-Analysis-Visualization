def clean_country_name(x):
    if x ==  'United States of America':
        return 'United States'
    if x == 'United Kingdom of Great Britain and Northern Ireland':
        return 'United Kingdom'
    return x

def shorten_categories(categories, cutoff):
    categorical_map = {}
    for i in range(len(categories)):
        if categories.values[i] >= cutoff:
            categorical_map[categories.index[i]] = categories.index[i]
        else:
            categorical_map[categories.index[i]] = 'Other'
    return categorical_map

def clean_experience(x):
    if x ==  'More than 50 years':
        return 50
    if x == 'Less than 1 year':
        return 0.5
    return float(x)

def clean_education(x):
    if 'Bachelor’s degree' in x:
        return 'Bachelor’s degree'
    if 'Master’s degree' in x:
        return 'Master’s degree'
    if 'Professional degree' in x or 'Other doctoral' in x:
        return 'Post grad'
    return 'Less than a Bachelors'

def clean_experience_2018(x):
    if x ==  '3-5 years':
        return 4
    if x == '18-20 years':
        return 19
    if x == '6-8 years':
        return 7
    if x == '12-14 years':
        return 13
    if x == '0-2 years':
        return 1
    if x == '21-23 years':
        return 22
    if x == '24-26 years':
        return 25
    if x == '9-11 years':
        return 10
    if x == '15-17 years':
        return 16
    if x == '27-29 years':
        return 28
    if x == '30 or more years':
        return 50
    return float(x)