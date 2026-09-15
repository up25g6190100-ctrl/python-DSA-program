def remove_duplicates(arr):
    result = []
    seen = set()
    for x in arr:
        if x not in seen:
            result.append(x)
            seen.add(x)
            return result
        print(remove dupllicates([1,2,3,4,5,]))