def compare_sets(set1, set2, onlyNum=True):
    """
    Compare two sets and return the unique elements in each set as well as their intersection.
    Note: All elements are converted to the string

    Parameters:
    set1 (set or iterable): The first input set or iterable.
    set2 (set or iterable): The second input set or iterable.
    onlyNum (bool, optional): If True, returns only the counts of each part instead of the actual elements.
                              Defaults to False.

    Returns:
    dict: A dictionary containing the following keys:
        - 'only_in_set1': Elements present in set1 but not in set2 (as a comma-separated string if not onlyNum).
        - 'intersection': Elements present in both sets (as a comma-separated string if not onlyNum).
        - 'only_in_set2': Elements present in set2 but not in set1 (as a comma-separated string if not onlyNum).
        - If onlyNum is True, these values are replaced with their respective counts (e.g., 'only_in_set1_count').
    """
    s1 = set([str(x) for x in set1])
    s2 = set([str(x) for x in set2])

    # Calculate three core parts: unique to set1, intersection, and unique to set2
    unique_to_set1 = s1 - s2
    intersection = s1 & s2
    unique_to_set2 = s2 - s1

    # Return result based on onlyNum flag
    if onlyNum:
        return {
            "only_in_set1_count": len(unique_to_set1),
            "intersection_count": len(intersection),
            "only_in_set2_count": len(unique_to_set2)
        }
    else:
        return {
            "only_in_set1": ", ".join(sorted(unique_to_set1)),
            "intersection": ", ".join(sorted(intersection)),
            "only_in_set2": ", ".join(sorted(unique_to_set2))
        }


