import json
import sys

# Load target
target_file = 'M3_L2_Data_Preprocessing_Task(train).ipynb'
source_file = 'eda-on-mpg-data.ipynb'

with open(target_file, 'r', encoding='utf-8') as f:
    nb_train = json.load(f)

with open(source_file, 'r', encoding='utf-8') as f:
    nb_eda = json.load(f)

# Find start of "Analysis of Distribution"
start_idx = -1
for i, cell in enumerate(nb_eda['cells']):
    source_str = "".join(cell.get('source', []))
    if 'Analysis of Distribution' in source_str:
        start_idx = i
        break

if start_idx == -1:
    print("Could not find 'Analysis of Distribution' in EDA notebook.")
    sys.exit(1)

print(f"Found 'Analysis of Distribution' at cell {start_idx}. Extracting {len(nb_eda['cells']) - start_idx} cells.")
cells_to_append = nb_eda['cells'][start_idx:]

nb_train['cells'].extend(cells_to_append)

with open(target_file, 'w', encoding='utf-8') as f:
    json.dump(nb_train, f, indent=1)

print("Successfully appended cells to target notebook.")
