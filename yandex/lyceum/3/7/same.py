def same_by(characteristic, objects):
    if not objects:
        return True
    sample = characteristic(objects[0])
    for e in map(characteristic, objects):
        if e != sample:
            return False
    return True
