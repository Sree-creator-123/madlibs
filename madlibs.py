print("Welcome to Mad Libs Python edition")

madlibs = ["1. Summer Trip", "2. Our Cafeteria", "3. Chocolate Bunny", "4. Birthday Party"]
for a in madlibs:
    print(a)
    
person = int(input("Pick a number: "))

while True == True:
    if person == 1:
        person1 = input("Person: ")
        place1 = input("Place: ")
        adjective1 = input("Adjective: ")
        place2 = input("Place: ")
        pluralnoun1 = input("Plural Noun: ")
        adjective2 = input("Adjective: ")
        pluralnoun2 = input("Plural Noun: ")
        place3 = input("Place: ")
        actionverb1 = input("Action Verb: ")
        pluralnoun3 = input("Plural Noun: ")
        pluralnoun4 = input("Plural Noun: ")
        noun1 = input("Noun: ")
        actionverb2 = input("Action Verb: ")
        actionverb3 = input("Action Verb: ")
        adjective3 = input("Adjective: ")
        print("Last summer, my mom and dad took me and " +person1, "on a trip to " +place1, ". The weather there is very " +adjective1, "! Northern " +place2, "has many " +pluralnoun1, ", and they make " +adjective2,"" +pluralnoun2, "there. Many people also go to " +place3, "to " +actionverb1, "or see the " +pluralnoun3, ". The people that love to live there eat " +pluralnoun4, "and are proud of their big " +noun1, ". They also like to " +actionverb2, "in the sun and swim in the " +actionverb3, ". It was a really " +adjective3, "trip!")
        break
    if person == 2:
        adjective1 = input("Adjective: ")
        verb1 = input("Verb: ")
        adjective2 = input("Adjective: ")
        noun1 = input("Noun: ")
        verb2 = input("Verb: ")
        adjective3 = input("Adjective: ")
        noun2 = input("Noun: ")
        adjective4 = input("Adjective: ")
        adjective5 = input("Adjective: ")
        noun3 = input("Noun: ")
        noun4 = input("Noun: ")
        print("Our school cafeteria has really " +adjective1, "food. Just thinking about makes my stomach " +verb1, ". The spaghetti is " +adjective2, "and tastes like " +noun1, ". One day, I swear one of the meatballs started to " +verb2, "! The turkey tacos are totally " +adjective3, "and look kind of like old " +noun2, ". My friend Dana actually likes the meatloaf, even though it's " +adjective4, "and " +adjective5, ". I call it 'mystery meatloaf' and think it's really made out of " +noun3, ". My dad said he'd make my lunches, but the first day, he made me a sandwich out of " +noun4, "and peanut butter. I think I'd rather take my chances with the cafeteria!")
        break
    if person == 3:
        nouns1 = input("Nouns: ")
        number1 = input("Number: ")
        adjective1 = input("Adjective: ")
        noun1 = input("Noun: ")
        game1 = input("A Game: ")
        adjective2 = input("Adjective: ")
        color1 = input("Color: ")
        liquid1 = input("Liquid: ")
        noun2 = input("Noun: ")
        nouns2 = input("Nouns: ")
        noun3 = input("Noun: ")
        adjective3 = input("Adjective: ")
        print("Schools are closed at Easter time and all the " +nouns1, "get " +number1, "weeks off. The " +adjective1, "teachers also get vacation. There are lots of things to do on Easter vacation. Some kids hang around and watch the " +noun1, ". Others go outside and play " +game1, ". Little kids will color " +adjective2, "eggs. They use a package of " +color1, "dye. They pour it in a bowl full of " +liquid1, ". Then they dip the " +noun2, "in the bowl and then rinse off. After the " +nouns2, "are dried, you place them in the Easter " +noun3, "along with a " +adjective3, "chocolate bunny!")
        break
    if person == 4:
        verbing1 = input("Verb(ing): ")
        adverb1 = input("Adverb: ")
        adjective1 = input("Adjective: ")
        verbing2 = input("Verb(ing): ")
        name1 = input("Name: ")
        name2 = input("Name: ")
        name3 = input("Name: ")
        place1 = input("Place: ")
        adjective2 = input("Adjective: ")
        pluralnoun1 = input("Plural Noun: ")
        color1 = input("Color: ")
        pluralnoun2 = input("Plural Noun: ")
        verb1 = input("Verb: ")
        food1 = input("Food: ")
        food2 = input("Food: ")
        verb2 = input("Verb: ")
        verb3 = input("Verb: ")
        partofbody1 = input("Part of body: ")
        animal1 = input("Animal: ")
        verb4 = input("Verb: ")
        pluralnoun3 = input("Plural Noun: ")
        verbing3 = input("Verb(ing): ")
        verbing4 = input("Verb(ing): ")
        verbing5 = input("Verb(ing): ")
        adjective3 = input("Adjective: ")
        print("I'm " +verbing1, "a " +adverb1, "party for my birthday. I'm " +verbing2, "my best friends, like " +name1, "and " +name2, "and " +name3, ". The party will be at the " +place1, "with " +adjective2,"" +pluralnoun1, "and " +color1,"" +pluralnoun2, "for decorations. First we will " +verb1, "some snacks, like " +food1, "and " +food2, ", and then we will " +verb2, "some party games, like " +verb3, "the " +partofbody1, "on the " +animal1, "and " +verb4, "the " +pluralnoun3, ". Then comes my faorite part: " +verbing3, "Happy Birthday, " +verbing4, "presents and " +verbing5, "some " +adjective3, "cake.")
        break
    
