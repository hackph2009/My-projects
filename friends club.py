print("""


███████╗██████╗░██╗███████╗███╗░░██╗██████╗░░██████╗██╗  ░██████╗░██████╗░░█████╗░██╗░░░██╗██████╗░
██╔════╝██╔══██╗██║██╔════╝████╗░██║██╔══██╗██╔════╝╚█║  ██╔════╝░██╔══██╗██╔══██╗██║░░░██║██╔══██╗
█████╗░░██████╔╝██║█████╗░░██╔██╗██║██║░░██║╚█████╗░░╚╝  ██║░░██╗░██████╔╝██║░░██║██║░░░██║██████╔╝
██╔══╝░░██╔══██╗██║██╔══╝░░██║╚████║██║░░██║░╚═══██╗░░░  ██║░░╚██╗██╔══██╗██║░░██║██║░░░██║██╔═══╝░
██║░░░░░██║░░██║██║███████╗██║░╚███║██████╔╝██████╔╝░░░  ╚██████╔╝██║░░██║╚█████╔╝╚██████╔╝██║░░░░░
╚═╝░░░░░╚═╝░░╚═╝╚═╝╚══════╝╚═╝░░╚══╝╚═════╝░╚═════╝░░░░  ░╚═════╝░╚═╝░░╚═╝░╚════╝░░╚═════╝░╚═╝░░░░░


   """)
print("First, You must prove you are a member of our Group")
name=input("Firstly, Enter your name: \n ").lower()
if name=="yousef" or name=="yousif" or name=="youssef":
  print(f"Welcome, montager and rapper, {name}")
  member_number=input("Enter The member number of Groub: \n ")
  if member_number=="3":
    print ("Good job")
    age=input("Finally, Enter your age: \n ")
    if age=="16" or age=="17":
      print(f"Good job {name} Welcome to our Group")
    else:
      print("Sorry, You can't enter becuse your age isn't in our group")
  else:
    print("Sorry, You can't enter you are not a member of this group")
elif name=="hacker" or name=="mohammed" or name=="mohamed":
    print("Welcome, Hacker The admin of this group")
    member_number=input("Enter The member number of Groub: \n ")
    if member_number=="3":
      print ("Good job")
      age=input("Finally, Enter your age: \n ")
      if age=="16" or age=="17":
        print(f"Good job {name} Welcome to our Group")
      else:
        print("Sorry, You can't enter becuse your age isn't in our group")
    else:
      print("Sorry, You can't enter you are not a member of this group")
elif name=="elsayd" or name=="elsaid" or name=="sayed" or name=="elsayed" or name=="elaithi" :
    print("Welcome, elsayed the best member in this group")
    member_number=input("Enter The member number of Groub: \n ")
    if member_number=="3":
      print ("Good job")
      age=input("Finally, Enter your age: \n ")
      if age=="16" or age=="17":
        print(f"Good job {name} Welcome to our Group")
      else:
        print("Sorry, You can't enter becuse your age isn't in our group")
    else:
      print("Sorry, You can't enter you are not a member of this group")
else:
    print(f"Sorry, The name [ {name} ] isn't a member of this group")