def find_references(text):
    words = text.split()
    
    refs = []
    for word in words:
        if word[0] == "[" and word[-1] == "]":
            reference = word[1:-1]
            reference_number = int(reference)
            refs.append(reference_number)
    
    return refs
