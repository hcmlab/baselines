# The range for each head is inclusive at the start and exclusive at the end
# The third entry of the lists determines how the reward typ is weighted
HEADS = {
    0: [1, 5, 1],  # Normal pills
    1: [5, 19, 1],  # Power pills
    2: [19, 1000, 1],  # eating blue ghosts
    3: [-10, 0, 1],  # dying
}
