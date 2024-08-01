#!/usr/bin/python3
"""task 0"""


def canUnlockAll(boxes):
    """prototype"""
    visited = {0}
    queue = [boxes[0]]
    while queue:
        box = queue.pop(0)
        for key in box:
            if key not in visited and key < len(boxes):
                visited.add(key)
                queue.append(boxes[key])
                return len(visited) == len(boxes)
