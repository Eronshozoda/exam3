
numbers = input().split()


uniter = 0


for i in range(len(numbers)):
  
      if i == len(numbers) - 1 or numbers[i] != numbers[i + 1]:
        uniter += 1

print(uniter)
