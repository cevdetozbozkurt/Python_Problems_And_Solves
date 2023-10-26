supported = ["Lights off", "Lock the door","Open the door", "Make coffee", "Shut down"]

while True:
    prompt = input()
    for i in supported:
        
        if prompt.lower() == i.lower() and prompt.lower() != "shut down":
            print("OK") 
            break
        elif prompt.lower() == "shut down":
            exit()
        elif i.lower == "shut down" and prompt.lower() != i.lower():
            print("Unknown")