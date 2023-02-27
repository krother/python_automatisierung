
# 1. Create a list with the numbers 1..7
a = [1,2,3,4,5,6,7]
b = [i for i in range(1, 8)]
c = list(range(1, 8))

# 2. Store the numbers in a text file (no pandas!)
#   a) convert the numbers to a string
#   b) open a file with f = open(filename, 'w')
#   c) write to the file with f.write(s)
#   d) close the file with f.close()
s1 = '\n'.join([str(number) for number in a])

f = open('file.txt', 'w')
f.write(s1)
for number in a:
    f.write(f"{number}\n")
f.close()

# 3. Read the numbers again
#   a) open the file for reading
#   b) loop over the file object
#   c) append everything to a list
f = open('file.txt', 'r')
s2 = f.read()  # contents of the entire file in one string
lines = s2.split()

# alternative 1
f = open('file.txt', 'r')
s3 = f.readlines()

# alternative 2
f = open('file.txt', 'r')
n2 = []
total = 0
for line in f:
    number = int(line)
    n2.append(number)
    total += number

# 4. Sum them up arithmetically
n1 = [int(x) for x in lines]
total = sum(n1)


# 5. Write the sum as an extra line to the same file
f = open('file.txt', 'a')  # append mode
f.write(f'\n----------------\n{total}\n')
f.close()

# 6. Read the contents into a single string
with open('file.txt', 'r') as f:  # ContextManager
    s = f.read()
# file gets closed automatically

# 7. Calculate the product of everything
prod = 1
for number in n1:
    prod *= number
prod
