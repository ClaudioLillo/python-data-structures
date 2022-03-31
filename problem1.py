# Sorted list
cards = [108, 56, 44, 21, 19, 15, 14, 12, 11, 11, 11, 9, 9, 7, 4, 3]

target = 11

# Linear search, time complexity (O)N, space complexity (O) 
def findtarget(cards, target):
    index = len(cards)//2
    while index < len(cards) and index >= 0:
        num = cards[index]
        if num > target:
            index += 1
        elif num < target:
            index -= 1
        else:
            return index
    return "target not found in list"

result = findtarget(cards, target)
print("target card was found in position ", result)

# A most efficient solution could be apply the function recursively, using a list from rigth or left portion of list, depending on the result of comparison
# Both solutions are applicable for lists that includes duplicated numbers

# Binary search, time complexity (O)log2N, space complexity ?

def findRecursive(cards, target, index_memo=0):
    if len(cards) == 1 and cards[0] != target:
        return "not found"
    index = len(cards)//2
    num = cards[index]
    if num > target:
        return findRecursive(cards[index+1:], target, index_memo = index_memo + index + 1)
    elif num < target:
        return findRecursive(cards[:index], target, index_memo = index_memo)
    return index + index_memo

print("result: ", findRecursive(cards, target))

    
    
