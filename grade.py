def get_ordinal(n):
    """(1st, 2nd, 3rd, 4th...)"""
    if 11 <= (n % 100) <= 13: # special cases
        suffix = 'th'
    else:
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')
    return f"{n}{suffix}"

def grade():
    name = input("Please enter your name:").strip()
    attempt = 0  # initialization
    total = input("The number of the total words: ")
    results = [] # save the result
    while True:
        attempt += 1
        ordinal = get_ordinal(attempt)  # 1 -> 1st; 2 -> 2nd etc
        
        
        mistake = input("The number of wrong words: ")
        
        
        total_num = int(total)
        mistake_num = int(mistake)
        rate = (total_num - mistake_num) / total_num
        percentage_rate = f"{rate:.2%}"
        results.append((ordinal,percentage_rate))

        
        print(f"{ordinal} attempt accuracy rate: {percentage_rate}")
        
        # selection
        if rate >= 0.85:
            print("Pass!")
            break
        elif 0.80 <= rate < 0.85:
            print("Only need to dictate the wrong words")
        else:
            print("Dictate again")
    print("\n--- Summary ---")
    print(f"{name}'s dictation results:")
    for ordinal, rate in results:
        print(f"{ordinal} attempt: {rate}")

if __name__ == "__main__":
    grade()