#!/bin/bash 
#$ -V
#$ -N FCC_Silicon
#$ -cwd
#$ -o $JOB_NAME.o$JOB_ID
#$ -e my_stderr
#$ -pe mpi 16
#$ -l h_vmem=4G
#$ -q  parallel.q
#$ -M noah.perreau@univ-fcomte.fr
#$ -m bea

module load vasp/5.4
mpirun -np $NSLOTS vasp
