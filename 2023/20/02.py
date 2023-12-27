import math

mods = [line.strip() for line in open('input').readlines()]

class ModuleBase:
    def __init__(self, key, connections):
        self.key = key
        self.connections = connections


class FlipFlop(ModuleBase):
    def __init__(self, key, connections):
        super().__init__(key, connections)
        self.state = False


    def process(self, low, _):
        if not low:
            return
        
        for connection in self.connections:
            pulses.append((self.state, self.key, connection))

        self.state = not self.state


class Conjunction(ModuleBase):
    def __init__(self, key, connections):
        super().__init__(key, connections)
        self.recents = dict()


    def add_input(self, input_key):
        self.recents[input_key] = True


    def process(self, low, from_key):
        self.recents[from_key] = low
        some_low = any(self.recents.values())
        for connection in self.connections:
            pulses.append((not some_low, self.key, connection))
        

    def get_low(self):
        return lcm([modules[input_key].get_high() for input_key in self.inputs])
        

class Broadcaster(ModuleBase):
    def __init__(self, key, connections):
        super().__init__(key, connections)


    def process(self, low, _):
        for connection in self.connections:
            pulses.append((low, self.key, connection))


class Rx(ModuleBase):
    def __init__(self):
        super().__init__('rx', [])


    def process(self, low, _):
        global done

        if low:
            done = True


def make_module(descr):
    descr = descr.split(' -> ')

    if descr[0][0] == '%':
        module = FlipFlop(descr[0][1:], descr[1].split(', '))
    elif descr[0][0] == '&':
        module = Conjunction(descr[0][1:], descr[1].split(', '))
    elif descr[0] == 'broadcaster':
        module = Broadcaster(descr[0], descr[1].split(', '))

    modules[module.key] = module


modules = {}
for descr in mods:
    make_module(descr)

modules['rx'] = Rx()

pre_rx = None
for module in modules.values():
    for connection in module.connections:
        to = modules[connection]
        if hasattr(to, 'add_input'):
            to.add_input(module.key)

        if connection == 'rx':
            pre_rx = module.key


pulses, sent_high = [], {}

def find_pre_rx_inputs():
    i = 1
    while True:
        pulses.append((True, 'button', 'broadcaster'))
        while pulses:
            low, from_key, to_key = pulses.pop(0)
            modules[to_key].process(low, from_key)

            if to_key == pre_rx and from_key not in sent_high and not low:
                sent_high[from_key] = i
                if len(sent_high) == len(modules[pre_rx].recents):
                    return
        
        i += 1


find_pre_rx_inputs()

p = 1
for v in sent_high.values():
    p *= v // math.gcd(p, v)

print(p)
