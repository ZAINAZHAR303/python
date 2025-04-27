def solve():
    T = int(input()) 
    results = []
    
    for _ in range(T):
        N = int(input())
        result = 'u' + 'wu' * N
        results.append(result)
    
    
    print("\n".join(results))

if __name__ == "__main__":
    solve()
