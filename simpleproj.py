"""Temperature log storage with file handling, datetime and threading"""
import threading
import datetime
import random
import os
import time

def read_temperature():
    """Function to simulate temperature reading from a sensor"""
    temperature = random.uniform(0, 100)
    return temperature

def log_temperature(sensor_id, stop_event):
    """Function to log temperature data to a file"""
    while not stop_event.is_set():
        temperature = read_temperature()
        current_time = datetime.datetime.now()
        log_line = f"{current_time}: Sensor {sensor_id} - Temperature: {temperature:.2f} °C\n"

        # Create a log directory if it doesn't exist
        log_dir = f"sensor_logs/sensor_{sensor_id}"
        os.makedirs(log_dir, exist_ok=True)

        # Generate a log file name based on the current date
        log_file = os.path.join(log_dir, f"{current_time.date()}_log.txt")

        # Append the temperature data to the log file
        with open(log_file, "a", encoding="utf8") as file:
            file.write(log_line)

        # Sleep for a fixed duration ex: 2sec
        sleep_duration=2
        time.sleep(sleep_duration)

def main():
    """Create and start multiple sensor threads"""
    num_sensors = 3
    threads = []
    stop_events = []

    for sensor_id in range(num_sensors):
        stop_event = threading.Event()
        thread = threading.Thread(target=log_temperature, args=(sensor_id, stop_event))
        thread.start()
        threads.append(thread)
        stop_events.append(stop_event)

    # Run the threads for a fixed duration ex: 10sec
    run_duration = 10
    time.sleep(run_duration)

    # Signal the threads to stop
    for stop_event in stop_events:
        stop_event.set()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
