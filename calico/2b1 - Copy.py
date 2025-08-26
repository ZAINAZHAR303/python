import math

def cross_product(origin, point_a, point_b):
    return (point_a[0] - origin[0]) * (point_b[1] - origin[1]) - (point_a[1] - origin[1]) * (point_b[0] - origin[0])

def build_convex_hull(coords):
    coords = sorted(coords)
    lower_half = []
    for pt in coords:
        while len(lower_half) >= 2 and cross_product(lower_half[-2], lower_half[-1], pt) <= 0:
            lower_half.pop()
        lower_half.append(pt)

    upper_half = []
    for pt in reversed(coords):
        while len(upper_half) >= 2 and cross_product(upper_half[-2], upper_half[-1], pt) <= 0:
            upper_half.pop()
        upper_half.append(pt)

    return lower_half[:-1] + upper_half[:-1]

def euclidean_distance(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

def dot_product(p1, p2):
    return p1[0]*p2[0] + p1[1]*p2[1]

def find_min_area_rectangle(hull_points):
    total_points = len(hull_points)
    if total_points == 1:
        return 0.0
    if total_points == 2:
        return euclidean_distance(hull_points[0], hull_points[1]) * 0.0
    
    smallest_area = float('inf')
    next_point = 1

    for idx in range(total_points):
        next_idx = (idx + 1) % total_points
        vector_edge = (hull_points[next_idx][0] - hull_points[idx][0], hull_points[next_idx][1] - hull_points[idx][1])
        length_edge = math.hypot(vector_edge[0], vector_edge[1])
        unit_vector = (vector_edge[0] / length_edge, vector_edge[1] / length_edge)

        while True:
            next_candidate = (next_point + 1) % total_points
            if abs(cross_product(hull_points[idx], hull_points[next_idx], hull_points[next_candidate])) > abs(cross_product(hull_points[idx], hull_points[next_idx], hull_points[next_point])):
                next_point = next_candidate
            else:
                break

        min_proj = float('inf')
        max_proj = -float('inf')
        max_width = 0.0

        for corner in hull_points:
            proj_length = dot_product((corner[0] - hull_points[idx][0], corner[1] - hull_points[idx][1]), unit_vector)
            min_proj = min(min_proj, proj_length)
            max_proj = max(max_proj, proj_length)
            perp_width = abs(cross_product(hull_points[idx], hull_points[next_idx], corner)) / length_edge
            max_width = max(max_width, perp_width)

        current_area = (max_proj - min_proj) * max_width
        smallest_area = min(smallest_area, current_area)

    return smallest_area

def compute_min_rectangles():
    test_cases = int(input())
    for _ in range(test_cases):
        num_points = int(input())
        input_coords = []
        for _ in range(num_points):
            x_coord, y_coord = map(float, input().split())
            input_coords.append((x_coord, y_coord))
        
        convex_shape = build_convex_hull(input_coords)
        minimal_area = find_min_area_rectangle(convex_shape)
        print(f"{minimal_area:.10f}")

compute_min_rectangles()
