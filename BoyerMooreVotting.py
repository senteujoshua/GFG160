def findMajority(arr):
    n = len(arr)

    ele1, ele2 = -1, -1
    cnt1, cnt2 = 0, 0

    for ele in arr:
        if ele == ele1:
            cnt1 += 1
        if ele ==ele2:
            cnt2 += 1
        elif cnt1 == 0:
            ele1, cnt1 = ele, 1
        elif cnt2 == 0:
            ele2, cnt2 = ele, 1
        else:
            cnt1, cnt2 = cnt1 - 1, cnt2 - 1

    res = []
    cnt1, cnt2 = 0, 0
        # Count the occurrences of candidates
    for ele in arr:
        if ele1 == ele:
            cnt1 += 1
        if ele2 == ele:
            cnt2 += 1

    # Add to result if they are majority elements
    if cnt1 > n / 3:
        res.append(ele1)
    if cnt2 > n / 3 and ele1 != ele2:
        res.append(ele2)

    if len(res) == 2 and res[0] > res[1]:
        res[0], res[1] = res[1], res[0]

    return res

    


if __name__ == "__main__":
    arr = [2,2,3,1,3,2,1,1]
    res = findMajority(arr)
    for ele in res:
        print(ele,end=" ")