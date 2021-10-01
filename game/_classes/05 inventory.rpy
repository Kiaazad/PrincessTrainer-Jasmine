init python:
    class inventory:
        def __init__(self, cash, items, markup):
            self.cash = cash
            self.bags = [bag("Bag", 12), bag("Person", 5)]
            self.togos = bag("To Go", 5)
            self.sum = 0

            if items:
                for i in items:
                    self.bags[0].add(i[0], i[1])

            self.markup = markup

            self.uniqueID = []
            self.holding = None
            self.selected = self.bags[0]
            
            self.pick_pocket_skill = 0
            self.pick_pocket_alert = 0

            self.bag_x = 0
        def dragged(self, drags, drop):
            self.bag_x = drags[0].x
            renpy.restart_interaction()


        def change(self, slot):
            self.selected = slot
        def pick_pocket(self, target):
            amount = renpy.random.randint(0, target.cash)
            chance = renpy.random.randint(0,100)
            fail = renpy.random.randint(0,100)
            if fail > self.pick_pocket_skill:
                if target == hero:
                    msg.msg(_("You felt something fishy is going on."))
                else:
                    msg.msg(target.name + _(" felt something fishy is going on."))
                    if self.pick_pocket_skill < target.pick_pocket_alert:
                        msg.msg(target.name + _(" Caught you."))
                        # Trigger a fight

                target.pick_pocket_alert += 1

            if chance < self.pick_pocket_skill:
                target.cash -= amount
                self.cash += amount
                if self == hero:
                    msg.msg("You've picked {} from {}'s pocket.".format(amount, target.name))
            else:
                if self == hero:
                    msg.msg("You've failed to pick {}'s pocket.".format(target.name))

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

        def gotcash(self, a, u = None):
            if u and u in self.uniqueID:
                pass
            else:
                self.cash += a
                msg.msg("{} got {} dinars.".format(self.name, a))
        def paidcash(self, a):
            self.cash -= a

        def togos_collect(self):
            for i in self.togos.items:
                if i:
                    self.got(i.item, i.qtt)
            self.togos.clear()
        def got(self, item, quantity = 1, uniqueID = None):
            if uniqueID and uniqueID in self.uniqueID:
                pass
            elif len(self.bags) == 0:
                msg.msg("{} have no bags.".format(self.name))
            else:
                for i in self.bags:
                    if i.add(item,quantity):
                        msg.msg("{} got {} {}".format(self.name, quantity, item.name))
                        self.uniqueID.append(uniqueID)
                        break
                else:
                    msg.msg("Bags are full.")

        def drop(self, x, q, a = True):
            if len(self.bags):
                self.bags[0].rem(x, q)
                if a:
                    msg.msg("{} have dropped {} {}".format(self.name, q, x.name))
        def sell(self, x, q, buyer, price):
            if len(self.bags):
                self.bags[0].rem(x, q)
                buyer.got(x,q)
                buyer.cash -= price
                self.cash += price
                msg.msg("You have sold {} of {} to {} for {}".format(q, x.name, buyer.name, price))


