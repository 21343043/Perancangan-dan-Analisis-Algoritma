# Input
w = [23, 45, 67, 39] # bobot masing-masing objek
v = [67, 86, 139, 42] # nilai masing-masing objek
K = 100 # kapasitas maksimum knapsack

# Algoritma Greedy untuk Knapsack
def knapsack_greedy(w, v, K):
    n = len(w)
    x = [0]*n # inisialisasi setiap status pengambilan objek i dengan 0
    i = 0
    TotalBobot = 0
    Available = True
    while (i < n) and (Available):
        # cek objek ke-i
        i += 1
        if (TotalBobot + w[i-1] <= K):
            # masukkan objek Ci ke dalam knapsack
            x[i-1] = 1
            TotalBobot += w[i-1]
        else:
            Available = False
            x[i-1] = 0 # objek Ci tidak dimasukkan ke dalam knapsack
    return x

# Output
hasil = knapsack_greedy(w, v, K)
print("Status pengambilan masing-masing objek: ", hasil)