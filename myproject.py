from collections import deque

def astaralgo(jug1_capacity, jug2_capacity, target):
    
    visited = set()
    
    path = []
    
    q = deque()
    
    q.append((0, 0))  
    while q:
        state = q.popleft()

       
        if state in visited:
            continue
       
        visited.add(state)

        
        path.append(state)
        jug1, jug2 = state

        if jug1 == target or jug2 == target:
            path.append(state)
            print_steps(path)
            return True

        
        
        q.append((jug1_capacity, jug2))
       
        q.append((jug1, jug2_capacity))
       
        q.append((0, jug2))
    
        q.append((jug1, 0))
      
        pour_to_jug2 = min(jug1, jug2_capacity - jug2)
        q.append((jug1 - pour_to_jug2, jug2 + pour_to_jug2))
    
        pour_to_jug1 = min(jug2, jug1_capacity - jug1)
        q.append((jug1 + pour_to_jug1, jug2 - pour_to_jug1))


    print("No solution.")
    return False

def print_steps(path):
    for step in path:
        print(f"Jug1: {step[0]} liters, Jug2: {step[1]} liters")

# Example usage
jug1_capacity = 7
jug2_capacity = 3
target = 5

print(bfs_solve(jug1_capacity, jug2_capacity, target))
