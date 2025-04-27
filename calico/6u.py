def find_min_actions(rows: int, cols: int, drift_seq: str, board: list) -> int:
    
    
    label_to_position = {}
    for r in range(rows):
        for c in range(cols):
            label_to_position[board[r][c]] = (r, c)
    
    
    drift_directions = {
        'U': (-1, 0),
        'D': (1, 0),
        'L': (0, -1),
        'R': (0, 1),
    }
    drift_size = len(drift_seq)
    
    moves_needed = 0
    pos_row, pos_col = 0, 0 
    drift_step = 0  
    
    
    for num in range(1, rows * cols + 1):
        target_r, target_c = label_to_position[num]
        
        accumulated_r, accumulated_c = 0, 0
        steps = 0
        while True:
            
            new_row = (pos_row + accumulated_r) % rows
            new_col = (pos_col + accumulated_c) % cols
            
            
            row_dist = abs(new_row - target_r)
            row_dist = min(row_dist, rows - row_dist)
            col_dist = abs(new_col - target_c)
            col_dist = min(col_dist, cols - col_dist)
            actions_required = row_dist + col_dist
            
            if actions_required <= steps:
                break
            
            
            next_drift = (drift_step + steps) % drift_size
            move_r, move_c = drift_directions[drift_seq[next_drift]]
            accumulated_r += move_r
            accumulated_c += move_c
            steps += 1
        
        moves_needed += steps
        pos_row, pos_col = target_r, target_c
        drift_step = (drift_step + steps) % drift_size
    
    return moves_needed


def start():
    tests = int(input())
    for _ in range(tests):
        r, c = map(int, input().split())
        sequence = input().strip()
        matrix = [list(map(int, input().split())) for _ in range(r)]
        print(find_min_actions(r, c, sequence, matrix))


if __name__ == '__main__':
    start()
