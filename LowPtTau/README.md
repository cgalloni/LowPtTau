# LowPtTau

Get CMSSW:
```
cmsrel  CMSSW_9_4_7
cd CMSSW_9_4_7/src
git cms-init
```

Get the additional packages to change the reconstruction:
```
git cms-addpkg PhysicsTools/PatAlgos
git cms-addpkg RecoTauTag/Configuration

git remote add camilla https://github.com/cgalloni/LowPtTau
git fetch camilla
git checkout -b Development_LowPtTau    camilla/LowPtTau
git clone https://github.com/cgalloni/LowPtTau

scram b -j 8
```



List of changed files:

```
RecoTauTag/Configuration/python/LowPtHPSPFTaus_cff.py
RecoTauTag/Configuration/python/LowPtHPSPFTaus_cfi.py
``

List of modified files:
```
PhysicsTools/PatAlgos/python/slimming/miniAOD_tools.py
PhysicsTools/PatAlgos/python/slimming/MicroEventContent_cff.py

```

Important settings in RecoTauTag/Configuration/python/LowPtHPSPFTaus_cf*.py


process.ak4PFJetsLegacyHPSPiZeros.minJetPt = cms.double(1.0),
process.selectedPatTausLowPt.cut = cms.string("pt > 1. && tauID(\'decayModeFindingNewDMs\')> 0.5")

