mods = [line.strip() for line in open('input').readlines()]

modules, pulses, presses = {}, [], {True: 0, False: 0}

class FlipFlop:
    def __init__(self, key, connections):
        self.key = key
        self.connections = connections
        self.state = False


    def process(self, low, _):
        if not low:
            return
        
        for connection in self.connections:
            pulses.append((self.state, self.key, connection))

        self.state = not self.state


class Conjunction:
    def __init__(self, key, connections):
        self.key = key
        self.connections = connections
        self.recents = dict()


    def add_input(self, input_key):
        self.recents[input_key] = True


    def process(self, low, from_key):
        self.recents[from_key] = low
        some_low = any(self.recents.values())
        for connection in self.connections:
            pulses.append((not some_low, self.key, connection))
        

class Broadcaster:
    def __init__(self, key, connections):
        self.key = key
        self.connections = connections


    def process(self, low, _):
        for connection in self.connections:
            pulses.append((low, self.key, connection))


class Dummy:
    def __init__(self, key):
        self.key = key


    def process(self, _, __):
        pass


def make_module(descr):
    descr = descr.split(' -> ')

    if descr[0][0] == '%':
        module = FlipFlop(descr[0][1:], descr[1].split(', '))
    elif descr[0][0] == '&':
        module = Conjunction(descr[0][1:], descr[1].split(', '))
    elif descr[0] == 'broadcaster':
        module = Broadcaster(descr[0], descr[1].split(', '))

    modules[module.key] = module


for descr in mods:
    make_module(descr)

for module in list(modules.values()):
    for connection in module.connections:
        if connection not in modules:
            modules[connection] = Dummy(connection)

        to = modules[connection]
        if hasattr(to, 'add_input'):
            to.add_input(module.key)

def press_button():
    pulses.append((True, 'button', 'broadcaster'))
    while pulses:
        low, from_key, to_key = pulses.pop(0)
        presses[low] += 1
        modules[to_key].process(low, from_key)


for _ in range(1000):
    press_button()


print(presses[True] * presses[False])
