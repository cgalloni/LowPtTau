import FWCore.ParameterSet.Config as cms
import copy

'''

Sequences for reconstructing LowPt taus using the HPS algorithm

'''

import CommonTools.ParticleFlow.pfNoPileUp_cff as LowPtTaus
pfPileUpForLowPtTaus = LowPtTaus.pfPileUp.clone(
    PFCandidates = cms.InputTag('particleFlow'),
    checkClosestZVertex = cms.bool(False)
)
pfNoPileUpForLowPtTaus = LowPtTaus.pfNoPileUp.clone(
    topCollection = cms.InputTag('pfPileUpForLowPtTaus'),
    bottomCollection = cms.InputTag('particleFlow')
)


import RecoJets.JetProducers.ak4PFJets_cfi as LowPtTaus2


# reclustering ak8 chs
betapar = cms.double(0.0)
fatjet_ptmin = 1.0

#from RecoJets.JetProducers.ak5PFJets_cfi import ak5PFJets

from RecoJets.JetProducers.ak8PFJets_cfi import ak8PFJets

#ak8CHSJets_lowpt = ak8PFJetsCHS.clone( src = 'chs',jetPtMin = fatjet_ptmin )
ak8PFJets_lowpt = ak8PFJets.clone( rParam = 0.8, jetPtMin = fatjet_ptmin,    jetCollInstanceName = cms.string('ak8PFJets_lowpt') )


LowPtTauSeeds = cms.EDProducer("LowPtTauSeedsProducer",
    subjetSrc = cms.InputTag('ak8PFJets_lowpt', 'ak8PFJets_lowpt'),
    pfCandidateSrc = cms.InputTag('particleFlow'),
    verbosity = cms.int32(0)
)

LowPtHPSPFTausTask = cms.Task(
    pfPileUpForLowPtTaus,
    pfNoPileUpForLowPtTaus,
    ak8PFJets_lowpt,
    LowPtTauSeeds
)
