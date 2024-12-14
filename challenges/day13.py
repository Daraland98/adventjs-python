'''The elves at the North Pole have created a special robot 🤖 that helps Santa Claus distribute gifts inside a large warehouse. The robot moves on a 2D plane and we start from the origin (0, 0).

We want to know if, after executing a series of movements, the robot returns to exactly where it started.

The robot's basic commands are:

L: Move to the left
R: Move to the right
U: Move upwards
D: Move downwards
But it also has certain modifiers for the movements:

*: The movement is done with double intensity (e.g., *R means RR)
!: The next movement is inverted (e.g., R!L is considered as RR)
?: The next movement is done only if it hasn't been done before (e.g., R?R means R)
Note: When the movement is inverted with ! the inverted movement is counted and not the original one. For example, !U?U inverts the U movement, so it counts as having done the D movement but not the U. Thus, !U?U translates to D?U, and therefore, the final U movement is done.

You must return:

true: if the robot returns exactly to where it started
[x, y]: if the robot does not return to where it started, return the position where it stopped'''

def is_robot_back(moves: str) -> bool | list[int]:
    position = [0, 0]  # Inicialmente en el origen (0, 0)
    executed_moves = set()  # Para registrar movimientos realizados con '?'
    invert_next = False  # Indica si el próximo movimiento debe invertirse

    # Mapeo de movimientos a cambios de posición
    move_map = {
        'L': (-1, 0), 'R': (1, 0), 
        'U': (0, 1), 'D': (0, -1)
    }
    inverse_map = {
        'L': 'R', 'R': 'L',
        'U': 'D', 'D': 'U'
    }

    i = 0
    while i < len(moves):
        move = moves[i]

        if move == '*':  # Movimiento doble
            if i + 1 < len(moves) and moves[i + 1] in move_map:
                next_move = moves[i + 1]
                position[0] += 2 * move_map[next_move][0]
                position[1] += 2 * move_map[next_move][1]
                executed_moves.add(next_move)
                i += 1  # Saltar el siguiente movimiento porque ya se ejecutó
        elif move == '!':  # Invertir el siguiente movimiento
            invert_next = True
        elif move == '?':  # Ejecutar sólo si no se hizo antes
            if i + 1 < len(moves) and moves[i + 1] in move_map:
                next_move = moves[i + 1]
                if next_move not in executed_moves:
                    position[0] += move_map[next_move][0]
                    position[1] += move_map[next_move][1]
                    executed_moves.add(next_move)
                i += 1  # Saltar el siguiente movimiento porque ya se verificó
        elif move in move_map:  # Movimiento normal
            actual_move = move
            if invert_next:  # Invertir si es necesario
                actual_move = inverse_map[move]
                invert_next = False  # Resetear el modificador de inversión
            position[0] += move_map[actual_move][0]
            position[1] += move_map[actual_move][1]
            executed_moves.add(actual_move)

        i += 1  # Avanzar al siguiente carácter

    # Verificar si volvió al origen
    return True if position == [0, 0] else position


# Step-by-step examples:
print(is_robot_back('R!U?U')) # [1,0]
# 'R'  -> moves to the right 
# '!U' -> inverts and becomes 'D'
# '?U' -> moves upwards, because the 'U' movement hasn't been done yet

print(is_robot_back('UU!U?D')) # [0,1]
# 'U'  -> moves upwards
# 'U'  -> moves upwards
# '!U' -> inverts and becomes 'D'
# '?D' -> does not move, since the 'D' movement has already been done

print(is_robot_back('R')) # [1, 0]
print(is_robot_back('RL')) # true
print(is_robot_back('RLUD')) # true
print(is_robot_back('*RU')) # [2, 1]
print(is_robot_back('R*U')) # [1, 2]
print(is_robot_back('LLL!R')) # [-4, 0]
print(is_robot_back('R?R')) # [1, 0]
print(is_robot_back('U?D')) # true
print(is_robot_back('R!L')) # [2,0]
print(is_robot_back('U!D')) # [0,2]
print(is_robot_back('R?L')) # true
print(is_robot_back('U?U')) # [0,1]
print(is_robot_back('*U?U')) # [0,2]
print(is_robot_back('U?D?U')) # true