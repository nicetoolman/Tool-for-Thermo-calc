def find_elements_from_filename(filename):    
    filename = filename.split()[0].split('-')
    element1 = filename[0]
    element2 = filename[1]    
    return element1, element2
