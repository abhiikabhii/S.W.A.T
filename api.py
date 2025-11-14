import random
import time

def get_sensor_data():
    return {
        "ph": round(random.uniform(6.0, 9.5), 2),
        "turbidity": round(random.uniform(1.0, 9.0), 2),
        "flow": round(random.uniform(0.0, 2.0), 2)
    }

if __name__ == "__main__":
    while True:
        print(get_sensor_data())
        time.sleep(2)
