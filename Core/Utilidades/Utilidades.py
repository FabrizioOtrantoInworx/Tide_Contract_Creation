import random

class Utilidades():

    def CreateUMR(text = ""):
        umr = text + "Umr" + str(random.randint(100,99999999999))
        return umr

    def CreateSourceSystemReference(text = ""):
        sourceSystemReference = text + "sourceSystemReference" + str(random.randint(100,99999999999))
        return sourceSystemReference