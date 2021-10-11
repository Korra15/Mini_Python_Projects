from collections import defaultdict

count = 0


def hashing(key):
    return key % size


class HashLinearProbing:
    def __init__(self, size):
        self.hash_table = defaultdict().fromkeys(range(size), -1)

    def insertIntoHashIndexWithoutReplacement(self, key, index):
        global count

        load_factor = ((count / size) * 100)

        if load_factor < 80:
            if self.hash_table[index] == -1:
                self.hash_table[index] = key
                count = count + 1
            else:
                self.findVacantIndex(key, index)
        else:
            print("Cannot enter the key since the hash table is almost full.")

    def findVacantIndex(self, key, index):
        global count

        for i in range(1, size):
            index = index + 1
            pos = index % size
            if self.hash_table[pos] == -1:
                self.hash_table[pos] = key
                count = count + 1
                break
        print("Value cannot to hashed")

    def display(self):
        print("Hash Table Keys: (index, value)")
        for itr in self.hash_table.items():
            print(itr, end="  ")
        print()


# ------------------------------------------------------ #


size = int(input("Enter the size of the table: "))
hash_object = HashLinearProbing(size)

for _ in range(size):
    key_value = int(input("Enter key value: "))
    index = hashing(key_value)
    hash_object.insertIntoHashIndexWithoutReplacement(key_value, index)
    hash_object.display()

print("\nThank you for using the Hash Linear Probing program.")
