def solution(phone_book):
    phone_book.sort(key = lambda x : len(x))
    
    for front in phone_book:
        for numbers in phone_book:
                
            if numbers != front and numbers[:len(front)] == front:
                return False
            
    return True