navigate_pot1_prompt = """Following these instructions, if we return to the starting point, return 'yes'; else return 'no'.

def left_rotate(face_direct):
    face_direct = tuple(face_direct)
    mapping_dict = {(1, 0): (0, 1), (0, 1): (-1, 0), (-1, 0): (0, -1), (0, -1): (1, 0)}
    return list(mapping_dict[face_direct])

def right_rotate(face_direct):
    face_direct = tuple(face_direct)
    mapping_dict = {(1, 0): (0, -1), (0, 1): (1, 0), (-1, 0): (0, 1), (0, -1): (-1, 0)}
    return list(mapping_dict[face_direct])

def around_rotate(face_direct):
    face_direct = tuple(face_direct)
    mapping_dict = {(1, 0): (-1, 0), (0, 1): (0, -1), (-1, 0): (1, 0), (0, -1): (0, 1)}
    return list(mapping_dict[face_direct])

def move_steps(current_position, face_direct, step, step_direct=''):
    new_list = []
    if step_direct == 'left':
        face_direct = left_rotate(face_direct)
    elif step_direct == 'right':
        face_direct = right_rotate(face_direct)
    elif step_direct == 'backward':
        face_direct = around_rotate(face_direct)
    for i in range(len(current_position)):
        new_list.append(current_position[i] + face_direct[i] * step)
    return new_list

# Instruction: Take 1 step. Take 2 steps. Take 3 steps. Turn around. Take 6 steps. Turn left.
# Python code, return ans
start_position = [0, 0]
current_position = start_position
# assume the start face is to x-positive
face_direct = [1, 0]
# Take 1 step.
current_position = move_steps(current_position, face_direct, 1)
# Take 2 steps.
current_position = move_steps(current_position, face_direct, 2)
# Take 3 steps.
current_position = move_steps(current_position, face_direct, 3)
# Turn around.
face_direct = around_rotate(face_direct)
# Take 6 steps.
current_position = move_steps(current_position, face_direct, 6)
# Turn left. Now the face is to y-positive
face_direct = left_rotate(face_direct)
ans = 'yes' if current_position == start_position else 'no'

# Instruction: Always face forward. Take 1 step left. Take 3 steps left. Take 5 steps left. Take 9 steps right.
# Python code, return ans
start_position = [0, 0]
current_position = start_position
# assume the start face is to x-positive
face_direct = [1, 0]
# Take 1 step left
current_position = move_steps(current_position, face_direct, 1, 'left')
# Take 3 steps left
current_position = move_steps(current_position, face_direct, 3, 'left')
# Take 5 steps left.
current_position = move_steps(current_position, face_direct, 5, 'left')
# Take 9 steps right.
current_position = move_steps(current_position, face_direct, 9, 'right')
ans = 'yes' if current_position == start_position else 'no'

# Instruction: Take 10 steps. Turn right. Take 2 steps. Turn around. Turn around.
# Python code, return ans
start_position = [0, 0]
current_position = start_position
# assume the start face is to x-positive
face_direct = [1, 0]
# Take 10 steps.
current_position = move_steps(current_position, face_direct, 10)
# Turn right.
face_direct = right_rotate(face_direct)
# Take 2 steps.
current_position = move_steps(current_position, face_direct, 2)
# Turn around.
face_direct = around_rotate(face_direct)
# Turn around.
face_direct = around_rotate(face_direct)
ans = 'yes' if current_position == start_position else 'no'

# Instruction: Always face forward. Take 10 steps left. Take 10 steps right. Take 7 steps backward. Take 7 steps forward.
# Python code, return ans
start_position = [0, 0]
current_position = start_position
# assume the start face is to x-positive
face_direct = [1, 0]
# Take 10 steps left.
current_position = move_steps(current_position, face_direct, 10, 'left')
# Take 10 steps right.
current_position = move_steps(current_position, face_direct, 10, 'right')
# Take 7 steps backward.
current_position = move_steps(current_position, face_direct, 7, 'backward')
# Take 7 steps forward.
current_position = move_steps(current_position, face_direct, 7, 'forward')
ans = 'yes' if current_position == start_position else 'no'

# Instruction: Turn left. Turn around. Take 3 steps. Turn around. Take 3 steps. Take 7 steps. Turn around. Take 7 steps.
# Python code, return ans
start_position = [0, 0]
current_position = start_position
# assume the start face is to x-positive
face_direct = [1, 0]
# Turn left.
face_direct = left_rotate(face_direct)
# Turn around.
face_direct = around_rotate(face_direct)
# Take 3 steps.
current_position = move_steps(current_position, face_direct, 3)
# Turn around.
face_direct = around_rotate(face_direct)
# Take 3 steps.
current_position = move_steps(current_position, face_direct, 3)
# Take 7 steps.
current_position = move_steps(current_position, face_direct, 7)
# Turn around.
face_direct = around_rotate(face_direct)
# Take 7 steps.
current_position = move_steps(current_position, face_direct, 7)
ans = 'yes' if current_position == start_position else 'no'

# Instruction: Always face forward. Take 5 steps right. Take 8 steps backward. Take 1 step right. Take 7 steps backward.
# Python code, return ans
start_position = [0, 0]
current_position = start_position
# assume the start face is to x-positive
face_direct = [1, 0]
# Take 5 steps right.
current_position = move_steps(current_position, face_direct, 5, 'right')
# Take 8 steps backward.
current_position = move_steps(current_position, face_direct, 8, 'backward')
# Take 1 step right.
current_position = move_steps(current_position, face_direct, 1, 'right')
# Take 7 steps backward.
current_position = move_steps(current_position, face_direct, 7, 'backward')
ans = 'yes' if current_position == start_position else 'no'

"""

