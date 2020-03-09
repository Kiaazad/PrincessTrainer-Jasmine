init python:
    class inventory:
        def __init__(self, cash, items, markup):
            self.cash = cash
            self.bags = [bag("Bag", 10), bag("Person", 5)]
            self.togos = bag("To Go", 5)
            self.sum = 0
            if items:
                for i in items:
                    self.bags[0].add(i[0], i[1])

            self.markup = markup

            self.uniqueID = []
            self.holding = None
        def discard(self):
            self.holding = None

        def sumit(self):
            sum = 0
            for i in self.togos.items:
                if i is not None:
                    sum += i.item.val*i.qtt
            self.sum = sum
            return sum

        def has(self, x):
            if not isinstance(x, list):
                x = [x]
            for t in x:
                for i in self.bags:
                    for ii in i.items:
                        if ii is not None:
                            if ii.item == t:
                                return True
            else:
                return False

        def gotcash(self, a, u):
            if u and u in self.uniqueID:
                pass
            else:
                self.cash += a
        def paidcash(self, a):
            self.cash -= a

        def togos_collect(self):
            for i in self.togos.items:
                if i:
                    self.got(i.item, i.qtt)
            self.togos.clear()
        def got(self, item, quantity, uniqueID = None):
            if uniqueID and uniqueID in self.uniqueID:
                pass
            elif len(self.bags) == 0:
                msg.msg("You have no bags.")
            else:
                for i in self.bags:
                    if i.add(item,quantity):
                        msg.msg("You have got {} {}".format(quantity, item.name))
                        self.uniqueID.append(uniqueID)
                        break
                else:
                    msg.msg("Bags are full.")

        def drop(self, x, q):
            if len(self.bags):
                self.bags[0].rem(x, q)
                msg.msg("You have dropped {} {}".format(q, x.name))