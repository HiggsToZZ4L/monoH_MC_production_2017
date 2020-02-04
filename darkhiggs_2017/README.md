DOCUMENTATION
=========================

Copy the .gz files and untar them
--------------
```
./untar.sh
```

Create the crab config files
--------------

```
python mkStep0.py 
```

Set CRAB environment
--------------

```
cmsenv (CMSSW_9_4_9)

source /cvmfs/cms.cern.ch/crab3/crab.sh

voms-proxy-init --voms cms --valid 168:00
```

Submit the jobs
--------------

```
./runStep0.sh
```
