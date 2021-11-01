
init python:
    def drop_loot(table):
        sum1 = 0
        for i in table:
            sum1 += i[1]
        r = renpy.random.ranint(1,sum)
        sum2 = 0
        for i in table:
            sum2 += i[1]
            if r < sum2:
                return i[0]

    def drop_more(table, n):
        loot = []
        for i in range(n):
            item = drop_loot(table)
            if not item == None:
                loot.append(item)
        return loot

# default test_loot_table = [
#     [big_fish, 12],
#     [shoe, 4],
#     [small_fish, 24]
# ]