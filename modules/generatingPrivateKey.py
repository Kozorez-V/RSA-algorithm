#find d satisfying the condition e*d = (k*phi) + 1

def calculateD(phi, e):
    k = 2
    while True:
        if (k * phi + 1) % e == 0:
            return (k * phi + 1) // e
        else:
            k += 1