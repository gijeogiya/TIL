def solution(participant, completion):
    
    for i in range(len(completion)):
        participant.remove(completion[i])
        
    answer = participant[0]
            
    return answer