navigate_pot2_prompt = """Following these instructions, if we return to the starting point, return 'yes'; else return 'no'.
def left_rotate(face_direct):
    face_direct = tuple(face_direct)
    mapping_dict = {(1, 0): (0, 1), (0, 1): (-1, 0), (-1, 0): (0, -1), (0, -1): (1, 0)}
    return list(mapping_dict[face_direct])

def right_rotate(face_direct):
    face_direct = tuple(face_direct)
    mapping_dict = {(1, 0): (0, -1), (0, 1): (1, 0), (-1, 0): (0, 1), (0, -1): (-1, 0)}
    return list(mapping_dict[face_direct])

def around_rotate(face_direct):
    face_direct = tuple(face_direct)
    mapping_dict = {(1, 0): (-1, 0), (0, 1): (0, -1), (-1, 0): (1, 0), (0, -1): (0, 1)}
    return list(mapping_dict[face_direct])

def move_steps(current_position, face_direct, step, step_direct=''):
    new_list = []
    if step_direct == 'left':
        face_direct = left_rotate(face_direct)
    elif step_direct == 'right':
        face_direct = right_rotate(face_direct)
    elif step_direct == 'backward':
        face_direct = around_rotate(face_direct)
    for i in range(len(current_position)):
        new_list.append(current_position[i] + face_direct[i] * step)
    return new_list

# Instruction: Always face forward. Take 4 steps forward. Take 9 steps right. Take 6 steps right. Take 8 steps right.
# Python code, return ans
start_position = [0, 0]
current_position = start_position
# assume the start face is to x-positive
face_direct = [1, 0]
# Take 4 steps forward.
current_position = move_steps(current_position, face_direct, 4, 'forward')
# Take 9 steps right.
current_position = move_steps(current_position, face_direct, 9, 'right')
# Take 6 steps right.
current_position = move_steps(current_position, face_direct, 3, 'right')
# Take 8 steps right.
current_position = move_steps(current_position, face_direct, 8, 'right')
ans = 'yes' if current_position == start_position else 'no'

# Instruction: Turn left. Take 6 steps. Take 1 step. Turn around. Turn around. Turn around. Take 7 steps.
# Python code, return ans
start_position = [0, 0]
current_position = start_position
# assume the start face is to x-positive
face_direct = [1, 0]
# Turn left.
face_direct = left_rotate(face_direct)
# Take 6 steps.
current_position = move_steps(current_position, face_direct, 6)
# Take 1 step.
current_position = move_steps(current_position, face_direct, 1)
# Turn around.
face_direct = around_rotate(face_direct)
# Turn around.
face_direct = around_rotate(face_direct)
# Turn around.
face_direct = around_rotate(face_direct)
# Take 7 steps.
current_position = move_steps(current_position, face_direct, 7)
ans = 'yes' if current_position == start_position else 'no'

# Instruction: Always face forward. Take 2 steps backward. Take 9 steps left. Take 2 steps left. Take 10 steps forward. Take 8 steps left. Take 4 steps forward.
# Python code, return ans
start_position = [0, 0]
current_position = start_position
# assume the start face is to x-positive
face_direct = [1, 0]
# Take 2 steps backward.
current_position = move_steps(current_position, face_direct, 1, 'backward')
# Take 9 steps left.
current_position = move_steps(current_position, face_direct, 9, 'left')
# Take 2 steps left.
current_position = move_steps(current_position, face_direct, 2, 'left')
# Take 10 steps forward.
current_position = move_steps(current_position, face_direct, 10)
# Take 8 steps left.
current_position = move_steps(current_position, face_direct, 8, 'left')
# Take 4 steps forward.
current_position = move_steps(current_position, face_direct, 4)
ans = 'yes' if current_position == start_position else 'no'

# Instruction: Turn around. Turn right. Take 5 steps. Take 2 steps.
start_position = [0, 0]
current_position = start_position
# assume the start face is to x-positive
face_direct = [1, 0]
# Turn around.
face_direct = around_rotate(face_direct)
# Turn right.
face_direct = right_rotate(face_direct)
# Take 5 steps.
current_position = move_steps(current_position, face_direct, 5)
# Take 2 steps.
current_position = move_steps(current_position, face_direct, 2)
ans = 'yes' if current_position == start_position else 'no'

# Instruction: Take 4 steps. Turn around. Turn left. Turn right. Turn right. Turn right. Turn around. Take 4 steps.
# Python code
start_position = [0, 0]
current_position = start_position
# assume the start face is to x-positive
face_direct = [1, 0]
# Take 4 steps
current_position = move_steps(current_position, face_direct, 4)
# Turn around
face_direct = around_rotate(face_direct)
# Turn left
face_direct = left_rotate(face_direct)
# Turn right
face_direct = right_rotate(face_direct)
# Turn right
face_direct = right_rotate(face_direct)
# Turn right
face_direct = right_rotate(face_direct)
# Turn around
face_direct = around_rotate(face_direct)
# Take 4 steps
current_position = move_steps(current_position, face_direct, 4)
ans = 'yes' if current_position == start_position else 'no'

# Instruction: Always face forward. Take 5 steps right. Take 5 steps backward. Take 5 steps forward. Take 5 steps left.
# Python code, return ans
start_position = [0, 0]
current_position = start_position
# assume the start face is to x-positive
face_direct = [1, 0]
# Take 5 steps right
current_position = move_steps(current_position, face_direct, 5, 'right')
# Take 5 steps backward
current_position = move_steps(current_position, face_direct, 5, 'backward')
# Take 5 steps forward
current_position = move_steps(current_position, face_direct, 5, 'forward')
# Take 5 steps left
current_position = move_steps(current_position, face_direct, 5, 'left')
ans = 'yes' if current_position == start_position else 'no'

"""

