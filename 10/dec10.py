

class ClockCircuit:
    def __init__(self):
        self.register_history = []
        self.X = 1
    
    def tick(self, duration: int):
        for _ in range(duration):
            self.register_history.append(self.X)
    
    def noop(self):
        self.tick(1)

    def addx(self, value: int,):
        # Takes two cycles
        self.tick(2)
        # AFTER the value is added
        self.X += value
    
    def get_signal_strength_at(self, cycle: int) -> int:
        return cycle * self.register_history[cycle-1]  # TODO: Is this indexing correct?
    



with open("10/operations.txt", 'r') as file:
    data = file.read().splitlines()

circuit = ClockCircuit()
for row in data:
    if row == "noop":
        circuit.noop()
    else:
        # must be addx
        _, x = row.split(' ')
        circuit.addx(int(x))

signal_strengths = [circuit.get_signal_strength_at(cycle) for cycle in (20, 60, 100, 140, 180, 220)]

print("Sum of signal strengths: ", sum(signal_strengths))


