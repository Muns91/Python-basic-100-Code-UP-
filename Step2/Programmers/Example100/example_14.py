def solution(n, k, cmd):
    state = ["O"] * n

    # 링크드 리스트 구성 요소
    nodes = {i: {'prev': i-1, 'next': i+1} for i in range(n)}
    nodes[0]['prev'] = None
    nodes[n-1]['next'] = None

    # 초기 위치 설정
    current = k

    recycle_bin = []

    for command in cmd:
        if command[0] == "D":  # Down
            move = int(command.split()[1])
            for _ in range(move):
                if nodes[current]['next'] is not None:
                    current = nodes[current]['next']
        elif command[0] == "U":  # Up
            move = int(command.split()[1])
            for _ in range(move):
                if nodes[current]['prev'] is not None:
                    current = nodes[current]['prev']
        elif command == "C":  # Delete
            state[current] = "X"
            recycle_bin.append(current)
            prev_node = nodes[current]['prev']
            next_node = nodes[current]['next']

            if prev_node is not None:
                nodes[prev_node]['next'] = next_node
            if next_node is not None:
                nodes[next_node]['prev'] = prev_node

            current = next_node if next_node is not None else prev_node

        elif command == "Z":  # Undo delete
            node = recycle_bin.pop()
            state[node] = "O"
            prev_node = nodes[node]['prev']
            next_node = nodes[node]['next']

            if prev_node is not None:
                nodes[prev_node]['next'] = node
            if next_node is not None:
                nodes[next_node]['prev'] = node

    result = ''.join(state)

    return result