navigate_cot1_prompt = """Following these instructions, if we return to the starting point, return 'yes'; else return 'no'.
Instruction: Take 1 step. Take 2 steps. Take 3 steps. Turn around. Take 6 steps. Turn left.
Explain: start_position = [0, 0], assume the start face is to x-positive
1. Take 1 step. Current position is [1, 0]
2. Take 2 steps. Current position is [3, 0]
3. Take 3 steps. Current position is [6, 0]
4. Turn around. The face is to x-negative in the following steps.
5. Take 6 steps. Current position is [0, 0]
6. Turn left. The face is to y-negative in the following steps.
After all the steps, the position is [0, 0], same as the starting point.
Answer: yes

Instruction: Always face forward. Take 1 step left. Take 3 steps left. Take 5 steps left. Take 9 steps right.
Explain: start_position = [0, 0], assume the start face is to x-positive
1. Always face forward. The face is to x-positive in the following steps.
2. Take 1 step left. Current position is [-1, 0]
3. Take 3 steps left. Current position is [-4, 0]
4. Take 5 steps left. Current position is [-9, 0]
5. Take 9 steps right. Current position is [0, 0]
After all the steps, the position is [0, 0], same as the starting point.
Answer: yes

Instruction: Take 10 steps. Turn right. Take 2 steps. Turn around. Turn around.
Explain: start_position = [0, 0], assume the start face is to x-positive
1. Take 10 steps. Current position is [10, 0]
2. Turn right. The face is to y-negative in the following steps.
3. Take 2 steps. Current position is [10, -2]
4. Turn around. The face is to y-positive in the following steps.
5. Turn around. The face is to y-negative in the following steps.
After all the steps, the position is [10, -2], not the same as the starting point.
Answer: no

# Instruction: Always face forward. Take 10 steps left. Take 10 steps right. Take 7 steps backward. Take 7 steps forward.
Explain: start_position = [0, 0], assume the start face is to x-positive
1. Take 10 steps left. Current position is [0, 10]
2. Take 10 steps right. Current position is [0, 0]
3. Take 7 steps backward. Current position is [-7, 0]
4. Take 7 steps forward. Current position is [0, 0]
After all the steps, the position is [0, 0], same as the starting point.
Answer: yes

Instruction: Turn left. Turn around. Take 3 steps. Turn around. Take 3 steps. Take 7 steps. Turn around. Take 7 steps.
Explain: start_position = [0, 0], assume the start face is to x-positive
1. Turn left. The face is to y-positive in the following steps.
2. Turn around. The face is to y-negative in the following steps.
3. Take 3 steps. Current position is [0, -3]
4. Turn around. The face is to y-positive in the following steps.
5. Take 3 steps. Current position is [0, 0]
6. Take 7 steps. Current position is [0, 7]
7. Turn around. The face is to y-negative in the following steps.
8. Take 7 steps. Current position is [0, 0]
After all the steps, the position is [0, 0], same as the starting point.
Answer: yes

Instruction: Always face forward. Take 5 steps right. Take 8 steps backward. Take 1 step right. Take 7 steps backward.
Explain: start_position = [0, 0], assume the start face is to x-positive
1. Take 5 steps right. Current position is [0, -5]
2. Take 8 steps backward. Current position is [-8, -5]
3. Take 1 step right. Current position is [-8, -6]
4. Take 7 steps backward. Current position is [-15, -6]
After all the steps, the position is [-15, -6], not the same as the starting point.
Answer: no

"""

