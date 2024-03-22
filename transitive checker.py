def transitive(lst):
    for pair in lst:
        for comparison in lst:
            if pair[1] == comparison[0]:
                search = (pair[0], comparison[1])
                if search not in lst:
                    print(pair, comparison)
                    return False
    return True


r1 = [(1,2), (2,1)]
r2 = [(2,2), (2,3), (2,4), (3,2), (3,3), (3,4)]
r3 = [(1,1), (1,2), (2,1), (2,2), (3,3), (4,4)]
r4 = [(1,2), (2,3), (3,4)]
r5 = [(1,1), (2,2), (3,3), (4,4)]

