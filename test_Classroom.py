def Test_Classroom():
    errors = 0
    try:
        import Classroom
    except:
        errors += 1
    try:
        classroom_016 = Classroom.Classroom('016', 80, ['PC', 'projector',\
                                                        'mic'])
        classroom_007 = Classroom.Classroom('007', 12, ['TV'])
    except:
        errors += 1
    try:
        classroom_016.number
        classroom_016.capacity
        classroom_016.equimpent
    except:
        errors += 1
    try:
        classroom_016.equipment_differences(classroom_007)
    except:
        errors += 1
    try:
        print(classroom_016)
    except:
        errors += 1
    try:
        [classroom_016]
    except:
        errors += 1
    return errors


print(Test_Classroom())
