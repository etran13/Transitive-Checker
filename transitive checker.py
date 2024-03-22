def transitive(lst):
    for pair in lst:
        for comparison in lst:
            if pair[1] == comparison[0]:
                search = (pair[0], comparison[1])
                if search not in lst:
                    print(pair, comparison)
                    return False
    return True




