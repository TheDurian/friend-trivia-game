
import random
import json

with open("config.json", "r", encoding="utf-8") as config_file:
    config = json.loads(config_file.read())

for player in config["People"]:
    with open(f"{player}.txt", "w", encoding="utf-8") as player_file:
        for question_num in range(config["NumberOfQuestions"]):
            topic_dict = config["Topics"][random.randint(0, len(config["Topics"])-1)]
            topic = topic_dict["topic"]
            if topic_dict.get("modifier_chance") and random.random() < topic_dict["modifier_chance"]:
                topic += f" {topic_dict['modifiers'][random.randint(0, len(topic_dict['modifiers'])-1)]}"


            people = config["People"].copy()
            
            # Determine the people involved
            if random.random() < config["ChanceFor_Everybody"]:
                person = "everybody"
            elif random.random() < config["ChanceFor_Nobody"]:
                person = "nobody"
            else:
                person = ""
                if random.random() < config["ChanceFor_OnlyPeople"]:
                    person = "only"
                
                rand_person = people.pop(random.randint(0, len(people)-1))
                person = f"{person} {rand_person}".strip()
                while random.random() < config["ChanceFor_ExtraPerson"] and len(people):
                    rand_person = people.pop(random.randint(0, len(people)-1))
                    person = f"{person}+{rand_person}"
                
                if not len(people):
                    person = "everybody"

            suffix = topic_dict["suffixes"][random.randint(0, len(topic_dict["suffixes"])-1)]
            suffix = suffix.replace("%1", person)
            if "+" in person:
                suffix = suffix.replace("%2", "have")
            else:
                suffix = suffix.replace("%2", "has")
            
            if suffix.endswith("rate"):
                suffix += f" a {config['Ratings'][random.randint(0, len(config['Ratings'])-1)]}" 

            player_file.write(f"{topic} {suffix}\n")
