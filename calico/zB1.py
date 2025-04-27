import math

def cross(o, a, b):
    ox, oy = o
    ax, ay = a
    bx, by = b
    return (ax - ox) * (by - oy) - (ay - oy) * (bx - ox)

def distance(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

def dot(u, v):
    return u[0] * v[0] + u[1] * v[1]

def compute_convex_hull(points):
    points.sort()
    chain = []

    for p in points + points[::-1]:
        while len(chain) >= 2 and cross(chain[-2], chain[-1], p) <= 0:
            chain.pop()
        chain.append(p)
    
    return chain[:-1]

def rotating_calipers(hull):
    n = len(hull)
    if n <= 1:
        return 0.0
    if n == 2:
        return 0.0

    min_area = float('inf')
    k = 1

    for i in range(n):
        ni = (i + 1) % n
        dx, dy = hull[ni][0] - hull[i][0], hull[ni][1] - hull[i][1]
        edge_len = math.hypot(dx, dy)
        direction = (dx / edge_len, dy / edge_len)

        while True:
            next_k = (k + 1) % n
            if abs(cross(hull[i], hull[ni], hull[next_k])) > abs(cross(hull[i], hull[ni], hull[k])):
                k = next_k
            else:
                break

        min_proj, max_proj = 0, 0
        max_width = 0

        for pt in hull:
            proj = dot((pt[0] - hull[i][0], pt[1] - hull[i][1]), direction)
            min_proj = min(min_proj, proj)
            max_proj = max(max_proj, proj)
            height = abs(cross(hull[i], hull[ni], pt)) / edge_len
            max_width = max(max_width, height)

        area = (max_proj - min_proj) * max_width
        min_area = min(min_area, area)

    return min_area

def process_test_case():
    n = int(input())
    points = [tuple(map(float, input().split())) for _ in range(n)]
    hull = compute_convex_hull(points)
    result = rotating_calipers(hull)
    print(f"{result:.10f}")

def main():
    t = int(input())
    for _ in range(t):
        process_test_case()

if __name__ == "__main__":
    main()
