✋ Hand Guester
A real-time hand gesture recognition system using Python and OpenCV

Hand Guester is a Python-based computer vision project designed to recognize and interpret hand gestures in real time.
It uses machine learning and image processing techniques to create contactless control of applications through simple hand movements captured via webcam.

This project is ideal for gesture-based control, automation, and AI education demos.

✨ Features
  🖐 Real-time hand tracking via webcam input
  
  🔍 Static and dynamic gesture recognition
  
  ⚙️ Customizable gesture-to-action mapping
  
  💡 Lightweight & portable – runs on basic hardware
  
  🧠 Built fully in Python with OpenCV and MediaPipe

💡 Applications
  🖱 Virtual mouse and keyboard interface
  
  🏠 Smart home automation control
  
  🎓 Computer vision learning demonstrations
  
  🚀 Interactive and accessible computing

⚙️ Requirements
  Make sure you have the following installed:
  
  Python 3.8+
  
  OpenCV (cv2)
  
  MediaPipe
  
  NumPy
  
  PyAutoGUI (optional for automation actions)

Install dependencies with:

bash
pip install opencv-python mediapipe numpy pyautogui
🚀 How to Run
Clone and launch the program:

bash
git clone https://github.com/Shakthivijay/hand_guester.git
cd hand_guester
python hand_guester.py
Then, position your hand in front of the webcam and perform encoded gestures.
Each gesture will map to the corresponding action as defined in the main script logic.

📂 Folder Structure
text
hand_guester/
│
├── hand_guester.py             # Main script for gesture detection
├── modules/                    # Optional helper modules  
├── requirements.txt            # Dependency list  
└── README.md                   # Project documentation
🧩 Working Principle
  Input Capture: Webcam detects the hand region.
  
  Preprocessing: Converts frames, removes noise, and enhances contrast.
  
  Landmark Detection: MediaPipe model identifies 21 keypoints on the hand.
  
  Gesture Recognition: Mapped contours & keypoints trigger predefined commands.
  
  Action Triggered: Executes keyboard/mouse actions using PyAutoGUI.



🤖 Add gesture training with custom ML models

✋ Multi-hand and multi-user tracking

🌐 IoT integration for device automation

🪟 GUI configuration dashboard for gestures

🙏 Acknowledgments
Inspired by open-source gesture control systems and projects built on OpenCV, MediaPipe, and TensorFlow.
This is a demonstration of AI-driven Human-Computer Interaction (HCI) for next-generation applications.

📜 License
Licensed under the MIT License – Free to use, modify, and distribute.
