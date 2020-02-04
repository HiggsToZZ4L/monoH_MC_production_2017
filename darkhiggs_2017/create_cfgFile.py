import os
import sys

def create_cfgFile(datasetName, inputPath, step='step0', nEvents='100000', site='IFCA'):

    if "step0" in step: 
        text = "from WMCore.Configuration import Configuration\n"
        text += "config = Configuration()\n"
    else:
        text = "from CRABClient.UserUtilities import config\n"
        text += "config = config()\n"

    text += "config.section_('General')\n"
    text += "config.General.transferLogs = True\n"
    text += "config.General.requestName = 'EXO_" + datasetName + "_" + step + "'\n"
    text += "config.General.workArea = 'crab_projects'\n"


    text += "config.section_('JobType')\n"
    text += "config.JobType.pluginName  = 'PrivateMC'\n"
    text += "config.JobType.maxMemoryMB = 5000\n"


    if "step0" in step: #EventBased from lhe file
        text += "config.JobType.psetName = '" + step + "_" + datasetName + ".py'\n"
        with open(step + ".py") as f1:
            with open(step + "_" + datasetName + ".py", "w") as f2:
                for line in f1:
                    if 'ReplaceMe' in line:
                        f2.write(line.replace('ReplaceMe.lhe', inputPath))
                    else:
                        f2.write(line)
        
        text += "config.JobType.inputFiles = ['" + inputPath  + "']\n"
        text += "config.JobType.disableAutomaticOutputCollection = False\n"
        text += "config.section_('Data')\n"
        text += "config.Data.splitting = 'EventBased'\n"
        text += "config.Data.unitsPerJob = 400\n"
        text += "config.Data.totalUnits = " + nEvents + "\n"
        text += "config.Data.outputPrimaryDataset = 'CRAB_PrivateMC'\n"

    else: #step1, 2, 3, 4... FileBased from das path
        text += "config.JobType.allowUndistributedCMSSW = True\n"
        text += "config.JobType.psetName = '" + step + ".py'\n"
        text += "config.section_('Data')\n"
        text += "config.Data.splitting = 'FileBased'\n"
        text += "config.Data.unitsPerJob = 1\n"
        text += "config.Data.inputDataset = '" + inputPath  + "'\n"
        text += "config.Data.inputDBS = 'phys03'\n"

    text += "config.Data.outputDatasetTag = 'EXO_" + datasetName + "_" + step + "'\n"
    text += "config.Data.publication = True\n"

    if "IFCA" in site:
        text += "config.Data.outLFNDirBase = '/store/user/fernanpe/'\n"
#        text += "config.Data.outLFNDirBase = '/store/group/cms/fernanpe/'\n"
    else:
        text += "config.Data.outLFNDirBase = '/store/group/phys_muon/fernanpe/MonoH/'\n"        

    text += "config.section_('Site')\n"

    if "IFCA" in site:
        text += "config.Site.storageSite = 'T2_ES_IFCA'\n"
    else: #CERN
        text += "config.Site.storageSite = 'T2_CH_CERN'\n"

    f = open('crab_cfg_' + datasetName + "_" + step + ".py", 'w')
    f.write(text)
    f.close()
    print 'Created cfg file: crab_cfg_' + datasetName + "_" + step + '.py'



if __name__ == '__main__':
    create_cfgFile(*sys.argv[1:])
