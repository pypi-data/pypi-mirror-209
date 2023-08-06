#! /bin/bash
#$ -j y # Merge the error and output streams into a single file
#$ -o /unix/cedar/pwang/runArea/Regression_Test/myscan00/8TeV/0000/contur.log # Output file path
source /unix/cedar/software/cos7/defaults/setupEnv.sh;
export CONTUR_DATA_PATH=/home/pwang/contur_public
export CONTUR_USER_DIR=/home/pwang/contur_public/../contur_users
export RIVET_ANALYSIS_PATH=/home/pwang/contur_public/../contur_users:/home/pwang/contur_public/data/Rivet
export RIVET_DATA_PATH=/home/pwang/contur_public/../contur_users:/home/pwang/contur_public/data/Rivet:/home/pwang/contur_public/data/Theory
source $CONTUR_USER_DIR/analysis-list
cd /unix/cedar/pwang/runArea/Regression_Test/myscan00/8TeV/0000
Herwig read herwig.in -I /unix/cedar/pwang/runArea/Regression_Test/RunInfo -L /unix/cedar/pwang/runArea/Regression_Test/RunInfo;
Herwig run herwig.run --seed=101  --tag=runpoint_0000  --numevents=30000 ;
