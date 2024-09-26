#!/bin/bash

# SLURM submission script for multiple serial jobs on Niagara
#SBATCH --partition=debug
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=40  # 40 task for serial execution (one per core)
#SBATCH --cpus-per-task=1     # Each task uses 1 CPU
#SBATCH --time=1:00:00       # Set a time limit for debugging
#SBATCH --job-name=scf
#SBATCH --output=job_output_%j.txt
#SBATCH --error=job_error_%j.txt

module load CCEnv
module load StdEnv/2023 
module load gcc/12.3 xtb/6.6.1

# Set OMP_NUM_THREADS to 1 to limit xtb to 1 thread per process
export OMP_NUM_THREADS=1

#python run.py split_files/split_01.xyz 

# Parallel execution: each core handles one XYZ file
#parallel --jobs $SLURM_NTASKS python run.py {} ::: split_files/split_*.xyz

# Run each job in its own subdirectory
(
    cd subdir_01 && python ../run.py split_01.xyz && echo "Job 1 finished" &
    cd subdir_02 && python ../run.py split_02.xyz && echo "Job 2 finished" &
    cd subdir_03 && python ../run.py split_03.xyz && echo "Job 3 finished" &
    cd subdir_04 && python ../run.py split_04.xyz && echo "Job 4 finished" &
    cd subdir_05 && python ../run.py split_05.xyz && echo "Job 5 finished" &
    cd subdir_06 && python ../run.py split_06.xyz && echo "Job 6 finished" &
    cd subdir_07 && python ../run.py split_07.xyz && echo "Job 7 finished" &
    cd subdir_08 && python ../run.py split_08.xyz && echo "Job 8 finished" &
    cd subdir_09 && python ../run.py split_09.xyz && echo "Job 9 finished" &
    cd subdir_10 && python ../run.py split_10.xyz && echo "Job 10 finished" &
    cd subdir_11 && python ../run.py split_11.xyz && echo "Job 11 finished" &
    cd subdir_12 && python ../run.py split_12.xyz && echo "Job 12 finished" &
    cd subdir_13 && python ../run.py split_13.xyz && echo "Job 13 finished" &
    cd subdir_14 && python ../run.py split_14.xyz && echo "Job 14 finished" &
    cd subdir_15 && python ../run.py split_15.xyz && echo "Job 15 finished" &
    cd subdir_16 && python ../run.py split_16.xyz && echo "Job 16 finished" &
    cd subdir_17 && python ../run.py split_17.xyz && echo "Job 17 finished" &
    cd subdir_18 && python ../run.py split_18.xyz && echo "Job 18 finished" &
    cd subdir_19 && python ../run.py split_19.xyz && echo "Job 19 finished" &
    cd subdir_20 && python ../run.py split_20.xyz && echo "Job 20 finished" &
    cd subdir_21 && python ../run.py split_21.xyz && echo "Job 21 finished" &
    cd subdir_22 && python ../run.py split_22.xyz && echo "Job 22 finished" &
    cd subdir_23 && python ../run.py split_23.xyz && echo "Job 23 finished" &
    cd subdir_24 && python ../run.py split_24.xyz && echo "Job 24 finished" &
    cd subdir_25 && python ../run.py split_25.xyz && echo "Job 25 finished" &
    cd subdir_26 && python ../run.py split_26.xyz && echo "Job 26 finished" &
    cd subdir_27 && python ../run.py split_27.xyz && echo "Job 27 finished" &
    cd subdir_28 && python ../run.py split_28.xyz && echo "Job 28 finished" &
    cd subdir_29 && python ../run.py split_29.xyz && echo "Job 29 finished" &
    cd subdir_30 && python ../run.py split_30.xyz && echo "Job 30 finished" &
    cd subdir_31 && python ../run.py split_31.xyz && echo "Job 31 finished" &
    cd subdir_32 && python ../run.py split_32.xyz && echo "Job 32 finished" &
    cd subdir_33 && python ../run.py split_33.xyz && echo "Job 33 finished" &
    cd subdir_34 && python ../run.py split_34.xyz && echo "Job 34 finished" &
    cd subdir_35 && python ../run.py split_35.xyz && echo "Job 35 finished" &
    cd subdir_36 && python ../run.py split_36.xyz && echo "Job 36 finished" &
    cd subdir_37 && python ../run.py split_37.xyz && echo "Job 37 finished" &
    cd subdir_38 && python ../run.py split_38.xyz && echo "Job 38 finished" &
    cd subdir_39 && python ../run.py split_39.xyz && echo "Job 39 finished" &
    cd subdir_40 && python ../run.py split_40.xyz && echo "Job 40 finished"
)
wait
