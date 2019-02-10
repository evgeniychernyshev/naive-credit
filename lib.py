def is_creditable(age, salary):
    # позитивный тест
    """
    >>> is_creditable(30, 40000)
    True

    >>> is_creditable(20, 40000)
    False

    >>> is_creditable(70, 40000)
    False

    >>> is_creditable(30, 10000)
    False
    """
    min_age = 21
    max_age = 60
    min_salary = 30000

    if age >= min_age and age < max_age and salary >= min_salary:
        return True
    else:
        return False

