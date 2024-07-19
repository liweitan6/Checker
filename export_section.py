import os
import shutil
from database import get_history
from file import read_file_content

def export_code():
    export_directory = os.getcwd()
    # Create the main export directory
    
    # Create a summary file
    with open(os.path.join(export_directory, 'summary.txt'), 'w') as summary_file:
        summary_file.write("ID\tFile 1\tFile 2\tSimilarity\tTimestamp\tManual Check\n")
        
        for record in history:
            id, file1, file2, similarity, timestamp, manual_check = record
            
            # Write to summary file
            summary_file.write(f"{id}\t{file1}\t{file2}\t{similarity}\t{timestamp}\t{manual_check}\n")
            
            # Create directories for each comparison
            comparison_dir = os.path.join(export_directory, f"comparison_{id}")
            os.makedirs(comparison_dir, exist_ok=True)
            
            # Copy and rename the original files
            file1_name = os.path.basename(file1)
            file2_name = os.path.basename(file2)
            shutil.copy2(file1, os.path.join(comparison_dir, f"1_{file1_name}"))
            shutil.copy2(file2, os.path.join(comparison_dir, f"2_{file2_name}"))
            
            # Create text files with the code content
            with open(os.path.join(comparison_dir, f"1_{file1_name}.txt"), 'w') as f:
                f.write(read_file_content(file1))
            with open(os.path.join(comparison_dir, f"2_{file2_name}.txt"), 'w') as f:
                f.write(read_file_content(file2))
    
    return export_directory