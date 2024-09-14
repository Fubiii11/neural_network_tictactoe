import csv
import numpy as np

def check_winner(board):

    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] != 0:
            return board[combo[0]]
    return 0

def minimax(board, depth, player):
    winner = check_winner(board)
    if winner == 1:
        return (10 - depth)
    elif winner == -1:
        return (depth - 10)
    if is_full(board):
        return 0

    if player == 1:
        best_score = -float('inf')
        for move in get_available_moves(board):
            board[move] = 1
            score = minimax(board, depth + 1, -1)
            board[move] = 0
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for move in get_available_moves(board):
            board[move] = -1
            score = minimax(board, depth + 1, 1)
            board[move] = 0
            best_score = min(best_score, score)
        return best_score

def find_best_move(board, player):
    best_move = -1
    if player == 1:
        best_score = -float('inf')
    else:
        best_score = float('inf')

    for move in get_available_moves(board):
        board[move] = player
        score = minimax(board, 0, -player)
        board[move] = 0

        if (player == 1 and score > best_score) or (player == -1 and score < best_score):
            best_score = score
            best_move = move

    return best_move

def is_full(board):
    return all(spot != 0 for spot in board)

def get_available_moves(board):
    return [i for i, spot in enumerate(board) if spot == 0]

def load_data(file):
    data = []
    with open(file, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            data.append([int(i) for i in row])
    return np.array(data)

#load data
x = load_data("bretter.csv")

updated_data=[]
for board in x:
    best_move = find_best_move(list(board), -1)
    updated_board = list(board) + [best_move]
    updated_data.append(updated_board)

def save_data(file, data):
    with open(file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)

save_data("updated_bretter.csv", updated_data)

