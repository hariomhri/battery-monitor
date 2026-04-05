# 🔋 Battery Monitor (Linux)

A modern **GUI Battery Monitoring App** for Linux built with Python & Tkinter.

It shows real-time battery details like:

* 🔋 Battery Percentage
* 💚 Battery Health
* 🔄 Charging Status
* ⏳ Time Remaining
* ⚡ Voltage
* 🔌 Current (Ampere)
* 🔥 Power Consumption (Watt)

---

## 🚀 Features

* ✅ Clean modern UI (dark theme)
* ✅ Real-time updates (every 1 second)
* ✅ Battery health calculation
* ✅ Works on most Linux systems (Ubuntu tested)
* ✅ Lightweight (no heavy dependencies)

---

## 📸 Preview

Simple GUI showing battery stats in card layout.

---

## ⚙️ Requirements

Make sure your system has:

* Python 3.x
* Tkinter
* UPower (for battery data)

---

## 🛠️ Installation

### 1. Install dependencies

```bash
sudo apt update
sudo apt install python3 python3-tk upower
```

---

### 2. Clone repository

```bash
git clone https://github.com/YOUR_USERNAME/battery-monitor.git
cd battery-monitor
```

---

### 3. Run the app

```bash
python3 battery_monitor.py
```

---

## 📊 How It Works

This app uses:

* `upower` → to fetch battery data
* `/sys/class/power_supply` → to calculate battery health
* Tkinter → for GUI

Current (Ampere) is calculated as:

```
Current (A) = Power (W) / Voltage (V)
```

---

## ⚠️ Notes

* Battery data depends on your hardware support
* Some systems may not provide:

  * voltage
  * power
  * health data

In such cases, values will show as `N/A`

---

## 🧪 Tested On

* Ubuntu 22.04 / 24.04
* GNOME Desktop

---

## 🚀 Future Improvements

* 📊 Graph (battery usage history)
* 🖥️ Floating widget
* 🔔 Charging alerts
* 📦 .deb installer

---

## 🤝 Contributing

Feel free to fork and improve the project.

---

## 📜 License

MIT License

---

## 👨‍💻 Author

Made with ❤️ by Hariom Sharma
