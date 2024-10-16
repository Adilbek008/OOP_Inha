######################################################################################################
# Only write your code within the area mentioned below. 
# Return your student ID in the first function
######################################################################################################
def your_ID():
    return "Group-H"

##################################################################################################
################ -Write your code in the designated section for each problem- ####################
##################################################################################################
######## Problem 1: Breaking Bad #################################################################

##################################################################################################

######## Problem 2: Lost #########################################################################
    
##################################################################################################

######## Problem 3: Fullmetal Alchemist ##########################################################

##################################################################################################

######## Problem 4: Sherlock #####################################################################

##################################################################################################

######## Problem 5: Death Note ###################################################################

##################################################################################################

######## Problem 6: Code Geass ###################################################################

##################################################################################################

######## Problem 7: Assassin's Creed #############################################################

##################################################################################################

######## Problem 8: DOTA #########################################################################

##################################################################################################

######## Problem 9: Baldur's Gate 3 ##############################################################
class Character_BG3:
    def __init__(self, name, race, class_type, alignment):
        self.name = name
        self.race = race
        self.class_type = class_type
        self.alignment = alignment
        
    def introduce(self):
        return f"Name: {self.name}, Race: {self.race}, Class Type: {self.class_type}, Alignment: {self.alignment}"
    
##################################################################################################

######## Problem 10: Harry Potter ################################################################
class Wizard:
    def __init__(self, name, house, wand, status):
        self.name = name
        self.house = house
        self.wand = wand
        self.status = status
    
    def describe(self):
        return f"Name: {self.name}, House: {self.house}, Wand: {self.wand}, Status: {self.status}"
    
##################################################################################################

######## Problem 11: Game of Thrones #############################################################

##################################################################################################

######## Problem 12: Star Wars ###################################################################

##################################################################################################

######## Problem 13: The Lord of the Rings #######################################################
class Lord:
    def __init__(self, race, name, homeland, characteristics, occupation, status):
        self.race = race
        self.name = name
        self.homeland = homeland
        self.characteristics = characteristics
        self.occupation = occupation
        self.status = status
    def describe(self):
        return (f"Race: {self.race}, Homeland: {self.homeland}, Characteristics: {self.characteristics}\n"
                f"Name: {self.name}, Occupation: {self.occupation}, Status: {self.status}")


##################################################################################################

######## Problem 14: Marvel Superheroes ##########################################################

##################################################################################################

######## Problem 15: Pirates of the Caribbean ####################################################

##################################################################################################

######## Problem 16: Naruto ######################################################################


##################################################################################################

######## Problem 17: Doctor Who ##################################################################

##################################################################################################

######## Problem 18: Star Trek ###################################################################

##################################################################################################

######## Problem 19: Transformers ###############################################################

##################################################################################################

######## Problem 20: The Matrix ##################################################################

##################################################################################################
########################## -Your Code Ends Here- #################################################
##################################################################################################


##################################################################################################
####### XXXXXXXXXXX !!!DO NOT MODIFY THIS SECTION!!! XXXXXXXXXXX #######
##################################################################################################

