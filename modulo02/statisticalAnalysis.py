import statistics

### Média aritmética

def arithmeticMean(amountReceived):
    if not amountReceived:
        return 0,0
    
    average = statistics.mean(amountReceived)
    return average