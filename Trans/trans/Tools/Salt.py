import random

class Salt:
    @staticmethod
    def GenerateSalt():
        # Initialize
        chars = "0123456789ABCDEF"
        randomNumberGen = random.SystemRandom()
        valArr = []
        for i in range(16):
            valArr.append(randomNumberGen.choice(chars))
        return ''.join(valArr)