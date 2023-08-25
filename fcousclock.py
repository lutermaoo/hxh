import time

def focus_timer(total_time, interval):
    while total_time > 0:
        print(f"Remain focused! {total_time} seconds left.")
        time.sleep(interval)
        total_time -= interval
    print("Time's up! Your focus session has ended.")

if __name__ == "__main__":
    total_time = int(input("Enter the total time for focus session (in seconds): "))
    interval = int(input("Enter the interval for reminders (in seconds): "))
    focus_timer(total_time, interval)
