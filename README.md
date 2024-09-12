
# High-throughput xTB Geometry Optimization

This repository contains a series of scripts designed to automate high-throughput geometry optimizations of molecular structures using the `xTB` software. The workflow involves splitting large XYZ files into smaller chunks in separate directories, running geometry optimizations in parallel across multiple cores, and aggregating the results.

## Features

- **Splitting XYZ files**: Large XYZ files are split into multiple smaller files for parallel processing.
- **Batch processing with SLURM**: SLURM job scripts are provided to manage parallel geometry optimization jobs on a high-performance computing cluster.
- **Energy extraction**: xTB geometry optimizations are run with `GFN2-xTB`, and the total energy of each molecule is extracted and saved in CSV format.
- **Duplicate handling**: Scripts ensure that previously optimized molecules are skipped to avoid redundant calculations.
- **Progress tracking**: The progress of the optimization is tracked and printed in real-time.

## Requirements

- Python 3.x
- `xTB` (6.6.1 or newer)
- `tqdm` (for progress tracking)
- `pandas` (optional, for data handling)
- HPC environment with `SLURM` for batch job submissions

## Workflow

1. **Splitting the XYZ file**:
   Use `split.py` to split the large XYZ file into smaller files, each in separate directory to ensure no conflicts during parallel computations within the same node. Each file will contain an approximately equal number of molecules.

   ```bash
   python split.py
   ```

2. **Prepare SLURM job**:
   The `job.sh` script is designed to submit jobs to a SLURM-based HPC environment. Each job will run the `run.py` script to process a specific split file. Ensure that all necessary modules are loaded, and the virtual environment is activated.

   ```bash
   sbatch job.sh
   ```

3. **Running Geometry Optimization**:
   The `run.py` script processes each XYZ file, running the xTB optimization on each molecule and saving the optimized geometries and energies in separate files.

4. **Extracting Results**:
   After the job completes, the optimized geometries are saved in `optimized.xyz` and the corresponding energies in `optimized_energies.csv`. The energy values are extracted directly from the xTB output.

## File Structure

- **`split.py`**: Script to split the large XYZ file into smaller chunks for parallel processing.
- **`job.sh`**: SLURM job submission script to run multiple geometry optimizations in parallel.
- **`run.py`**: The main script that runs xTB geometry optimizations and saves the results.
- **`optimized.xyz`**: Output file that contains optimized geometries.
- **`optimized_energies.csv`**: Output CSV file that contains the `mol_id` and their corresponding optimized energy.

## Example Usage

1. Split the XYZ file into smaller files in separate directories:
   ```bash
   python split.py
   ```

2. Submit the SLURM job to run the optimization:
   ```bash
   sbatch job.sh
   ```

3. Check the output files (`optimized.xyz` and `optimized_energies.csv`) for results.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
