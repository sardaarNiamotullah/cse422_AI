import math
import random

student_id = list(map(int, input("Enter your student id: ")))

pointsToWin = (student_id[-1] * 10 + student_id[-2])                                                                    # points needed to win the match
numberOfShuffles = student_id[3]
minPoints_Optimus = student_id[4]                                                                                       # minimum points Optimus can achieve
maxPoints_Optimus = (student_id[-1] * 10 + student_id[-2]) * 1.5                                                        # maximum points Optimus can achieve
random_points = [random.randint(minPoints_Optimus, math.floor(maxPoints_Optimus)) for _ in range(8)]                    # generate 8 random points between minPoint and maxPoint of Optimus

MAX_VALUE, MIN_VALUE = 1000, -1000
def compute_minimax_score(depth, node_index, maximizing_player, node_values, alpha, beta):
    if depth == 3:
        return node_values[node_index]
    if maximizing_player:
        best_score = MIN_VALUE
        for i in range(2):
            score = compute_minimax_score(depth + 1, node_index * 2 + i, False, node_values, alpha, beta)
            best_score = max(best_score, score)
            alpha = max(alpha, best_score)
            if beta <= alpha:
                break
        return best_score
    else:
        best_score = MAX_VALUE
        for i in range(2):
            score = compute_minimax_score(depth + 1, node_index * 2 + i, True, node_values, alpha, beta)
            best_score = min(best_score, score)
            beta = min(beta, best_score)
            if beta <= alpha:
                break
        return best_score

achieved_point = compute_minimax_score(0, 0, True, random_points, MIN_VALUE, MAX_VALUE)

print(f'Generated 8 random points between minimum and maximum points limit: {random_points}')
print(f'Total points to win: {pointsToWin}')
print(f'Achive point by applying alpha-beta puring: {achieved_point}')
print('The Winner is Optimus Prime') if achieved_point >= pointsToWin else print('The winner is Megatron')

print('\nAfter the shuffle: ')
listOfPoints = []
for i in range(numberOfShuffles):
    random.shuffle(random_points)
    listOfPoints.append(compute_minimax_score(0, 0, True, random_points, MIN_VALUE, MAX_VALUE))

print(f'List of all points values from each shuffle: {listOfPoints}')
print(f'The maximum value of all shuffles: {max(listOfPoints)}')

numberOfWins = sum(1 for i in listOfPoints if i >= pointsToWin)

print(f'Won {numberOfWins} times out of {numberOfShuffles} number of shuffles')