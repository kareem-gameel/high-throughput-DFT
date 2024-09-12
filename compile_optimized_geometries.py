import os

def compile_xyz_files(base_dir, output_file):
    """
    Go over each subdirectory in the base directory and compile all optimized XYZ files into one file.
    """
    with open(output_file, 'w') as output_xyz:
        # Iterate over each subdirectory
        for subdir in sorted(os.listdir(base_dir)):
            subdir_path = os.path.join(base_dir, subdir)
            if os.path.isdir(subdir_path):
                xyz_file = os.path.join(subdir_path, 'optimized.xyz')
                if os.path.exists(xyz_file):
                    with open(xyz_file, 'r') as infile:
                        output_xyz.write(infile.read())
                    print(f"Compiled {xyz_file}")

# Example usage
compile_xyz_files('/scratch/o/ovoznyy/gameelka/xtb_remainder/split_files', 'compiled_optimized.xyz')
