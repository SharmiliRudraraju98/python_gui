# main.py
import tkinter as tk
from tkinter import ttk, messagebox
import random
from tree_structures.bst import BST
from tree_structures.avl import AVLTree
from gui.performance_panel import PerformancePanel
from gui.styles import TreeVisualizerStyles as Styles

class TreeComparisonVisualizer(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Tree Data Structures Visualization")
        self.geometry("1400x900")
        self.configure(bg=Styles.BACKGROUND_COLOR)
        
        # Apply custom styles
        Styles.apply_styles()
        
        # Create main container
        self.main_container = ttk.Frame(self, style="Main.TFrame")
        self.main_container.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Create compact header section
        header_frame = ttk.Frame(self.main_container)
        header_frame.pack(fill=tk.X)
        
        # Create performance panel and control panel
        self.performance_panel = PerformancePanel(header_frame)
        self.performance_panel.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        self.control_panel = ttk.Frame(header_frame, style="Panel.TFrame")
        self.control_panel.pack(side=tk.RIGHT, fill=tk.X)
        self.setup_controls()
        
        # Create visualization area
        self.viz_container = ttk.Frame(self.main_container, style="Panel.TFrame")
        self.viz_container.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # Create canvases for both trees
        self.canvas_bst = tk.Canvas(self.viz_container, 
                                  bg=Styles.CANVAS_COLOR,
                                  highlightthickness=1,
                                  highlightbackground=Styles.EDGE_COLOR)
        self.canvas_avl = tk.Canvas(self.viz_container, 
                                  bg=Styles.CANVAS_COLOR,
                                  highlightthickness=1,
                                  highlightbackground=Styles.EDGE_COLOR)
        
        self.canvas_bst.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=2)
        self.canvas_avl.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=2)
        
        # Initialize trees
        self.bst = BST()
        self.avl = AVLTree()

    def setup_controls(self):
        # Create a more compact control panel
        control_container = ttk.Frame(self.control_panel, style="Panel.TFrame")
        control_container.pack(fill=tk.X, padx=5, pady=2)
        
        # Left side: Value input and basic operations
        left_frame = ttk.Frame(control_container)
        left_frame.pack(side=tk.LEFT, padx=5)
        
        # Compact input area
        input_area = ttk.Frame(left_frame)
        input_area.pack(side=tk.LEFT, padx=5)
        
        self.value_entry = ttk.Entry(input_area, width=6, style="Custom.TEntry")
        self.value_entry.pack(side=tk.LEFT, padx=2)
        
        # Basic operations in a row
        ops_frame = ttk.Frame(left_frame)
        ops_frame.pack(side=tk.LEFT, padx=2)
        
        ttk.Button(ops_frame, text="Insert", width=6,
                  command=self.insert_value,
                  style="Operation.TButton").pack(side=tk.LEFT, padx=1)
        ttk.Button(ops_frame, text="Find", width=6,
                  command=self.find_value,
                  style="Operation.TButton").pack(side=tk.LEFT, padx=1)
        ttk.Button(ops_frame, text="Delete", width=6,
                  command=self.delete_value,
                  style="Operation.TButton").pack(side=tk.LEFT, padx=1)
        
        # Right side: Additional operations
        right_frame = ttk.Frame(control_container)
        right_frame.pack(side=tk.RIGHT, padx=5)
        
        ttk.Button(right_frame, text="Random", width=8,
                  command=self.insert_random,
                  style="Operation.TButton").pack(side=tk.LEFT, padx=1)
        ttk.Button(right_frame, text="Stress", width=8,
                  command=self.run_stress_test,
                  style="Success.TButton").pack(side=tk.LEFT, padx=1)
        ttk.Button(right_frame, text="Reset", width=8,
                  command=self.reset_trees,
                  style="Warning.TButton").pack(side=tk.LEFT, padx=1)

    def insert_value(self):
        try:
            value = int(self.value_entry.get())
            self.value_entry.delete(0, tk.END)
            
            bst_success = self.bst.insert(value)
            avl_success = self.avl.insert(value)
            
            if not bst_success or not avl_success:
                messagebox.showwarning("Duplicate Value", 
                    f"Value {value} already exists in the tree!",
                    parent=self)
            
            self.draw_trees()
            self.update_metrics()
            self.value_entry.focus()
            
        except ValueError:
            messagebox.showerror("Invalid Input", 
                "Please enter a valid integer!",
                parent=self)

    def find_value(self):
        try:
            value = int(self.value_entry.get())
            self.value_entry.delete(0, tk.END)
            
            bst_path = self.bst.find_path(value)
            avl_path = self.avl.find_path(value)
            
            self.draw_trees(highlight_paths={'bst': bst_path, 'avl': avl_path})
            self.update_metrics()
            
            if not bst_path or not avl_path:
                messagebox.showinfo("Find Result", 
                    f"Value {value} not found in the trees.",
                    parent=self)
            
            self.value_entry.focus()
            
        except ValueError:
            messagebox.showerror("Invalid Input", 
                "Please enter a valid integer!",
                parent=self)

    def delete_value(self):
        try:
            value = int(self.value_entry.get())
            self.value_entry.delete(0, tk.END)
            
            bst_success = self.bst.delete(value)
            avl_success = self.avl.delete(value)
            
            if not bst_success or not avl_success:
                messagebox.showwarning("Value Not Found", 
                    f"Value {value} not found in the tree!",
                    parent=self)
            
            self.draw_trees()
            self.update_metrics()
            self.value_entry.focus()
            
        except ValueError:
            messagebox.showerror("Invalid Input", 
                "Please enter a valid integer!",
                parent=self)

    def insert_random(self):
        value = random.randint(1, 100)
        attempts = 0
        max_attempts = 100
        
        while attempts < max_attempts:
            if self.bst.insert(value) and self.avl.insert(value):
                break
            value = random.randint(1, 100)
            attempts += 1
        
        if attempts >= max_attempts:
            messagebox.showwarning("Operation Failed", 
                "Could not find a unique random value to insert.",
                parent=self)
        
        self.draw_trees()
        self.update_metrics()
