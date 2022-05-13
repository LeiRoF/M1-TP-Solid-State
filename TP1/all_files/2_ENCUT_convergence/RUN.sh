#!/bin/bash 
#$ -V
#$ -N Silicon_cutoff_opt
#$ -cwd
#$ -o $JOB_NAME.o$JOB_ID
#$ -e my_stderr
#$ -pe mpi 16
#$ -l h_vmem=4G
#$ -q  parallel.q
#$ -M noah.perreau@univ-fcomte.fr
#$ -m bea

module load vasp/5.4
rm energy.txt
mkdir -p outputs

for cutoff in 100 110 120 130 140 150 160 170 180 190 200 220 240 260 280 300 350 400 450 500
do
	sed -e "s/MY_ENCUT/${cutoff}/g" INCAR_template > INCAR
	mpirun -np $NSLOTS vasp
	energy=$(tail -n 1 OSZICAR | cut -b27-42)
	printf "%5d  " $cutoff >> energy.txt
	echo $energy >> energy.txt

	mv OSZICAR outputs/OSZICAR_$cutoff
	mv OUTCAR outputs/OUTCAR_$cutoff
done


