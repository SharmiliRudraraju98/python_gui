# gui/performance_panel.py
import tkinter as tk
from tkinter import ttk
from .styles import TreeVisualizerStyles as Styles

class PerformancePanel(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, style="Panel.TFrame")
        self.setup_ui()
    
    def setup_ui(self):
        # Create a more compact layout
        metrics_frame = ttk.Frame(self, style="Panel.TFrame")
        metrics_frame.pack(fill=tk.X, padx=5, pady=2)
        
        # Create styles for BST and AVL frames with background color
        style = ttk.Style()
        style.configure("BST.TLabelframe", background="lightblue")
        style.configure("AVL.TLabelframe", background="lightgreen")
        
        # BST Metrics
        bst_frame = ttk.LabelFrame(metrics_frame, text="BST", style="BST.TLabelframe")
        bst_frame.pack(side=tk.LEFT, padx=5, pady=2, fill=tk.X, expand=True)
        
        # Create columns for BST metrics
        bst_left = ttk.Frame(bst_frame)
        bst_left.pack(side=tk.LEFT, padx=5)
        bst_right = ttk.Frame(bst_frame)
        bst_right.pack(side=tk.LEFT, padx=5)
        
        self.bst_labels = {
            'comparisons': self._create_compact_label(bst_left, "#Comp:"),
            'insert_time': self._create_compact_label(bst_left, "Ins:"),
            'find_time': self._create_compact_label(bst_left, "Find:"),
            'delete_time': self._create_compact_label(bst_right, "Del:"),
            'operations': self._create_compact_label(bst_right, "#Oper:")
        }
        
        # AVL Metrics
        avl_frame = ttk.LabelFrame(metrics_frame, text="AVL", style="AVL.TLabelframe")
        avl_frame.pack(side=tk.LEFT, padx=5, pady=2, fill=tk.X, expand=True)
        
        # Create columns for AVL metrics
        avl_left = ttk.Frame(avl_frame)
        avl_left.pack(side=tk.LEFT, padx=5)
        avl_right = ttk.Frame(avl_frame)
        avl_right.pack(side=tk.LEFT, padx=5)
        
        self.avl_labels = {
            'comparisons': self._create_compact_label(avl_left, "#Comp:"),
            'rotations': self._create_compact_label(avl_left, "#Rot:"),
            'insert_time': self._create_compact_label(avl_right, "Ins:"),
            'find_time': self._create_compact_label(avl_right, "Find:"),
            'delete_time': self._create_compact_label(avl_right, "Del:")
        }

    
    def _create_compact_label(self, parent, text):
        frame = ttk.Frame(parent)
        frame.pack(anchor='w', pady=1)
        ttk.Label(frame, text=text, style="Metric.TLabel",
                 width=8).pack(side=tk.LEFT)
        value = ttk.Label(frame, text="0", style="Metric.TLabel",
                         width=10)
        value.pack(side=tk.LEFT)
        return value
    
    def update_metrics(self, bst_metrics, avl_metrics):
        # Update BST metrics
        self.bst_labels['comparisons'].config(text=str(bst_metrics.comparisons))
        
        # Format times to microseconds for better visibility
        bst_insert_time = bst_metrics.get_avg_time('insert') * 1_000_000
        bst_delete_time = bst_metrics.get_avg_time('delete') * 1_000_000
        bst_find_time = bst_metrics.get_avg_time('find') * 1_000_000
        
        self.bst_labels['insert_time'].config(
            text=f"{bst_insert_time:.1f}µs")
        self.bst_labels['find_time'].config(
            text=f"{bst_find_time:.1f}µs")
        self.bst_labels['delete_time'].config(
            text=f"{bst_delete_time:.1f}µs")
        self.bst_labels['operations'].config(
            text=str(sum(bst_metrics.operations.values())))
        
        # Update AVL metrics
        self.avl_labels['comparisons'].config(text=str(avl_metrics.comparisons))
        self.avl_labels['rotations'].config(text=str(avl_metrics.rotations))
        
        avl_insert_time = avl_metrics.get_avg_time('insert') * 1_000_000
        avl_delete_time = avl_metrics.get_avg_time('delete') * 1_000_000
        avl_find_time = avl_metrics.get_avg_time('find') * 1_000_000
        
        self.avl_labels['insert_time'].config(
            text=f"{avl_insert_time:.1f}µs")
        self.avl_labels['find_time'].config(
            text=f"{avl_find_time:.1f}µs")
        self.avl_labels['delete_time'].config(
            text=f"{avl_delete_time:.1f}µs")