from typing import Optional, Dict, List
import tkinter as tk
from .node import Node
from gui.styles import TreeVisualizerStyles as Styles


class BaseTree:
    def __init__(self):
        self.root = None
        self.node_radius = 20
        self.horizontal_spacing = 50
        self.vertical_spacing = 70
        self.tooltip = None

    def contains(self, value: int) -> bool:
        return self._contains_recursive(self.root, value)

    def _contains_recursive(self, node: Optional[Node], value: int) -> bool:
        if not node:
            return False
        if node.value == value:
            return True
        if value < node.value:
            return self._contains_recursive(node.left, value)
        return self._contains_recursive(node.right, value)

    def _update_positions(self):
        if not self.root:
            return
        
        # Track occupied horizontal positions at each level
        level_occupied_positions: Dict[int, List[float]] = {}
        
        def calculate_node_position(node, level, x_range_start, x_range_end):
            """
            Recursively calculate node positions with overlap prevention
            
            Args:
                node: Current node being positioned
                level: Current tree level (depth)
                x_range_start: Minimum allowed x position
                x_range_end: Maximum allowed x position
            
            Returns:
                float: The calculated x position for the node
            """
            if not node:
                return None
            
            # Calculate mid-point of allowed x range
            mid_x = (x_range_start + x_range_end) / 2
            
            # Determine y position based on level
            node.y = level * self.vertical_spacing
            
            # Initialize positions for this level if not exists
            if level not in level_occupied_positions:
                level_occupied_positions[level] = []
            
            # Find a suitable x position
            x_candidates = [mid_x]
            search_directions = [1, -1]  # Alternate searching left and right
            
            for direction in search_directions:
                for offset_multiplier in range(1, 10):  # Limit search range
                    offset = direction * offset_multiplier * (self.node_radius * 2 + self.horizontal_spacing)
                    candidate_x = mid_x + offset
                    
                    # Check if candidate is within original x range
                    if candidate_x < x_range_start or candidate_x > x_range_end:
                        break
                    
                    # Check for overlap with existing nodes at this level
                    if all(abs(candidate_x - pos) > self.node_radius * 2 + self.horizontal_spacing 
                           for pos in level_occupied_positions[level]):
                        x_candidates.append(candidate_x)
                        break
            
            # Select first valid x position
            node_x = x_candidates[0]
            
            # Register this position as occupied
            level_occupied_positions[level].append(node_x)
            node.x = node_x
            
            # Calculate child ranges dynamically
            if node.left:
                calculate_node_position(
                    node.left, 
                    level + 1, 
                    x_range_start, 
                    node_x - self.node_radius
                )
            
            if node.right:
                calculate_node_position(
                    node.right, 
                    level + 1, 
                    node_x + self.node_radius, 
                    x_range_end
                )
        
        # Initial call with full canvas width 
        # Assuming a reasonable initial canvas width of 1000
        calculate_node_position(self.root, 0, 0, 1000)

    def draw_tree(self, canvas, tree, highlight_path=None):
        canvas.delete("all")
        
        title_text = "Binary Search Tree" if isinstance(tree, self.BST) else "AVL Tree"
        canvas.create_text(20, 20, text=title_text, 
                         font=Styles.HEADER_FONT, anchor="w")
        
        def draw_node(node, is_avl=False):
            if not node:
                return
            
            # Draw edges
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
            
            # Determine node colors
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
            
            # Add hover functionality
            canvas.tag_bind(f"node_{id(node)}", "<Enter>", lambda e, n=node: self.show_tooltip(e, n.value))
            canvas.tag_bind(f"node_{id(node)}", "<Leave>", lambda e: self.hide_tooltip())
            
            canvas.create_oval(node.x - self.node_radius, 
                             node.y - self.node_radius,
                             node.x + self.node_radius, 
                             node.y + self.node_radius,
                             tags=f"node_{id(node)}",
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
        
        draw_node(tree.root, isinstance(tree, self.AVLTree))
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

    def show_tooltip(self, event, value):
        if self.tooltip:
            self.tooltip.destroy()
        
        self.tooltip = tk.Toplevel(event.widget)
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.geometry(f"+{event.x_root}+{event.y_root}")
        label = tk.Label(self.tooltip, text=f"Node Value: {value}", 
                        background="#FFFFDD", relief=tk.SOLID, borderwidth=1)
        label.pack()

    def hide_tooltip(self):
        if self.tooltip:
            self.tooltip.destroy()
            self.tooltip = None