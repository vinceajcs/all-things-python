def canVisitAllRooms(self, rooms):
    """
    :type rooms: List[List[int]]
    :rtype: bool
    """
    stack = [0]  # start in room 0
    visited = set(stack)

    while stack:
        room = stack.pop()
        for i in rooms[room]:
            if i not in visited:
                stack.append(i)
                visited.add(i)
                if len(visited) == len(rooms):
                    return True

    return len(visited) == len(rooms)
