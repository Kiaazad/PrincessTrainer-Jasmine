init python:
    class bag:
        def __init__(self, name, slots = 10, items = []):
            self.name = name
            self.slots = slots
            self.clear()
            if items:
                for ii,i in enumerate(items):
                    self.add(i[0], i[1])
        def shuffle(self):
            renpy.random.shuffle(self.items)
        def clear(self):
            self.items = [None]* self.slots
        def add(self, item, quantity):
            for i in self.items:
                if i and i.item == item:
                    i.qtt += quantity
                    return True
            else:
                for ii,i in enumerate(self.items):
                    if i == None:
                        self.items[ii] = stack(item, quantity)
                        return True
                else:
                    return False
        def rem(self, item, quantity):
            for n,i in enumerate(self.items):
                if i and i.item == item:
                    if i.qtt > quantity:
                        i.qtt -= quantity
                        return True
                    elif i.qtt == quantity:
                        self.items[n] = None
                        return True
                    else:
                        return False
            else:
                return False

        def stack(self):
            pass

        def swap(self, slot, who):
            r = self.items[slot]
            self.items[slot] = who.holding
            who.holding = r
        def pick(self, slot, who):
            if who.holding and self.items[slot]:
                if self.items[slot].item == who.holding.item:
                    self.items[slot].qtt += who.holding.qtt
                    who.holding = None
                else:
                    self.swap(slot, who)
            else:
                self.swap(slot, who)
        def pickOne(self, slot, who):
            if self.items[slot] == None:
                self.pick(slot, who)
            elif  who.holding == None or self.items[slot].item == who.holding.item:
                r = self.items[slot].item
                if self.items[slot].qtt > 1:
                    self.items[slot].qtt -= 1
                else:
                    self.items[slot] = None
                if who.holding == None:
                    who.holding = stack(r, 1)
                else:
                    who.holding.qtt += 1
            else:
                self.pick(slot, who)