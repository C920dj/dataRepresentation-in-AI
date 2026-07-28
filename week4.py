maze = {"A": ["B"], "B": ["A", "C"], "C":["B", "D"], "D":["C"]}

start, goal = "A", "D"

frontier = maze[start]
search_space = list(maze.keys())

print(frontier)
print(search_space)
print(goal in frontier)

current = start
path = [current]

while current != goal:
    frontier = maze[current]
    for neighbor in frontier:
        if neighbor not in path:
            current = neighbor
            path.append(current)
            break
print(path)
print(current == goal)
