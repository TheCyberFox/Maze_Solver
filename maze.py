# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 07:45:28 2020

@author: mkolta
"""

# def reachable(current_pos, direction):
#     global maze
#     curr_string = maze[current_pos[0]][current_pos[1]]
#     if direction == "R":
#         if curr_string.find("|") == -1 and current_pos[0] < len(maze) - 1:
#             return True
#         else:
#             return False
#     elif direction == "U":
#         if curr_string.find("¯") == -1 and current_pos[1] > 0:
#             return True
#         else:
#             return False
#     elif direction == "L":
#         if current_pos[0] > 0:
#             if maze[current_pos[0] - 1][current_pos[1]].find("|") == -1:
#                 return True
#             else:
#                 return False
#         else:
#             return False
#     elif direction == "D":
#         if current_pos[1] < len(maze[0]) - 1:
#             if maze[current_pos[0]][current_pos[1] + 1].find("¯") == -1:
#                 return True
#             else:
#                 return False
#         else:
#             return False
#     else:
#         return False


maze1 = [["S ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
         ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "¯ "],
         ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
         ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
         ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
         ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
         ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
         ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
         ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
         ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", " E"]]

maze = [["¯ ", "¯ ", "¯ ", "¯ ", "¯ ", "¯ ", "¯ ", "¯ ", "¯ ", "¯|"],
        [" |", "¯ ", "¯ ", "¯ ", "¯ ", "¯ ", "¯ ", "¯ ", "¯ ", " |"],
        [" |", "  ", "¯ ", "¯ ", "¯ ", "¯|", "¯ ", "¯ ", "¯ ", " |"],
        [" |", "¯ ", "¯ ", "¯ ", " |", "¯ ", "¯ ", "¯ ", "¯ ", "¯|"],
        [" |", "  ", "  ", "  ", " |", "  ", "¯|", "¯ ", "¯|", " |"],
        [" |", "  ", "  ", "  ", "  ", "¯ ", "¯ ", "¯ ", "¯ ", " |"],
        [" |", "¯ ", "¯ ", "¯ ", "¯ ", "¯ ", "¯ ", "¯ ", "¯ ", " |"],
        [" |", " |", "¯ ", "¯|", "¯ ", "¯|", "¯|", "¯|", "¯ ", " |"],
        [" |", " |", " |", " |", " |", " |", "  ", " |", "  ", "¯|"],
        [" |", "  ", " |", "  ", " |", "  ", "¯ ", "  ", "¯ ", " |"]]


class Cell:

    def __init__(self, current_pos, maze_local, took_path=None, parent=None):
        self.maze_local = maze_local
        self.current_pos = current_pos
        self.parent = parent
        self.possible_paths = {"L": self.reachable("L"), "R": self.reachable("R"), "U": self.reachable("U"),
                               "D": self.reachable("D")}
        if took_path == "D":
            self.possible_paths["U"] = False
        elif took_path == "U":
            self.possible_paths["D"] = False
        elif took_path == "R":
            self.possible_paths["L"] = False
        elif took_path == "L":
            self.possible_paths["R"] = False

    def get_pos(self):
        return self.current_pos

    def get_parent(self):
        return self.parent

    def get_possible_paths(self):
        return self.possible_paths

    def set_possible_paths(self, direction, possible):
        self.possible_paths[direction] = possible

    def reachable(self, direction):
        curr_string = self.maze_local[self.current_pos[0]][self.current_pos[1]]
        if direction == "R":
            if not (curr_string.find("|") == -1 and self.current_pos[1] < len(self.maze_local[0]) - 1):
                return False
        elif direction == "U":
            if not (curr_string.find("¯") == -1 and self.current_pos[0] > 0):
                return False
        elif direction == "L":
            if self.current_pos[1] > 0:
                if not self.maze_local[self.current_pos[0]][self.current_pos[1] - 1].find("|") == -1:
                    return False
            else:
                return False
        elif direction == "D":
            if self.current_pos[0] < len(self.maze_local) - 1:
                if not self.maze_local[self.current_pos[0] + 1][(self.current_pos[1])].find("¯") == -1:
                    return False
            else:
                return False
        return True

    def is_end(self):
        if self.current_pos == [len(self.maze_local) - 1, len(self.maze_local[0]) - 1]:
            return True


def solve_maze(solve_path, maze_to_solve):
    maze_h = len(maze_to_solve)
    maze_w = len(maze_to_solve[1])

    cell_list = [Cell([0, 0], maze_to_solve)]
    best_path = []
    path_taken = []
    if solve_path == "BFS":
        print("Starting BFS")
    else:
        print("Starting DFS")
    while not len(cell_list) == 0:
        if solve_path == "BFS":
            cell = cell_list.pop(0)
        else:
            cell = cell_list.pop()
        path_taken.append(cell)
        if cell.is_end():
            best_path.append(cell)
            while not cell.get_parent() is None:
                best_path.insert(0, cell.get_parent())
                cell = cell.parent
            i = 1
            print("FOUND THE END! Best Path Found Listed Below:")
            print_path(best_path)
            print()
            print("This is the path it travelled:")
            print_path(path_taken)

            break

        for path, possible in cell.get_possible_paths().items():
            path_exists = False
            if possible:
                if path == "D":
                    for item in path_taken:
                        if item.current_pos == [cell.current_pos[0] + 1, cell.current_pos[1]]:
                            item.set_possible_paths("U", False)
                            cell.set_possible_paths(path, False)
                            path_exists = True
                    if not path_exists:
                        cell_list.append(
                            Cell([cell.current_pos[0] + 1, cell.current_pos[1]], maze_to_solve, path, cell))
                elif path == "U":
                    for item in cell_list:
                        if item.current_pos == [cell.current_pos[0] - 1, cell.current_pos[1]]:
                            item.set_possible_paths("D", False)
                            cell.set_possible_paths(path, False)
                            path_exists = True
                    if not path_exists:
                        cell_list.append(
                            Cell([cell.current_pos[0] - 1, cell.current_pos[1]], maze_to_solve, path, cell))
                elif path == "R":
                    for item in cell_list:
                        if item.current_pos == [cell.current_pos[0], cell.current_pos[1] + 1]:
                            item.set_possible_paths("L", False)
                            cell.set_possible_paths(path, False)
                            path_exists = True
                    if not path_exists:
                        cell_list.append(
                            Cell([cell.current_pos[0], cell.current_pos[1] + 1], maze_to_solve, path, cell))
                elif path == "L":
                    for item in cell_list:
                        if item.current_pos == [cell.current_pos[0], cell.current_pos[1] - 1]:
                            item.set_possible_paths("R", False)
                            cell.set_possible_paths(path, False)
                            path_exists = True
                    if not path_exists:
                        cell_list.append(
                            Cell([cell.current_pos[0], cell.current_pos[1] - 1], maze_to_solve, path, cell))


def print_path(traveled):
    i = 1
    for ea_cell in traveled:
        if not i == len(traveled):
            print(('%(num)s:%(pos)s' % {"num": i, "pos": (ea_cell.current_pos[1], ea_cell.current_pos[0])}),
                  end=", ")
        else:
            print(('%(num)s:%(pos)s' % {"num": i, "pos": (ea_cell.current_pos[1], ea_cell.current_pos[0])}))
        if i % 5 == 0:
            print()
        i += 1


def print_maze(maze):
    maze_row_len = len(maze[0])
    for x in range(0, maze_row_len + 1):
        print("__", end='')
    print("")
    for row in maze:
        print("|", end='')
        for c in row:
            print(c, end='')
        print("|")
    for x in range(0, maze_row_len + 1):
        print("¯¯", end='')
    print()


print_maze(maze)
solve_maze("BFS", maze)
print()
solve_maze("DFS", maze)
print()
print_maze(maze1)
solve_maze("BFS", maze1)
print()
solve_maze("DFS", maze1)
print()
