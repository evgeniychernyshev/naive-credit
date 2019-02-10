def is_creditable(age, salary):
    # позитивный тест
    """
    >>> is_creditable(30, 40000)
    True

    # негативные тесты
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

    if age < min_age:
        return False
    if age > max_age:
        return False
    if salary < min_salary:
        return False

    return True
