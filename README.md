# DriveGuard-AI-A-Vision-Based-Blind-Spot-Monitoring-and-Lane-Departure-Warning-System

## 📖 Overview

**SafeLane** is a computer vision–based driver-assistance system that enhances road safety by addressing two common causes of accidents:

1. **Blind-spot hazards** – when vehicles in adjacent lanes are hidden from the driver’s view.
2. **Lane departure risks** – when a vehicle drifts out of its lane unintentionally.

The system uses **YOLOv8** for real-time vehicle detection and **OpenCV lane detection** algorithms. When a vehicle enters the blind-spot region, or if the driver deviates from the lane, the system raises a **visual + audible alert** to the driver.

This project demonstrates how **AI + computer vision** can improve automotive safety at low cost, making it an excellent proof-of-concept for **ADAS (Advanced Driver Assistance Systems)**.

---

## ⚡ Features

* **Blind-Spot Detection:** Monitors predefined regions (left & right ROIs).
* **Lane Departure Warning:** Uses Canny + Hough transforms to detect lane markings.
* **YOLOv8 Vehicle Detection:** Real-time detection of cars, buses, trucks, and motorcycles.
* **Configurable ROIs:** Adjustable via `config.json` for different cameras/vehicles.
* **Alerts:** On-screen warnings and optional audio beeps.
* **Works on Video or Live Camera:** Can run with dashcam feed or webcam.

---

## 🗂️ Project Structure

```
blindspot-lane-assist/
├── main.py              # Main entry point
├── config.json          # Config for camera source, ROIs, thresholds
├── requirements.txt     # Dependencies
└── README.md            # Documentation
```

---

## ⚙️ Installation

### 1. Clone the project

```bash
git clone https://github.com/your-username/blindspot-lane-assist.git
cd blindspot-lane-assist
```

### 2. Setup virtual environment

**Windows (PowerShell):**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**Linux/macOS:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

### Run on webcam (default):

```bash
python main.py
```

### Run with custom config:

```bash
python main.py -c config.json
```

### Run on video file:

Edit `config.json`:

```json
"source": "sample_video.mp4"
```

---

## 🔧 Configuration (`config.json`)

* **source:** Video source (0 = webcam, or path to video file).
* **blindspot.left / right:** Normalized coordinates for left/right blind-spot regions.
* **lane.roi:** Triangular ROI for lane detection.
* **alerts:** Enable/disable beep, adjust cooldown time.
* **draw:** Toggle bounding boxes, lane lines, FPS counter.

Example:

```json
"blindspot": {
  "left": [[0.05, 0.68], [0.28, 0.60], [0.43, 0.95], [0.05, 0.95]],
  "right": [[0.72, 0.60], [0.95, 0.68], [0.95, 0.95], [0.57, 0.95]]
}
```

---

## 🧠 Tech Stack

* **Python 3.10+**
* **OpenCV** – Lane detection, ROI handling, visualization.
* **YOLOv8 (Ultralytics)** – Real-time vehicle detection.
* **NumPy** – Image operations & geometry.

---

## 📊 Performance

* **FPS:** \~15–30 on CPU with YOLOv8n (depending on resolution).
* **Accuracy:** Works well on daylight highway/dashcam footage.
* **Limitations:** Lane detection may struggle in poor lighting, rain, or worn-out road markings.

---

## 🚀 Future Improvements

* Train YOLO on **custom dataset** for side/rear cameras in local conditions.
* Use **Deep Learning–based lane detection** (e.g., SCNN, LaneNet) for robustness.
* Add **distance estimation** and **collision warning system**.
* Integrate with **Raspberry Pi + USB Camera** for low-cost deployment.

---

## 🏆 Applications

* Advanced Driver Assistance Systems (ADAS)
* Low-cost retrofitting for existing vehicles
* Research in autonomous driving & AI safety systems

---

## 👨‍💻 Author

* **Sujal Revankar** – Final Year CSE (AIML) Student
* Developed as a **Major Project** for B.E. in Artificial Intelligence & Machine Learning

---

👉 I can also create a **short abstract + block diagram** (for your project report submission). Do you want me to prepare that as well?
