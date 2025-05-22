# 🧬 Sequence Transformation Visualizer

This repository provides an interactive **sequence transformation visualizer** built with **Manim Community Edition**. It is designed to help users understand and visualize sequence transformations through both **linear** and **circular** operations. The tool is ideal for educational purposes, algorithm demonstrations, and debugging sequence-based problems.

---

## ✨ Features

- **Interactive Input**:
  - Input initial and target sequences interactively.
  - Real-time validation of user inputs with error feedback.

- **Visualization Modes**:
  - **Linear Mode**:
    - Supports greedy and breakpoint-based sequence transformations.
  - **Circular Mode**:
    - Visualizes circular sequence transformations edge switching.

- **Dynamic UI**:
  - Clickable buttons for mode selection, resetting, and navigation.
  - Hover effects for enhanced interactivity.

---

## ⚙️ Prerequisites

- Python 3.10+

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/mmedoo/manim
   cd manim
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   ```

3. Install dependencies:

   - **On Linux/macOS:**
      ```bash
      source venv/bin/activate
      pip install -r reqs.txt
      ```

   - **On Windows:**
      ```bash
      venv\Scripts\activate
      pip install -r reqs.txt
      ```
---

## 🚀 Usage

Run the main script to start the app:
- **On Linux/macOS:**
   ```bash
   venv/bin/manim -p -qm --renderer=opengl main.py Run
   ```

- **On Windows:**
  ```bash
  venv\Scripts\manim.exe -p -qm --renderer=opengl main.py Run
  ```


## 🛠️ Workflow

1. **Stage 1**: Input the initial sequence.
2. **Stage 2**: Input the target sequence.
3. **Stage 3**: Choose between **Linear** or **Circular** visualization modes:
   - **Linear**:
     - Visualize transformations using greedy or breakpoint-based algorithms.
   - **Circular**:
     - Visualize cycles and switch edges interactively.

---

## 🗂️ Project Structure

```
├── src/                   # Source code
│   ├── circular.py        # Circular sequence visualization logic
│   ├── events.py          # Event handling (mouse, keyboard)
│   ├── stages.py          # Stage management for the visualization
│   ├── utils/             # Utility functions for interactivity and visualization
│   └── linear/            # Linear sequence visualization logic
│   │   ├── entry.py       # Entry point for linear visualization
│   │   ├── greedy.py      # Greedy algorithm implementation
│   │   └── breakpoint.py  # Breakpoint-based algorithm implementation
├── README.md              # Project documentation
├── main.py                # Entry point for the visualization
└── reqs.txt               # Python dependencies
```

---

## 🔮 Planned Features

- [ ] Support for negative block enterance.
- [ ] Cycle counting in circular mode.
- [ ] Current sequence written in circular mode.

---

## 🤝 Contributing

Contributions are welcome! Follow these steps to contribute:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature-name"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---

## 📄 License

This project is licensed under the MIT License. See the LICENSE file for details.

---

Happy Visualizing! 🎥