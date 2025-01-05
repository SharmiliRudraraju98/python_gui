Tree Comparison Visualizer
**Author**: Sharmili Rudraraju
**Course**: CSE-411 Advanced Programming Techniques
**Instructor**: Prof. Corey Montella

---

Introduction
The **Tree Comparison Visualizer** is a Python-based application designed to provide side-by-side visualizations of Binary Search Trees (BST) and AVL Trees. It aims to help users understand and compare the behavior and performance of these two fundamental data structures.

The tool offers real-time metrics, dynamic visualizations, and intuitive controls, making it an excellent resource for both learners and professionals.

---

Features
- **Side-by-Side Visualization**: Compare BST and AVL tree structures and operations in real time.
- **Performance Metrics**: Track operation times, comparison counts, and AVL tree rotations.
- **Stress Testing**: Analyze tree performance with large datasets.
- **Intuitive Interface**: Simple controls for insertion, deletion, searching, and resetting trees.
- **Keyboard Shortcuts**: Enhance usability with shortcuts for common operations.

---

System Requirements
- **Operating System**: Windows
- **Python Version**: Python 3.7 or higher
- **Display Resolution**: Minimum 1400x900 pixels
- **RAM**: At least 4GB (recommended for large trees)

---

Installation
### Steps:
1. Ensure Python 3.7 or higher is installed on your system. Verify using:
   ```bash
   python --version
   ```
2. **Tkinter** (required for the GUI) is bundled with Python. No additional package installations are necessary.
3. Download the source code from the repository and extract it to your preferred location.
4. Navigate to the application directory in the terminal or command prompt.
5. Run the application using:
   ```bash
   python app.py
   ```
6. Alternatively, use the precompiled Windows `.exe` file located in the `dist` folder.

---

How to Use
Main Window Layout
1. **Control Panel**: Input values and perform operations (insert, find, delete, etc.).
2. **Visualization Area**: View the BST and AVL trees side by side.
3. **Performance Metrics Panel**: Real-time statistics on operations.
Basic Operations
- **Insert**: Add values to both trees.
- **Find**: Search for values in both trees and highlight paths.
- **Delete**: Remove values and observe restructuring.
- **Random**: Generate and insert random values.
- **Stress Test**: Perform stress testing with large datasets.
- **Reset**: Clear both trees.
Keyboard Shortcuts
| Shortcut   | Action         | Description                          |
|------------|----------------|--------------------------------------|
| `Enter`    | Insert         | Adds the current value to both trees |
| `Delete`   | Remove         | Deletes the current value            |
| `Ctrl+F`   | Find           | Searches for the current value       |
| `Ctrl+R`   | Random         | Inserts a random value               |
| `Ctrl+T`   | Stress Test    | Runs a performance test              |
| `Escape`   | Reset          | Clears both trees                    |

---

Advanced Features
- **Visualization Enhancements**:
  - AVL nodes are color-coded based on height.
  - Search paths and target nodes are highlighted.
  - Connecting edges vary in thickness and color based on operations.

- **Stress Testing**:
  - Inserts 20 random values to simulate larger datasets.
  - Tracks tree height, rotations, comparisons, and operation times.

- **Performance Metrics**:
  - Tracks execution time (in microseconds), comparisons, and rotations.
  - Provides insights into the efficiency of balanced (AVL) vs. unbalanced (BST) trees.

---

Troubleshooting
Common Issues
1. **Invalid Input**: Ensure the input field contains integers only.
2. **Slow Performance**: Reset trees periodically or use smaller datasets.
3. **Visual Glitches**: Resize the window to refresh the layout.

---

Best Practices
For Learning
- Start with small trees to understand basics.
- Demonstrate balanced vs. unbalanced scenarios.
- Compare search paths and restructuring processes.
For Performance Testing
- Use systematic test patterns.
- Document results for consistent comparisons.

---

References
- [Python Documentation](https://docs.python.org/3/)
- [TkDocs](https://tkdocs.com/)
- [GeeksforGeeks: BST & AVL Tree Complexity](https://www.geeksforgeeks.org/complexity-different-operations-binary-tree-binary-search-tree-avl-tree/)
- [Interactive Visual Binary Search Tree](https://github.com/kousheekc/Interactive-Visual-Binary-Search-Tree)
- [Binary Search Tree GUI](https://github.com/nahrens007/BinarySearchTreeGui)

---

License
This project is provided for educational purposes. Please contact the author for permission to use in other contexts.
