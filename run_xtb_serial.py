import tempfile
import os
import subprocess
import sys  # To get the input XYZ file from the command line
from tqdm import tqdm

# Ensure the split file is provided as an argument
if len(sys.argv) != 2:
    print("Usage: python run.py <split_file.xyz>")
    sys.exit(1)

# Get the split XYZ file from the command line argument
split_file = sys.argv[1]

# Define the output file paths in the current directory
optimized_xyz_path = 'optimized.xyz'
optimized_energies_path = 'optimized_energies.csv'

# Create or overwrite the optimized_energies.csv file in the current directory
if not os.path.exists(optimized_energies_path):
    with open(optimized_energies_path, 'w') as energy_file:
        # Write the header for the CSV file
        energy_file.write("mol_id,energy\n")

def extract_energy_from_xtbopt(file_path):
    """
    Extract the total energy from the second line of the xtbopt.xyz file.
    """
    with open(file_path, 'r') as file:
        lines = file.readlines()
        energy_info = lines[1].strip().split()
        try:
            if "energy:" in energy_info:
                energy_index = energy_info.index("energy:") + 1
                energy = energy_info[energy_index]
            else:
                energy = "Not Found"
        except IndexError:
            energy = "Not Found"
        return energy

def mol_id_already_processed(mol_id, csv_path, xyz_path):
    """
    Check if the mol_id is already present in either the optimized_energies.csv
    or the optimized.xyz file.
    """
    if os.path.exists(csv_path):
        with open(csv_path, 'r') as file:
            lines = file.readlines()
            for line in lines[1:]:
                if line.startswith(mol_id):
                    return True

    if os.path.exists(xyz_path):
        with open(xyz_path, 'r') as file:
            lines = file.readlines()
            for i in range(1, len(lines), 2):
                if mol_id in lines[i]:
                    return True

    return False

# Read the molecules from the split XYZ file passed as an argument
molecules = []
with open(split_file, 'r') as file:
    while True:
        num_atoms_line = file.readline().strip()
        if not num_atoms_line:
            break
        mol_id_line = file.readline().strip()
        coordinates = [file.readline().strip() for _ in range(int(num_atoms_line))]
        molecules.append((num_atoms_line, mol_id_line, coordinates))

# Loop over the molecules using tqdm for progress tracking
for num_atoms, mol_id, coordinates in tqdm(molecules, desc="Processing molecules"):
    temp_dir = tempfile.mkdtemp()

    if mol_id_already_processed(mol_id, optimized_energies_path, optimized_xyz_path):
        print(f"Skipping {mol_id} as it is already processed.")
        continue

    input_file_path = os.path.join(temp_dir, 'molecule.xyz')
    with open(input_file_path, 'w') as temp_file:
        temp_file.write(f"{num_atoms}\n")
        temp_file.write(f"{mol_id}\n")
        for line in coordinates:
            temp_file.write(line + '\n')

    subprocess.run(['xtb', input_file_path, '--gfn2', '--opt', 'vtight'], cwd=temp_dir)

    optimized_file_path = os.path.join(temp_dir, 'xtbopt.xyz')
    if os.path.exists(optimized_file_path):
        with open(optimized_file_path, 'r') as opt_file:
            optimized_molecule = opt_file.readlines()

        final_energy = extract_energy_from_xtbopt(optimized_file_path)

        with open(optimized_xyz_path, 'a') as output_xyz_file:
            output_xyz_file.write(optimized_molecule[0])
            output_xyz_file.write(f"{mol_id}\n")
            output_xyz_file.writelines(optimized_molecule[2:])

        with open(optimized_energies_path, 'a') as energy_file:
            energy_file.write(f"{mol_id},{final_energy}\n")

print(f"Optimization process completed. Results saved in {optimized_xyz_path} and {optimized_energies_path}")
