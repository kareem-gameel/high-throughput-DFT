import os

def split_xyz_file(input_file, output_dir, num_splits=40):
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Read all molecules from the input file
    with open(input_file, 'r') as file:
        molecules = []
        while True:
            num_atoms_line = file.readline().strip()
            if not num_atoms_line:
                break
            mol_id_line = file.readline().strip()
            coordinates = [file.readline().strip() for _ in range(int(num_atoms_line))]
            molecules.append((num_atoms_line, mol_id_line, coordinates))

    # Calculate the number of molecules per split
    num_molecules = len(molecules)
    molecules_per_split = num_molecules // num_splits
    remainder = num_molecules % num_splits

    # Split the molecules into separate files
    start = 0
    for i in range(num_splits):
        end = start + molecules_per_split + (1 if i < remainder else 0)  # Handle remainder
        output_file_path = os.path.join(output_dir, f'split_{i + 1:02d}.xyz')
        with open(output_file_path, 'w') as output_file:
            for num_atoms, mol_id, coords in molecules[start:end]:
                output_file.write(f"{num_atoms}\n")
                output_file.write(f"{mol_id}\n")
                for line in coords:
                    output_file.write(f"{line}\n")
        start = end

    print(f"Split {num_molecules} molecules into {num_splits} files.")

# Example usage
split_xyz_file('tmQM_CO_diss_remainder.xyz', 'split_files')
