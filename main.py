import matplotlib.pyplot as plt

num = input("What number?: ")
lst = []

def mainLoop(sum):
  outputNum = int(sum)
  lst.append(outputNum)
  if outputNum % 2 == 0:
    outputNum /= 2
  else:
    outputNum *= 3
    outputNum += 1

  if outputNum == 1:
    lst.append(1)
    return
  else:
    mainLoop(outputNum)

mainLoop(num)

print(lst)

plt.plot(lst, 'r--')
plt.xlabel("Steps")
plt.ylabel("Step value")
plt.show()