navigate_cot2_prompt = """Following these instructions, if we return to the starting point, return 'yes'; else return 'no'.
Instruction: Always face forward. Take 4 steps forward. Take 9 steps right. Take 6 steps right. Take 8 steps right.
Explain: start_position = [0, 0], assume the start face is to x-positive
1. Always face forward. The face is to x-positive in the following steps.
2. Take 4 steps forward. Current position is [4, 0]
3. Take 9 steps right. Current position is [4, 9]
4. Take 6 steps right. Current position is [4, 15]
5. Take 8 steps right. Current position is [4, 23]
After all the steps, the position is [4, 23], not the same as the starting point.
Answer: no

Instruction: Turn left. Take 6 steps. Take 1 step. Turn around. Turn around. Turn around. Take 7 steps.
Explain: start_position = [0, 0], assume the start face is to x-positive
1. Turn left. The face is to y-positive in the following steps.
2. Take 6 steps. Current position is [0, 6]
3. Take 1 step. Current position is [0, 7]
4. Turn around. The face is to y-negative in the following steps.
5. Turn around. The face is to y-positive in the following steps.
6. Turn around. The face is to y-negative in the following steps.
7. Take 7 steps. Current position is [0, 0]
After all the steps, the position is [0, 0], same as the starting point.
Answer: yes

Instruction: Always face forward. Take 2 steps backward. Take 9 steps left. Take 2 steps left. Take 10 steps forward. Take 8 steps left. Take 4 steps forward.
Explain: start_position = [0, 0], assume the start face is to x-positive
1. Take 2 steps backward. Current position is [-2, 0]
2. Take 9 steps left. Current position is [-2, 9]
3. Take 2 steps left. Current position is [-2, 11]
4. Take 10 steps forward. Current position is [8, 11]
5. Take 8 steps left. Current position is [8, 19]
5. Take 4 steps forward. Current position is [12, 19]
After all the steps, the position is [12, 19], not the same as the starting point.
Answer: no

Instruction: Turn around. Turn right. Take 5 steps. Take 2 steps.
Explain: start_position = [0, 0], assume the start face is to x-positive
1. Turn around. The face is to x-negative in the following steps.
2. Turn right. The face is to y-pegative in the following steps.
3. Take 5 steps. Current position is [0, 5]
4. Take 2 steps. Current position is [0, 7]
After all the steps, the position is [0, 7], not the same as the starting point.
Answer: no

Instruction: Take 4 steps. Turn around. Turn left. Turn right. Turn right. Turn right. Turn around. Take 4 steps.
Explain: start_position = [0, 0], assume the start face is to x-positive
1. Take 4 steps. Current position is [4, 0]
2. Turn around. The face is to x-negative in the following steps.
3. Turn left. The face is to y-negative in the following steps.
4. Turn right. The face is to x-negative in the following steps.
5. Turn right. The face is to y-positive in the following steps.
6. Turn right. The face is to x-positive in the following steps.
7. Turn around. The face is to x-negative in the following steps.
8. Take 4 steps. Current position is [0, 0]
After all the steps, the position is [0, 0], same as the starting point.
Answer: yes

Instruction: Always face forward. Take 5 steps right. Take 5 steps backward. Take 5 steps forward. Take 5 steps left.
Explain: start_position = [0, 0], assume the start face is to x-positive
1. Take 5 steps right. Current position is [0, 5]
2. Take 5 steps backward. Current position is [-5, 5]
3. Take 5 steps forward. Current position is [0, 5]
4. Take 5 steps left. Current position is [0, 0]
After all the steps, the position is [0, 0], same as the starting point.
Answer: yes

"""