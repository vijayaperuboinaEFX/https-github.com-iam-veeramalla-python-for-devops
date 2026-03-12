
print("********List operation********")
list_ec2 = ["aws","GCP","oracle","alibaba","azure","hello machha"]



list_ec2.insert(0,"vijay")
print (list_ec2)

awscloud =len(list_ec2)
print(awscloud)

#for awscloud in list_ec2:
for i in range(len(list_ec2)):
    print(f"Item at index {i}: {list_ec2[i]}")

print("********end List operation********")    
    

print("********set operation********")
my_set = {1, 2, 3, 4, 5,6}
print(my_set) 