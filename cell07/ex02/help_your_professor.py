def average(grades_dict):
    """Calculates and returns the average score from the dictionary of student grades."""
    if not grades_dict:
        return 0
    return sum(grades_dict.values()) / len(grades_dict)


class_3B = {
    "marine": 18,
    "jean": 15,
    "coline": 8,
    "luc": 9
}

class_3C = {
    "quentin": 17,
    "julie": 15,
    "marc": 8,
    "stephanie": 13
}


print(f"Average for class 3B: {average(class_3B)}.")
print(f"Average for class 3C: {average(class_3C)}.")