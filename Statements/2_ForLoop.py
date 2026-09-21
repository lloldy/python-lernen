# for-Schleife = wiederholt Code für jedes Element einer Sequenz

test = "Pyhton"

for letter in test:      
    print("Hallo")        

test2 = (1,2,3,4,5, "Test")   
for element in test2:        
    print("?")                


for x in range(10):       
    if x%2 == 0:            
        print(x)             #
    else:
        print("Die Zahl ist ungerade")   


even_numbers= []

for x in range(10):
    if x%2 == 0:
        even_numbers.append(x)

print(even_numbers)
