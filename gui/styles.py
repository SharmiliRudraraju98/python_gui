# tree_structures/styles.py
import tkinter as tk
from tkinter import ttk

class TreeVisualizerStyles:
    # Color scheme
    BACKGROUND_COLOR = "#f0f0f0"
    CANVAS_COLOR = "#ffffff"
    PRIMARY_COLOR = "#2c3e50"
    SECONDARY_COLOR = "#3498db"
    SUCCESS_COLOR = "#2ecc71"
    WARNING_COLOR = "#e74c3c"
    NODE_FILL = "#ecf0f1"
    NODE_BORDER = "#34495e"
    EDGE_COLOR = "#95a5a6"
    HIGHLIGHT_PATH_COLOR = "#FF6B6B"
    FOUND_NODE_FILL = "#4CAF50"
    FOUND_NODE_BORDER = "#2E7D32"
    PATH_NODE_FILL = "#FFE0B2"
    
    # AVL Node color gradients
    AVL_NODE_COLORS = [
        "#E3F2FD",  # height 1 - lightest blue
        "#BBDEFB",  # height 2
        "#90CAF9",  # height 3
        "#64B5F6",  # height 4
        "#42A5F5",  # height 5
        "#2196F3",  # height 6
        "#1E88E5",  # height 7
        "#1976D2",  # height 8
        "#1565C0",  # height 9
        "#0D47A1"   # height 10+ - darkest blue
    ]
    
    # Font configurations
    TITLE_FONT = ("Helvetica", 14, "bold")
    HEADER_FONT = ("Helvetica", 12, "bold")
    NORMAL_FONT = ("Helvetica", 10)
    NODE_FONT = ("Helvetica", 10, "bold")

    @classmethod
    def apply_styles(cls):
        style = ttk.Style()
        
        # Configure the main application style
        style.configure("Main.TFrame", background=cls.BACKGROUND_COLOR)
        
        # Configure button styles
        style.configure("Operation.TButton",
                       padding=5,
                       font=cls.NORMAL_FONT)
        
        style.configure("Success.TButton",
                       padding=5,
                       font=cls.NORMAL_FONT)
        
        style.configure("Warning.TButton",
                       padding=5,
                       font=cls.NORMAL_FONT)
        
        # Configure label styles
        style.configure("Title.TLabel",
                       font=cls.TITLE_FONT,
                       background=cls.BACKGROUND_COLOR,
                       foreground=cls.PRIMARY_COLOR)
        
        style.configure("Header.TLabel",
                       font=cls.HEADER_FONT,
                       background=cls.BACKGROUND_COLOR,
                       foreground=cls.PRIMARY_COLOR)
        
        style.configure("Metric.TLabel",
                       font=cls.NORMAL_FONT,
                       background=cls.BACKGROUND_COLOR,
                       padding=3)
        
        # Configure frame styles
        style.configure("Panel.TFrame",
                       background=cls.BACKGROUND_COLOR)
        
        style.configure("Control.TLabelframe",
                       background=cls.BACKGROUND_COLOR,
                       padding=10)
        
        style.configure("Control.TLabelframe.Label",
                       font=cls.HEADER_FONT,
                       background=cls.BACKGROUND_COLOR,
                       foreground=cls.PRIMARY_COLOR)

        # Entry style
        style.configure("Custom.TEntry",
                       padding=5,
                       font=cls.NORMAL_FONT)

    @classmethod
    def get_node_colors(cls, is_avl=False, height=1):
        """Get gradient colors based on node height for AVL trees"""
        if not is_avl:
            return cls.NODE_FILL, cls.NODE_BORDER
        
        # Get color based on height (clamped to available colors)
        color_index = min(height - 1, len(cls.AVL_NODE_COLORS) - 1)
        color_index = max(0, color_index)  # Ensure index is not negative
        return cls.AVL_NODE_COLORS[color_index], cls.NODE_BORDER