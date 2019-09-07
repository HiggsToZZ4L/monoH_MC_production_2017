DOCUMENTATION
=========================

Create the gridpacks
--------------
See the documentation here: https://github.com/cms-sw/genproductions/tree/master/bin/MadGraph5_aMCatNLO/cards/production/2017/13TeV/monoHiggs/Zp2HDM/

```
git clone git@github.com:cms-sw/genproductions.git
cd genproductions/bin/MadGraph5_aMCatNLO/
```

For Zprime_A0h_A0chichi:

```
cp cards/production/2017/13TeV/monoHiggs/Zp2HDM/Zprime_A0h_A0chichi/genGridpack_2HDM.py .
cp -r cards/production/2017/13TeV/monoHiggs/Zp2HDM/Zprime_A0h_A0chichi/cards/* cards/. 
python genGridpack_2HDM.py
```

input cards are now generated in the cards directory

TEST your gridpacks (not needed, but recommended)

```
cd CMSSW_7_1_30/src
cmsenv
tar xvf xxx.tar.xz
./runcmsgrid_LO.sh 5000 $RANDOM 1
```


Untar the gridpack and produce the LHE files (interfaced with Pythia) + RAW-SIM
--------------

```
cd CMSSW_9_4_9/src/MonoH_MC_2017/

cd CMSSW_7_1_30/src
cmsenv

cd -

cp /cvmfs/cms.cern.ch/phys_generator/gridpacks/2017/13TeV/madgraph/V5_2.4.2/monoHiggs/Zp2HDM/Zprime_A0h_A0chichi/v1/Zprime_A0h_A0chichi_MZp800_MA0300_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz .

tar xvf xxx.tar.xz

./runcmsgrid.sh 10000 $RANDOM 1 
```

Set CRAB environment
--------------

```
cmsenv (CMSSW_9_4_9)

source /cvmfs/cms.cern.ch/crab3/crab.sh

voms-proxy-init --voms cms --valid 168:00
```

CRAB info
--------------

```
crab submit -c configFile.py
crab status --dir/-d <CRAB-project-directory>
crab resubmit --dir/-d <CRAB-project-directory>
crab kill -d <CRAB-project-directory
```
Online monitoring: http://dashb-cms-job.cern.ch/dashboard/templates/task-analysis/#user=Pedro+Fernandez+Manteca&refresh=0&table=Mains&p=1&records=25&activemenu=2&pattern=&task=&from=&till=&timerange=lastWeek
New link: https://monit-grafana.cern.ch/d/cmsTMDetail/cms-task-monitoring-task-view?orgId=11&var-user=fernanpe&var-task=190716_125714%3Afernanpe_crab_EXO-RunIIFall17wmLHEGS-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_MH3_200_MH4_150_neg_step0

Documentation here: https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookCRAB3Tutorial


Submit the step0: Produce the GEN-SIM
--------------

```
crab submit -c crab_cfg_step0.py -> give it as input the lhe file
```


Submit the step1: Produce the premix + GEN-SIM
--------------

```
crab submit -c crab_cfg_step1.py -> search in DAS prod/phys03 your publicated output:
```

https://cmsweb.cern.ch/das/request?view=list&limit=50&instance=prod%2Fphys03&input=%2FCRAB_PrivateMC%2Ffernanpe*%2F*

Submit the step2: Produce AOD
--------------

```
crab submit -c crab_cfg_step2.py -> give it as input the das output of the previous step
```

Submit the step3: Produce miniAOD
--------------

```
crab submit -c crab_cfg_step3.py -> give it as input the das output of the previous step
```

Submit the step4: Produce nanoAOD
--------------

```
crab submit -c crab_cfg_step4.py -> give it as input the das output of the previous step
```

Added: nanoAOD das publication

- How to create the step4.py (named myNanoProcMc_NANO.py in this example)

```
cmsDriver.py myNanoProcMc -s NANO --eventcontent NANOAODSIM --datatier NANOAODSIM --no_exec --conditions 94X_mc2017_realistic_v14 --era Run2_2017,run2_nanoAOD_94XMiniAODv1 --customise_commands="process.add_(cms.Service('InitRootHandlers', EnableIMT = cms.untracked.bool(False)))"
```
- Put myNanoProcMc_NANO.py in crab_cfg_step4.py: config.JobType.psetName = 'myNanoProcMc_NANO.py'

- Most important thing: add fakeNameForCrab =cms.untracked.bool(True), as configuraion of the outputmodule


