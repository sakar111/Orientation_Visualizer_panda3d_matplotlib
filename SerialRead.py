import time
import random


def ReadData(port_baud, shared_data_supervisor, shared_data_time, shared_data_head, shared_data_pitch, shared_data_roll):
    data_time = 0
    while True:

        while shared_data_supervisor[0] == 'stop':
            time.sleep(1)

        count = 1

        while shared_data_supervisor[0] == 'clear':
            if count == 1:
                shared_data_time[:] = []
                shared_data_head[:] = []
                shared_data_pitch[:] = []
                shared_data_roll[:] = []

            count = 2

            time.sleep(1)


        while shared_data_supervisor[0] == 'start':
            data_head = random.randint(-90, 90)
            data_pitch = random.randint(-90, 90)
            data_roll = random.randint(-90, 90)

            shared_data_time.append(data_time)
            shared_data_head.append(data_head)
            shared_data_pitch.append(data_pitch)
            shared_data_roll.append(data_roll)

            data_time = data_time + 1

            time.sleep(0.5)



