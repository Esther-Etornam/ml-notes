# Function to calculate the dot product of 4 values

def dot4(a1, a2, a3, a4, b1, b2, b3, b4):
    return (a1 * b1) + (a2 * b2) + (a3 * b3) + (a4 * b4)


# Food ratings

ama = [2, -1, 0, 1]
kofi = [1, -2, 1, 2]
esi = [-2, 1, 1, -1]


# Compare Ama and Kofi
ama_kofi = dot4(
    ama[0], ama[1], ama[2], ama[3],
    kofi[0], kofi[1], kofi[2], kofi[3]
)

# Compare Ama and Esi
ama_esi = dot4(
    ama[0], ama[1], ama[2], ama[3],
    esi[0], esi[1], esi[2], esi[3]
)

# Compare Kofi and Esi
kofi_esi = dot4(
    kofi[0], kofi[1], kofi[2], kofi[3],
    esi[0], esi[1], esi[2], esi[3]
)


# Print results

print(ama_kofi)
print(ama_esi)
print(kofi_esi)