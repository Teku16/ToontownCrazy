from DistributedNPCToonBaseAI import *
from toontown.toon.ToonDNA import ToonDNA


class DistributedNPCYinAI(DistributedNPCToonBaseAI):
    def requestTransformation(self):
        avId = self.air.getAvatarIdFromSender()
        av = self.air.doId2do.get(avId)
        if av is None:
            return
        if not hasattr(av, 'dna'):
            return
        if (av.dna.getAnimal() == 'dog') and (av.dna.headColor != 0x1a):
            newDNA = ToonDNA()
            newDNA.makeFromNetString(av.getDNAString())
            newDNA.headColor = 0x1a
            newDNA.armColor = 0x1a
            newDNA.legColor = 0x1a
            taskMgr.doMethodLater(1.0, lambda task: av.b_setDNAString(newDNA.makeNetString()), 'transform-%d' % avId)
            self.sendUpdate('doTransformation', [avId])
