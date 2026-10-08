team1=["Alice", "Bob", "Charlie"]
team2=["David", "Eve", "Frank"] 
team1.append("Grace")
for x in team1:
    print(x,end=" ")
    
team1.extend(team2)
print()
for x in team2:
    print(x,end=" ")    