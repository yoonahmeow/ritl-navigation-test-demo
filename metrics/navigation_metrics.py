import math

def compute_distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def evaluate_goal_accuracy(final_pose, goal_pose, threshold_cm):
    error = compute_distance(final_pose, goal_pose)
    return error <= threshold_cm
