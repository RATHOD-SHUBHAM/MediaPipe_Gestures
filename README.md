# MediaPipe_Gestures

# 🖐️ Hand Gesture Recognition and Tracking using MediaPipe

This repository contains Python code that leverages **Google’s MediaPipe** to recognize and track hand gestures from both live camera streams and static images.

Using real-time hand landmark detection, the system can track individual fingers, detect various hand poses, and interpret gestures that can be used in a wide range of applications.

---

## 🔍 Overview

At the core of this project is MediaPipe’s **Hand Tracking solution**, which provides 21 3D landmarks per detected hand with high accuracy and real-time performance. This enables gesture classification, pose estimation, and motion tracking with minimal setup.

The code in this repository supports:
- 🎥 Real-time gesture recognition using live video streams
- 🖼️ Gesture detection from saved images
- ✨ Preprocessing and annotation utilities for visualization

---

## 🤖 Applications

Hand gesture recognition has wide applicability across domains such as:
- **Human-computer interaction**
- **Sign language interpretation**
- **AR/VR input systems**
- **Touchless interfaces**
- **Gaming and immersive environments**

### 🚀 Use Case in Robotics

I integrated this system into a **robotics project** where a **robotic arm mimicked human hand movements** in real-time. Using the detected hand landmarks, joint angles were inferred and relayed to the robot's servos, enabling intuitive and natural gesture-based control.

---

## 🛠️ Tech Stack

- 🐍 **Python 3**
- 🪞 **MediaPipe Hands** solution
- 🎥 **OpenCV** for real-time video handling and visualization

---

## 📁 Contents

- `LiveSteam` – Detect and visualize hand gestures in real-time from webcam
- `Image` – Perform gesture recognition on static images
- Utility scripts and drawing helpers

---

