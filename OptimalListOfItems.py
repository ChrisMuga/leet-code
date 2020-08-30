from typing import List, Tuple

"""
    Given a container with a specific carrying capacity, w.
    And a list of items each with its own required capacity, v.
    What is the optimal list of items that does not exceed the capacity w.
    
    [
        (Kettle, 5),
        (Pot, 10),
        (Slab, 40),
        (Canister, 30),
        (Cylinder, 50)
    ]
    
    w = 90

"""

containers = [
    ('Kettle', 5, 10),
    ('Pot', 10, 25),
    ('Slab', 40, 18),
    ('Canister', 30, 30),
    ('Cylinder', 50, 25)
]

"TODO: Finish Exercise"

max_capacity = 90


def optimize(items: List[Tuple[str, int, int]], w: int) -> List[Tuple[str, int, int]]:
    sorted_containers = sorted(containers, key=lambda x: x[1])
    print(sorted_containers)
    print(items, w)


optimize(containers, max_capacity)
