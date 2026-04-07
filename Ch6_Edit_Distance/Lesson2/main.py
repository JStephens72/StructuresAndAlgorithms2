def edit_distance(str1, str2):
    if str1 == "":
        return len(str2)

    if str2 == "":
        return len(str1)

    if str1[-1] == str2[-1]:
        return edit_distance(str1[:-1], str2[:-1])

    return (
        1
        + min(
            edit_distance(str1, str2[:-1]),  # insert
            edit_distance(str1[:-1], str2),  # delete
            edit_distance(str1[:-1], str2[:-1]),  # substitute
        )
    )
