import tkinter as tk
import subprocess

BAT_PATH = "/org/freedesktop/UPower/devices/battery_BAT1"

def get_battery_data():
    try:
        output = subprocess.check_output(
            ["upower", "-i", BAT_PATH]
        ).decode()

        def extract(key):
            for line in output.split("\n"):
                if key in line:
                    return line.split(":")[1].strip()
            return "N/A"

        percentage = extract("percentage")
        state = extract("state")

        time = "N/A"
        for line in output.split("\n"):
            if "time to full" in line or "time to empty" in line:
                time = line.split(":")[1].strip()

        power_raw = extract("energy-rate")
        voltage_raw = extract("voltage")

        power = power_raw.split()[0] if power_raw != "N/A" else "N/A"
        voltage = voltage_raw.split()[0] if voltage_raw != "N/A" else "N/A"

        try:
            amp = float(power) / float(voltage)
            amp = f"{amp:.2f}"
        except:
            amp = "N/A"

        # battery health
        try:
            full = int(open("/sys/class/power_supply/BAT1/energy_full").read())
            design = int(open("/sys/class/power_supply/BAT1/energy_full_design").read())
            health = (full / design) * 100
            health = f"{health:.1f}%"
        except:
            try:
                full = int(open("/sys/class/power_supply/BAT1/charge_full").read())
                design = int(open("/sys/class/power_supply/BAT1/charge_full_design").read())
                health = (full / design) * 100
                health = f"{health:.1f}%"
            except:
                health = "N/A"

        return percentage, state, time, voltage, amp, power, health

    except:
        return ("Error",) * 7


def update():
    p, s, t, v, a, w, h = get_battery_data()

    battery_value.config(text=p)
    health_value.config(text=h)
    status_value.config(text=s)
    time_value.config(text=t)
    voltage_value.config(text=f"{v} V")
    current_value.config(text=f"{a} A")
    power_value.config(text=f"{w} W")

    root.after(1000, update)


# 🎨 UI Setup
root = tk.Tk()
root.title("Battery Monitor")
root.geometry("360x400")
root.configure(bg="#0f172a")  # dark modern bg

# Header
header = tk.Label(root, text="🔋 Battery Monitor", font=("Arial", 18, "bold"),
                  fg="white", bg="#0f172a")
header.pack(pady=10)

# Card function
def create_card(title):
    frame = tk.Frame(root, bg="#1e293b", padx=10, pady=8)
    frame.pack(fill="x", padx=15, pady=5)

    label = tk.Label(frame, text=title, font=("Arial", 10),
                     fg="#94a3b8", bg="#1e293b")
    label.pack(anchor="w")

    value = tk.Label(frame, text="--", font=("Arial", 14, "bold"),
                     fg="white", bg="#1e293b")
    value.pack(anchor="w")

    return value


# Cards (modern UI)
battery_value = create_card("Battery Level")
health_value = create_card("Battery Health")
status_value = create_card("Status")
time_value = create_card("Time Remaining")
voltage_value = create_card("Voltage")
current_value = create_card("Current (Ampere)")
power_value = create_card("Power (Watt)")

update()
root.mainloop()
