import time, webbrowser


total_breaks = 3
break_count = 0

print("You started work at "+time.ctime())
while(break_count < total_breaks):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=rSg4m1hpEFI")
    break_count += 1

print("End of session")
