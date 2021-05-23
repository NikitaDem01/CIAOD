mas = [9,8,7,6,5,1,2,3,4]

def taskCoins(mas):
    maxcoins = 0
    count = int(len(mas)/3)
    for i in range(count):
        alicemax = max(mas)
        mas.remove(alicemax)
        helpcoin = max(mas)
        maxcoins = maxcoins + max(mas)
        mas.remove(helpcoin)
        bobmin = min(mas)
        mas.remove(bobmin)
    return maxcoins
  
  print(taskCoins(mas))
