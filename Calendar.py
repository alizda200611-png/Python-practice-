all_months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
total_m = int(input("Enter your mounths"))
total_d = int(input("Enter your days"))
for m  in range(1, total_m + 1):
   print(all_months [m - 1])
   line = ""
   for d in range(1, total_d + 1):
      line += str(d) + " "
   print(line)
