import random

def greedy_cash_change(total:int, notes:list) -> tuple:
    notes.sort(reverse=True)
    result = []
    
    for note in notes:
        while total >= note:
            total -= note
            result.append(note)
        
    return result

if __name__ == "__main__":
    total = random.randint(1, 100)
    print(total)
    notes = [100, 50, 20, 10, 5, 1]
    print(greedy_cash_change(total, notes))