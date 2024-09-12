import os
import pandas as pd

def compile_energies_csv(base_dir, output_csv):
    """
    Go over each subdirectory in the base directory and compile all optimized energies into one CSV file.
    """
    combined_data = []
    
    # Iterate over each subdirectory
    for subdir in sorted(os.listdir(base_dir)):
        subdir_path = os.path.join(base_dir, subdir)
        if os.path.isdir(subdir_path):
            energy_file = os.path.join(subdir_path, 'optimized_energies.csv')
            if os.path.exists(energy_file):
                df = pd.read_csv(energy_file)
                combined_data.append(df)
                print(f"Compiled {energy_file}")
    
    # Concatenate all dataframes into one and write to CSV
    combined_df = pd.concat(combined_data, ignore_index=True)
    combined_df.to_csv(output_csv, index=False)

# Example usage
compile_energies_csv('/scratch/o/ovoznyy/gameelka/xtb_remainder/split_files', 'compiled_optimized_energies.csv')
