def solution(phone_book):
    answer = True

    prefix = set()
    tmp = phone_book
    tmp.sort(key = len, reverse = True)

    for p in tmp:
        if p in prefix:
            answer = False
            break
        else:
            cases = get_all_cases(p)
            for case in cases:
                prefix.add(case)        

    return answer

def get_all_cases(phone):
    result = []
    for x in range(0, len(phone)):
        result.append(phone[:x+1])

    return result
