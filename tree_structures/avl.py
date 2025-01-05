# tree_structures/avl.py
from typing import Optional, List
from .base_tree import BaseTree
from .node import Node
from metrics.performance_metrics import PerformanceMetrics

class AVLTree(BaseTree):
    def __init__(self):
        super().__init__()
        self.metrics = PerformanceMetrics()
    
    def _get_height(self, node: Optional[Node]) -> int:
        if not node:
            return 0
        return node.height
    
    def _get_balance(self, node: Optional[Node]) -> int:
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)
    
    def _update_height(self, node: Optional[Node]) -> None:
        if not node:
            return
        node.height = max(self._get_height(node.left), 
                         self._get_height(node.right)) + 1
    
    def _rotate_right(self, y: Node) -> Node:
        self.metrics.increment_rotations()
        x = y.left
        T2 = x.right
        
        x.right = y
        y.left = T2
        
        self._update_height(y)
        self._update_height(x)
        
        return x
    
    def _rotate_left(self, x: Node) -> Node:
        self.metrics.increment_rotations()
        y = x.right
        T2 = y.left
        
        y.left = x
        x.right = T2
        
        self._update_height(x)
        self._update_height(y)
        
        return y
    
    def insert(self, value: int) -> bool:
        if self.contains(value):
            return False
        
        start_time = self.metrics.start_operation()
        try:
            self.root = self._insert_recursive(self.root, value)
            self._update_positions()
        finally:
            self.metrics.end_operation('insert', start_time)
        
        return True
    
    def find_path(self, value) -> Optional[List[Node]]:
        """
        Finds a value in the tree and returns the path taken to reach it.
        Also measures the time taken for the operation.
        Returns None if the value is not found.
        """
        # Start timing the find operation
        start_time = self.metrics.start_operation()
        
        try:
            if not self.root:
                return None
            
            path = []
            current = self.root
            
            while current:
                path.append(current)
                self.metrics.increment_comparisons()
                
                if value == current.value:
                    return path
                elif value < current.value:
                    current = current.left
                else:
                    current = current.right
            
            return None
        finally:
            # End timing and record the operation
            self.metrics.end_operation('find', start_time)
    
    def _insert_recursive(self, node: Optional[Node], value: int) -> Node:
        if not node:
            return Node(value)
        
        self.metrics.increment_comparisons()
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        else:
            node.right = self._insert_recursive(node.right, value)
        
        self._update_height(node)
        balance = self._get_balance(node)
        
        # Left Left Case
        if balance > 1 and value < node.left.value:
            return self._rotate_right(node)
        
        # Right Right Case
        if balance < -1 and value > node.right.value:
            return self._rotate_left(node)
        
        # Left Right Case
        if balance > 1 and value > node.left.value:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        
        # Right Left Case
        if balance < -1 and value < node.right.value:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        
        return node
    
    def delete(self, value: int) -> bool:
        if not self.contains(value):
            return False
        
        start_time = self.metrics.start_operation()
        try:
            self.root = self._delete_recursive(self.root, value)
            self._update_positions()
        finally:
            self.metrics.end_operation('delete', start_time)
        
        return True
    
    def _delete_recursive(self, node: Optional[Node], value: int) -> Optional[Node]:
        if not node:
            return None
        
        self.metrics.increment_comparisons()
        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            
            min_node = self._find_min(node.right)
            node.value = min_node.value
            node.right = self._delete_recursive(node.right, min_node.value)
        
        if not node:
            return None
        
        self._update_height(node)
        balance = self._get_balance(node)
        
        # Left Left Case
        if balance > 1 and self._get_balance(node.left) >= 0:
            return self._rotate_right(node)
        
        # Left Right Case
        if balance > 1 and self._get_balance(node.left) < 0:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        
        # Right Right Case
        if balance < -1 and self._get_balance(node.right) <= 0:
            return self._rotate_left(node)
        
        # Right Left Case
        if balance < -1 and self._get_balance(node.right) > 0:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        
        return node
    
    def _find_min(self, node: Node) -> Node:
        current = node
        while current.left:
            self.metrics.increment_comparisons()
            current = current.left
        return current