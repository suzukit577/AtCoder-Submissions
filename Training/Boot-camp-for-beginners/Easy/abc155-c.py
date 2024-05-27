from collections import defaultdict


def get_keys_from_value(d: dict, val) -> list:
    """get keys from vlue: O(n)

    Args:
        d (dict): dict
        val: value of d

    Returns:
        list: keys corresponding to given value
    """
    return [k for k, v in d.items() if v == val]


N = int(input())
dd = defaultdict(int)
for _ in range(N):
    S = input()
    dd[S] += 1
max_cnt = max(dd.values())
for word in sorted(get_keys_from_value(dd, max_cnt)):
    print(word)
