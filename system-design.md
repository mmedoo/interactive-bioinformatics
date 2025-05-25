---
icon: gear
layout:
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
---

# System Design

## **Project Structure**

* **Programming Language**: Python
* **Core Library**: Manim (OpenGL renderer)
*   **Folder Structure**:

    ```markup
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

***

## **Technologies Used**

* [**Manim**](https://manim.community/): Animation engine for mathematical visualizations.
* [**Python**](https://python.org/): Backend logic and algorithm implementation.

***

## **User Flow**

1. **Stage 1**: Input the initial sequence.
2. **Stage 2**: Input the target sequence.
3. **Stage 3**: Choose between **Linear** or **Circular** visualization modes:
   * **Linear**:
     * Visualize transformations using greedy or breakpoint-based algorithms.
   * **Circular**:
     * Visualize cycles and switch edges interactively.

***
