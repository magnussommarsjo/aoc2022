import enum

class Oponent(str, enum.Enum):
    ROCK = 'A'
    PAPER = 'B'
    SCISSORS = 'C'

class Response(str, enum.Enum):
    ROCK = 'X'
    PAPER = 'Y'
    SCISSOR = 'Z'

class Outcome(int, enum.Enum):
    WON = 6
    LOSE = 0
    DRAW = 3
    
def get_shape_point(response: Response) -> int:
    match response:
        case Response.ROCK:
            return 1
        case Response.PAPER:
            return 2
        case Response.SCISSOR:
            return 3

def get_outcome(oponent: str, response: str) -> Outcome:
    match oponent:
        case Oponent.ROCK:
            match response:
                case Response.ROCK:
                    return Outcome.DRAW
                case Response.PAPER:
                    return Outcome.WON
                case Response.SCISSOR:
                    return Outcome.LOSE
        case Oponent.PAPER:
            match response:
                case Response.ROCK:
                    return Outcome.LOSE
                case Response.PAPER:
                    return Outcome.DRAW
                case Response.SCISSOR:
                    return Outcome.WON
        case Oponent.SCISSORS:
            match response:
                case Response.ROCK:
                    return Outcome.WON
                case Response.PAPER:
                    return Outcome.LOSE
                case Response.SCISSOR:
                    return Outcome.DRAW




# Read and transform data
with open("02/strategy_guide.txt") as file:
    data = file.read()

lines = data.split('\n')
rounds = [line.split(' ') for line in lines]


scores = []
for round in rounds:
    if round == ['']:
        continue
    oponent = round[0]
    response = round[1]
    outcome = get_outcome(oponent, response)
    shape_point = get_shape_point(response)
    scores.append(outcome + shape_point)

print("First 3 rounds: ", scores[:3])
print("Total score: ", sum(scores))

# PART TWO =====================================================================


class DesiredOutcome(str, enum.Enum):
    LOSE = 'X'
    DRAW = 'Y'
    WIN = 'Z'

def get_response(oponent: str, disired_outcome: DesiredOutcome) -> Response:
    match oponent:
        case Oponent.ROCK:
            match disired_outcome:
                case DesiredOutcome.WIN:
                    return Response.PAPER
                case DesiredOutcome.LOSE:
                    return Response.SCISSOR
                case DesiredOutcome.DRAW:
                    return Response.ROCK
        case Oponent.PAPER:
            match disired_outcome:
                case DesiredOutcome.WIN:
                    return Response.SCISSOR
                case DesiredOutcome.LOSE:
                    return Response.ROCK
                case DesiredOutcome.DRAW:
                    return Response.PAPER
        case Oponent.SCISSORS:
            match disired_outcome:
                case DesiredOutcome.WIN:
                    return Response.ROCK
                case DesiredOutcome.LOSE:
                    return Response.PAPER
                case DesiredOutcome.DRAW:
                    return Response.SCISSOR


scores = []
for round in rounds:
    if round == ['']:
        continue
    oponent = round[0]
    desired_outcome = round[1]
    response = get_response(oponent, desired_outcome)

    outcome = get_outcome(oponent, response)
    shape_point = get_shape_point(response)
    scores.append(outcome + shape_point)

print("\n==== PART TWO =====")
print("First 3 rounds: ", scores[:3])
print("Total score: ", sum(scores))
