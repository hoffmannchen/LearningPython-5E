import pickle
X, Y, Z = 43, 44, 45                       # Native Python objects
S = 'Spam'                                 # Must be strings to store in file
D = {'a': 1, 'b': 2}
L = [1, 2, 3]
F = open('datafile.txt', 'wb')              # Create output text file
pickle.dump(D, F)
F.close()
F = open('datafile.txt', 'rb')
DD = pickle.load(F)
print(DD)
