init python:
    class inventory:
        def __init__(self, cash, items, markup):
            self.cash = cash
            self.bags = [bag("All")]
            if items:
                for i in items:
                    self.bags[0].add(i[0], i[1])

            self.markup = markup

            self.uniqueID = []

        def gotcash(self, a, u):
            if u and u in self.uniqueID:
                pass
            else:
                self.cash += a

        def paidcash(self, a):
            self.cash -= a

        def got(self, x, q, u = None): # x = item, q = Quantity, u = Unique ID
            if u and u in self.uniqueID:
                pass
            else:
                if len(self.bags):
                    self.bags[0].add(x, q)
                    self.uniqueID.append(u)
                    msg.msg("You have got {} of {}".format(q, x.name))

        def drop(self, x, q):
            if len(self.bags):
                self.bags[0].rem(x, q)
                msg.msg("You have dropped {} of {}".format(q, x.name))