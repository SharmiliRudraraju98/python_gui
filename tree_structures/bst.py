# tree_structures/bst.py
from typing import Optional, List
from .base_tree import BaseTree
from .node import Node
from metrics.performance_metrics import PerformanceMetrics

class BST(BaseTree):
    def __init__(self):
        super().__init__()
        self.metrics = PerformanceMetrics()
    
    def insert(self, value) -> bool:
        if self.contains(value):
            return False
        
        start_time = self.metrics.start_operation()
        try:
            if not self.root:
                self.root = Node(value)
            else:
                self._insert_recursive(self.root, value)
            self._update_positions()
        finally:
            self.metrics.end_operation('insert', start_time)
        
        return True
    
    def delete(self, value) -> bool:
        if not self.contains(value):
            return False
        
        start_time = self.metrics.start_operation()
        try:
            self.root = self._delete_recursive(self.root, value)
            self._update_positions()
        finally:
            self.metrics.end_operation('delete', start_time)
        
        return True
    
    def find_path(self, value) -> Optional[List[Node]]:
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
            self.metrics.end_operation('find', start_time)
    
    def _insert_recursive(self, node, value):
        self.metrics.increment_comparisons()
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)
    
    def _delete_recursive(self, node, value):
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
        
        return node
    
    def _find_min(self, node):
        current = node
        while current.left:
            self.metrics.increment_comparisons()
            current = current.left
        return current
    def find_path(self, value) -> Optional[List[Node]]:

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