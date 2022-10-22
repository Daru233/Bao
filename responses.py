import random


def handle_response(message):

    ROLL_SUBSTRING = 'roll'

    if message == '-hello':
        return 'hola'

    if ROLL_SUBSTRING in message:
        int_a, int_b = message.split()[1:]
        print(int_a, int_b)
        return random.randint(int_a, int_b)

    # if message is not None and ROLL_SUBSTRING in message:
    #     return 'message was roll'
    # else:
    #     return 'return was in the message'
