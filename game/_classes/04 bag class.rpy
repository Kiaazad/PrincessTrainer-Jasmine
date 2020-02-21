init python:
    class bag:
        def __init__(self, name, slots = 10, items = []):
            self.name = name
            self.slots = slots
            self.items = [None]* self.slots
            if items:
                for ii,i in enumerate(items):
                    self.add(i[0], i[1])
            self.dropped_x = 0
        def shuffle(self):
            renpy.random.shuffle(self.items)
        
        def add(self, x, q): # x = item, q = Quantity
            for i in self.items:
                if i and i.item == x:
                    i.qtt += q
                    break
            else:
                for ii,i in enumerate(self.items):
                    if i == None:
                        self.items[ii] = stack(x, q)
                        break
                else:
                    return "Full"
        def stack(self):
            pass
        def drop(self, drags, drop):
            self.dropped_x = drags[0].x
            renpy.restart_interaction()
        def swap(self, s, w):
            r = self.items[s]
            self.items[s] = w.holding
            w.holding = r
        def pick(self, s, w):
            if w.holding and self.items[s]:
                if self.items[s].item == w.holding.item:
                    self.items[s].qtt += w.holding.qtt
                    w.holding = None
                else:
                    self.swap(s, w)
            else:
                self.swap(s, w)
        def pickOne(self, s, w):
            if self.items[s] == None:
                self.pick(s, w)
            elif  w.holding == None or self.items[s].item == w.holding.item:
                r = self.items[s].item
                if self.items[s].qtt > 1:
                    self.items[s].qtt -= 1
                else:
                    self.items[s] = None
                if w.holding == None:
                    w.holding = stack(r, 1)
                else:
                    w.holding.qtt += 1
            else:
                self.pick(s, w)