def main(x):
    output = (your_ID(),)
    error_count = 0

    # Problem 1: Breaking Bad
    try:
        walter = Character_BB("Walter White", "Heisenberg", "Chemistry Teacher", "Deceased")
        print(walter.introduce())
        output = output + (walter.introduce(),)
    except Exception:
        output = output + ("Error",)
        error_count += 1
    print()
    # Problem 2: Lost
    try:
        island = Island("Mystery Island", "Pacific Ocean", 9)
        jack = Survivor("Jack", 35, "Doctor", island)
        print(island.describe())
        output = output + (island.describe(),)
        print(jack.introduce())
        output = output + (jack.introduce(),)
    except Exception:
        output = output + ("Error",)
        error_count += 1
    print()
    # Problem 3: Fullmetal Alchemist
    try:
        edward = Alchemist("Edward Elric", "State Alchemist", "Alchemy", "Active")
        print(edward.introduce())
        output = output + (edward.introduce(),)
    except Exception:
        output = output + ("Error",)
        error_count += 1
    print()
    # Problem 4: Sherlock
    try:
        sherlock = Detective("Sherlock Holmes", "Deduction", "John Watson", 100)
        print(sherlock.introduce())
        output = output + (sherlock.introduce(),)
    except Exception:
        output = output + ("Error",)
        error_count += 1
    print()
    # Problem 5: Death Note
    try:
        light = User("Light Yagami", "Kira", True, "Deceased")
        print(light.introduce())
        output = output + (light.introduce(),)
    except Exception:
        output = output + ("Error",)
        error_count += 1
    print()
    # Problem 6: Code Geass
    try:
        lelouch = KnightmarePilot("Lelouch Lamperouge", "Zero", "Black Knights", "Leader")
        print(lelouch.introduce())
        output = output + (lelouch.introduce(),)
    except Exception:
        output = output + ("Error",)
        error_count += 1
    print()
    # Problem 7: Assassin's Creed
    try:
        ezio = Assassin("Ezio Auditore", "Assassin", "Renaissance", "Active")
        print(ezio.introduce())
        output = output + (ezio.introduce(),)
    except Exception:
        output = output + ("Error",)
        error_count += 1
    print()
    # Problem 8: DOTA
    try:
        invoker = Hero("Invoker", "Mid", "Intelligence", "Radiant")
        print(invoker.introduce())
        output = output + (invoker.introduce(),)
    except Exception:
        output = output + ("Error",)
        error_count += 1
    print()
    # Problem 9: Baldur's Gate 3
    try:
        gale = Character_BG3("Gale", "Human", "Wizard", "Neutral Good")
        print(gale.introduce())
        output = output + (gale.introduce(),)
    except Exception:
        output = output + ("Error",)
        error_count += 1
    print()
    # Problem 10: Harry Potter
    try:
        harry = Wizard("Harry Potter", "Gryffindor", "Phoenix Feather Wand", "Active")
        print(harry.introduce())
        output = output + (harry.introduce(),)
    except Exception:
        output = output + ("Error",)
        error_count += 1
    print()
    # Problem 11: Game of Thrones
    try:
        stark = House("Stark", "Direwolf", "Winter is Coming", "The North")
        jon = Character_GoT("Jon Snow", "King in the North", stark, "Alive")
        print(stark.describe())
        output = output + (stark.describe(),)
    except Exception:
        output = output + ("Error",)
        error_count += 1
    try:
        print(jon.introduce())
        output = output + (jon.introduce(),)
    except Exception:
        output = output + ("Error",)
        error_count += 1
    print()
    # Problem 12: Star Wars
    try:
        luke = Jedi("Luke Skywalker", "Master", "Green", "Alive")
        print(luke.introduce())
        output = output + (luke.introduce(),)
    except Exception:
        output = output + ("Error",)
        error_count += 1
    print()
    # Problem 13: The Lord of the Rings
    try:
        elf_race = Race("Elf", "Rivendell", "Immortal")
        aragorn = Character_LoTR("Aragorn", elf_race, "Ranger", "Alive")
        print(elf_race.describe())
        output = output + (elf_race.describe(),)
    except Exception:
        output = output + ("Error",)
        error_count += 1
    try:
        print(aragorn.introduce())
        output = output + (aragorn.introduce(),)
    except Exception:
        output = output + ("Error",)
        error_count += 1
    print()
    # Problem 14: Marvel Superheroes
    try:
        spiderman = Superhero("Peter Parker", "Spiderman", "Super Agility", "Avengers")
        print(spiderman.introduce())
        output = output + (spiderman.introduce(),)
    except Exception:
        output = output + ("Error",)
        error_count += 1
    print()
    # Problem 15: Pirates of the Caribbean
    try:
        jack_sparrow = Pirate("Jack Sparrow", "Black Pearl", "Captain", "Alive")
        print(jack_sparrow.introduce())
        output = output + (jack_sparrow.introduce(),)
    except Exception:
        output = output + ("Error",)
        error_count += 1
    print()
    # Problem 16: Naruto
    try:
        naruto = Shinobi("Naruto Uzumaki", "Hokage", 100, 500)
        print(f"Before mission: {naruto.chakra} chakra, {naruto.missions_completed} missions completed.")
        output = output + (f"Before mission: {naruto.chakra} chakra, {naruto.missions_completed} missions completed.",)
    except Exception:
        output = output + ("Error",)
        error_count += 1
    try:
        naruto.complete_mission(20)
        print(f"After mission: {naruto.chakra} chakra, {naruto.missions_completed} missions completed.")
        output = output + (f"After mission: {naruto.chakra} chakra, {naruto.missions_completed} missions completed.",)
    except Exception:
        output = output + ("Error",)
        error_count += 1
    try:
        naruto.recover_chakra(30)
        print(f"After recovery: {naruto.chakra} chakra.")
        output = output + (f"After recovery: {naruto.chakra} chakra.",)
    except Exception:
        output = output + ("Error",)
        error_count += 1
    print()
    # Problem 17: Doctor Who
    try:
        doctor = TimeLord("The Doctor", 12, 1200, ["Sonic Screwdriver"])
        print(f"{doctor.name}, Regenerations Left: {doctor.regenerations_left}")
        output = output + (f"{doctor.name}, Regenerations Left: {doctor.regenerations_left}",)
    except Exception:
        output = output + ("Error",)
        error_count += 1
    try:
        print(doctor.use_gadget("Sonic Screwdriver"))
        output = output + (doctor.use_gadget("Sonic Screwdriver"),)
    except Exception:
        output = output + ("Error",)
        error_count += 1
    try:
        doctor.regenerate()
        print(f"After regeneration: Age: {doctor.current_age}, Regenerations Left: {doctor.regenerations_left}")
        output = output + (f"After regeneration: Age: {doctor.current_age}, Regenerations Left: {doctor.regenerations_left}",)
    except Exception:
        output = output + ("Error",)
        error_count += 1
    print()
    # Problem 18: Star Trek
    try:
        enterprise = Starship("Enterprise", 430, 9.5, "Earth")
        print(f"Starship: {enterprise.name}, Crew Size: {enterprise.crew_size}, Warp Speed: {enterprise.warp_speed}")
        output = output + (f"Starship: {enterprise.name}, Crew Size: {enterprise.crew_size}, Warp Speed: {enterprise.warp_speed}",)
    except Exception:
        output = output + ("Error",)
        error_count += 1
    try:
        print(enterprise.travel(100))
        output = output + (enterprise.travel(100),)
    except Exception:
        output = output + ("Error",)
        error_count += 1
    try:
        enterprise.recruit_crew(10)
        print(f"New Crew Size: {enterprise.crew_size}")
        output = output + (f"New Crew Size: {enterprise.crew_size}",)
    except Exception:
        output = output + ("Error",)
        error_count += 1
    print()
    # Problem 19: Transformers
    try:
        optimus = Transformer("Optimus Prime", "Robot", 100, 80)
        print(f"{optimus.name}, Form: {optimus.form}, Strength: {optimus.strength}, Energy: {optimus.energy}")
        output = output + (f"{optimus.name}, Form: {optimus.form}, Strength: {optimus.strength}, Energy: {optimus.energy}",)
    except Exception:
        output = output + ("Error",)
        error_count += 1
    try:
        optimus.transform()
        print(f"After transformation: Form: {optimus.form}")
        output = output + (f"After transformation: Form: {optimus.form}",)
    except Exception:
        output = output + ("Error",)
        error_count += 1
    try:
        print(f"Battle result: {optimus.battle(150)}")
        output = output + (f"Battle result: {optimus.battle(200)}",)
    except Exception:
        output = output + ("Error",)
        error_count += 1
    print()
    # Problem 20: The Matrix
    try:
        neo = MatrixCharacter("Neo", ["Martial Arts"], 10, 100)
        print(f"{neo.name}, Skills: {neo.skills}, Matrix Level: {neo.matrix_level}, Health: {neo.health}")
        output = output + (f"{neo.name}, Skills: {neo.skills}, Matrix Level: {neo.matrix_level}, Health: {neo.health}",)
    except Exception:
        output = output + ("Error",)
        error_count += 1
    try:
        neo.learn_skill("Gun Mastery")
        print(f"After learning: {neo.skills}")
        output = output + (f"After learning: {neo.skills}",)
    except Exception:
        output = output + ("Error",)
        error_count += 1
    try:
        print(neo.take_damage(50))
        output = output + (neo.take_damage(50),)
    except Exception:
        output = output + ("Error",)
        error_count += 1
    print("Total Error -", error_count)    
    return output

##################################################################################################

if __name__ == "__main__":
    main(0)
