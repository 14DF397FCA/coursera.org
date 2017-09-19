# python3
# Maximum Pairwise Product
n = int(input())
if n <= 0:
    print(0)
else:
    a = [int(x) for x in input().split()]
    len_a = len(a)
    if len_a != n:
        print(-1)
    else:
        if len_a == 1:
            print(int(a[0]))
        elif len_a == 2:
            print(int(a[0] * a[1]))
        else:
            max_a = a[0]
            max_a_id = -1
            max_b = a[0]
            for i in range(len_a):
                if max_a < a[i]:
                    max_a = a[i]
                    max_a_id = i
            max_b_id = -1
            for i in range(len(a)):
                if max_b <= a[i] <= max_a and max_a_id != i:
                    max_b = a[i]
                    max_b_id = i
            print(int(max_a * max_b))
