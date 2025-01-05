# tree_structures/node.py
from dataclasses import dataclass
from typing import Optional

@dataclass
class Node:
    value: int
    x: float = 0
    y: float = 0
    height: int = 1
    left: Optional['Node'] = None
    right: Optional['Node'] = None