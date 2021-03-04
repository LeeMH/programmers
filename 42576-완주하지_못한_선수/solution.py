def solution(participant, completion):
    completion_check = {}
    if len(participant) == 1:
        return participant[0]
    
    for c in completion:
        if c in completion_check:
            completion_check[c] = completion_check[c] + 1
        else:
            completion_check[c] = 1

    print(completion_check)
        
    for p in participant:        
        if not p in completion_check or completion_check[p] == 0:
            answer = p
            break
        else:
            completion_check[p] = completion_check[p] - 1

    return answer


parr = ['a', 'b', 'c']
carr = ['a', 'b']
print(solution(parr, carr))