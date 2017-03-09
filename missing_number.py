def find_missing(array1,array2):
    """method to create missing number"""

    if array1 == array2:

        return 0

    elif array1 != array2:

        set_a = set(array1)

        set_b = set(array2)

        check_missing = set_a^set_b

        return list(check_missing)[0]

find_missing([1, 2], [1, 2, 5] )