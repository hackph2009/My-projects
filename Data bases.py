import sqlite3
db = sqlite3.connect("app.db")
cr = db.cursor()
def commit_close():
    """Commit Changes And Close The Connection"""
    db.commit()
    db.close() 
    print("Connection is closed")

uid = 1

input_message = """
What Do You Want To Do?
"s" => Show All Skills
"a" => Add New Skill
"d" => Delete A Skill
"u" => Update Skill Progress
"q" => Quit The App
---select An Option---
"""
user_input = input(input_message).strip().lower()

commands_list = ["s", "a", "d", "u", "q"]

def show_skill():
    
    cr.execute(f"select * from skills where user_id = {uid}")
    results = cr.fetchall()
    print(f"You Have {len(results)} Skills.")
    if len(results) > 0 :
        print("\nShowing Skills With Progress....\n")

        for row in results:

            print(f"skill => {row[0]},", end=" ")
            print(f"Progress => {row[1]}%")

    commit_close()

def add_skill():
    
    sk = input("Write Skill name: ").strip().capitalize()
    cr.execute(f"select name from skills where name = '{sk}' and user_id = {uid}")
    result = cr.fetchone()
    if result == None:
        prog = input("Write Skill Progress: ").strip()
        cr.execute(f"insert into values('{sk}', {prog}, {uid})")
        print("Skill Added Successfully")
    else:
        print("This skill is already exists")
        option = input("Do you Need to edit? (Y, N): ").strip().upper()
        if option == "Y":
          prog = input("Write The New Skill Progress: ").strip()
          cr.execute(f"update skills set progress={prog} where name='{sk}' and user_id = {uid}")
          print("Edit Is Done!")
        else:
            print("Action Canceled")
    commit_close()
    
def delete_skill():
    
    sk = input("Write Skill name: ").strip().capitalize()
    cr.execute(f"delete from skills where name = '{sk}' and user_id = '{uid}'")
    commit_close()
    print("Skill Deleted Successfully!")
def update_skill():

    sk = input("Write Skill name: ").strip().capitalize()
    prog = input("Write The New Skill Progress: ").strip()
    cr.execute(f"update skills set progress = {prog} where name = '{sk}' and user_id = {uid}")
    print("Skill Updated successfully")
    
    commit_close()

if user_input in commands_list:
    
    print(f"\n The Command {user_input} Was Found\n ")

    if user_input == "s":
        
        show_skill()
        

    elif user_input == "a":
        
        add_skill()
        

    elif user_input == "d":
        
        delete_skill()
        

    elif user_input == "u":
        
        update_skill()
        

    else:

        print("App Is Closed")
        commit_close()
        exit()


else:

    print(f"Sorry The Command \"{user_input}\" Not Found")