# /////////////////////////
# In the TreeComparisonVisualizer class, update the run_stress_test method:

    def run_stress_test(self):
        response = messagebox.askyesno("Confirm Stress Test",
            "This will insert 20 random values into both trees. Continue?",
            parent=self)
        
        if not response:
            return
        
        # Reset metrics
        self.bst.metrics.reset()
        self.avl.metrics.reset()
        
        # Create progress window
        progress_window = tk.Toplevel(self)
        progress_window.title("Stress Test Progress")
        progress_window.geometry("300x150")
        progress_window.transient(self)
        progress_window.grab_set()
        
        # Center progress window
        progress_window.update_idletasks()
        x = self.winfo_x() + (self.winfo_width() - progress_window.winfo_width()) // 2
        y = self.winfo_y() + (self.winfo_height() - progress_window.winfo_height()) // 2
        progress_window.geometry(f"+{x}+{y}")
        
        # Setup progress bar
        ttk.Label(progress_window, text="Inserting random values...", 
                style="Header.TLabel").pack(pady=10)
        progress_var = tk.IntVar()
        progress_bar = ttk.Progressbar(progress_window, length=200, 
                                    mode='determinate', variable=progress_var)
        progress_bar.pack(pady=10)
        
        def update_progress(current, total):
            progress_var.set((current / total) * 100)
            progress_window.update()
        
        try:
            # Use a set to track used values
            used_values = set()
            total_insertions = 20
            
            for i in range(total_insertions):
                # Generate a new random value that hasn't been used
                while True:
                    value = random.randint(1, 100)
                    if value not in used_values:
                        break
                
                # Add value to used set
                used_values.add(value)
                
                # Insert into both trees
                try:
                    self.bst.insert(value)
                    self.avl.insert(value)
                    
                    # Update visualization every 5 operations
                    if (i + 1) % 5 == 0:
                        self.draw_trees()
                        self.update_metrics()
                    
                    # Update progress
                    update_progress(i + 1, total_insertions)
                    
                except Exception as e:
                    print(f"Error inserting value {value}: {str(e)}")
                    continue
            
            # Final update
            self.draw_trees()
            self.update_metrics()
            
        except Exception as e:
            messagebox.showerror("Error", 
                f"An error occurred during stress test: {str(e)}",
                parent=self)
        finally:
            progress_window.destroy()
        
        messagebox.showinfo("Stress Test", 
            "Stress test completed successfully!",
            parent=self)


        # ////////////////////

    def reset_trees(self):
        response = messagebox.askyesno("Confirm Reset",
            "Are you sure you want to reset both trees?",
            parent=self)
        
        if response:
            self.bst = BST()
            self.avl = AVLTree()
            self.draw_trees()
            self.update_metrics()
            messagebox.showinfo("Reset Complete", 
                "Trees have been reset successfully!",
                parent=self)

    def draw_tree(self, canvas, tree, highlight_path=None):
        canvas.delete("all")
        
        title_text = "Binary Search Tree" if isinstance(tree, BST) else "AVL Tree"
        canvas.create_text(20, 20, text=title_text, 
                         font=Styles.HEADER_FONT, anchor="w")
        
        def draw_node(node, is_avl=False):
            if not node:
                return
            
            if node.left:
                is_path_edge = (highlight_path and 
                              node in highlight_path and 
                              node.left in highlight_path)
                edge_color = Styles.HIGHLIGHT_PATH_COLOR if is_path_edge else Styles.EDGE_COLOR
                edge_width = 3 if is_path_edge else 2
                
                canvas.create_line(node.x, node.y, 
                                 node.left.x, node.left.y,
                                 width=edge_width, fill=edge_color)
            
            if node.right:
                is_path_edge = (highlight_path and 
                              node in highlight_path and 
                              node.right in highlight_path)
                edge_color = Styles.HIGHLIGHT_PATH_COLOR if is_path_edge else Styles.EDGE_COLOR
                edge_width = 3 if is_path_edge else 2
                
                canvas.create_line(node.x, node.y, 
                                 node.right.x, node.right.y,
                                 width=edge_width, fill=edge_color)
            
            is_highlight = highlight_path and node in highlight_path
            is_target = highlight_path and node == highlight_path[-1]
            
            if is_target:
                fill_color = Styles.FOUND_NODE_FILL
                border_color = Styles.FOUND_NODE_BORDER
            elif is_highlight:
                fill_color = Styles.PATH_NODE_FILL
                border_color = Styles.HIGHLIGHT_PATH_COLOR
            else:
                fill_color, border_color = Styles.get_node_colors(is_avl, 
                                                            node.height if is_avl else 1)
            
            canvas.create_oval(node.x - tree.node_radius, 
                             node.y - tree.node_radius,
                             node.x + tree.node_radius, 
                             node.y + tree.node_radius,
                             fill=fill_color, 
                             outline=border_color,
                             width=3 if is_highlight else 2)
            
            text_color = "#FFFFFF" if is_target else "#000000"
            text = str(node.value)
            if is_avl:
                canvas.create_text(node.x, node.y + 15,
                                 text=f"h={node.height}",
                                 font=Styles.NORMAL_FONT,
                                 fill=text_color)
            
            canvas.create_text(node.x, node.y - (5 if is_avl else 0),
                             text=text,
                             font=Styles.NODE_FONT,
                             fill=text_color)
            
            draw_node(node.left, is_avl)
            draw_node(node.right, is_avl)
        
        draw_node(tree.root, isinstance(tree, AVLTree))
        self._center_tree(canvas)

    def _center_tree(self, canvas):
        bbox = canvas.bbox('all')
        if bbox:
            canvas_width = canvas.winfo_width()
            canvas_height = canvas.winfo_height()
            if bbox[2] - bbox[0] > 0:
                scale = min((canvas_width - 80) / (bbox[2] - bbox[0]),
                          (canvas_height - 80) / (bbox[3] - bbox[1]))
                canvas.scale('all', bbox[0], bbox[1], scale, scale)
            
            bbox = canvas.bbox('all')
            if bbox:
                dx = (canvas_width - (bbox[2] + bbox[0])) / 2
                dy = (canvas_height - (bbox[3] + bbox[1])) / 2
                canvas.move('all', dx, dy)

    def draw_trees(self, highlight_paths=None):
        if highlight_paths is None:
            highlight_paths = {'bst': None, 'avl': None}
        
        self.draw_tree(self.canvas_bst, self.bst, highlight_paths['bst'])
        self.draw_tree(self.canvas_avl, self.avl, highlight_paths['avl'])

    def update_metrics(self):
        self.performance_panel.update_metrics(self.bst.metrics, self.avl.metrics)

if __name__ == "__main__":
    app = TreeComparisonVisualizer()
    # Add keyboard shortcuts
    app.bind('<Return>', lambda e: app.insert_value())
    app.bind('<Delete>', lambda e: app.delete_value())
    app.bind('<Control-r>', lambda e: app.insert_random())
    app.bind('<Control-f>', lambda e: app.find_value())
    app.bind('<Control-t>', lambda e: app.run_stress_test())
    app.bind('<Escape>', lambda e: app.reset_trees())
    
    # Give initial focus to entry
    app.value_entry.focus()
    
    # Run the application
    app.mainloop()