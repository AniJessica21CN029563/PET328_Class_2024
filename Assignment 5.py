# Request for reservoir dimensions and discretization parameters
Lx = float(input('What is the Length of the reservoir in the x axis: '))
Ly = float(input('What is the Length of the reservoir in the y axis: '))
Lz = float(input('What is the Length of the reservoir in the z axis: '))
nx = int(input('What is the number of gridblocks in the x axis: '))
ny = int(input('What is the number of gridblocks in the y axis: '))
nz = int(input('What is the number of gridblocks in the z axis: '))

# Request for the cut-off value
cut_off = float(input('What is the value of the cut-off: '))

# Initialize counters
n_active = 0
n_inactive = 0

# Loop through all blocks (nested loop)
for k in range(1, nz + 1):
    # Initialize layer counter
    active_layer = 0
    # Two nested loops go here
    for j in range(1, ny + 1):
        for i in range(1, nx + 1):
            perm = float(input(f"What is the permeability value for block ({i}, {j}, {k}): "))
            if perm < cut_off:
                category = 'inactive'
                n_inactive += 1
            else:
                category = 'active'
                n_active += 1
                active_layer += 1
            
    # Print layer count
    print(f"Layer {k} active blocks: {active_layer}")

# Print overall counts
all_blocks = n_active + n_inactive
n_active_percent = (n_active / all_blocks) * 100
round_n_active_percent = round(n_active_percent, 2)

n_inactive_percent = (n_inactive / all_blocks) * 100
round_n_inactive_percent = round(n_inactive_percent, 2)

print(f'The percentage of the active blocks in the entire reservoir is {round_n_active_percent}%')
print(f'The percentage of the inactive blocks in the entire reservoir is {round_n_inactive_percent}%')
