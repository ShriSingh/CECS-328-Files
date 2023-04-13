"""
Runtime of sorting monotonically increasing order of finish time: O(log n) <- Using QuickSort or HeapSort
Runtime of the Greedy-Activity-Selector: O(n)
Overall Runtime: n + n log n = O(n log n)
"""
def Greedy_Activity_Selector(s, f):
    n = len(s)
    # Has the first element in the array
    A = [1]
    k = 1
    for m in range(2, n):
        if s[m] >= f[k]:
            A.append(m)
            k = m
    return A

