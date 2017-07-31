#!/bin/bash
#
#SBATCH -p serial_requeue
#SBATCH -J PCA
#SBATCH -n 1
#SBATCH -N 1
#SBATCH -t 10:00:00
#SBATCH --mem 600000
#SBATCH -o %j_%N.out
#SBATCH -e %j_%N.err
#SBATCH --mail-type=ALL
#SBATCH --mail-user=yid095@mail.harvard.edu

cd /n/home11/stat115u1754/MLM

source new-modules.sh
# load tophat
# module load tophat/2.0.13-fasrc02
# load STAR
module load python
module load python/2.7.11-fasrc01
source activate ody


python Mod2.py

module load R
export R_LIBS_USER=$HOME/apps/R:$R_LIBS_USER
Rscript Mod2.R