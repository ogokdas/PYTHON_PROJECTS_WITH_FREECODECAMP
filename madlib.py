name = input("Enter a name: ")
size = input("Enter a size (tall or short): ")
eye_color = input("Enter a eye color: ")
hair_color = input("Enter a hair color: ")
male_female = input("Enter a sex (male or female): ")
age = input("Enter an age: ")
countries = [input("Enter a country: "), input("Enter a country more: ")]
team = input("Enter a team: ")
language = input("Enter a software language: ")
adj = input("Enter difficult or easy: ")
oop_func = input("Enter oop or functional: ")
ide = input("Enter an IDE name for software development: ")

madlib = f"\n\n{name.capitalize()} is a {size}, {eye_color}-eyed, {hair_color}-haired {male_female}. " \
         f"{name.capitalize()} is {age} years old. " \
         f"\n{name.capitalize()} loves to travel. The countries he visited are {countries[0].capitalize()} and {countries[1].capitalize()}. " \
         f"\n{name.capitalize()} supports the {team.capitalize()} team. " \
         f"\n\n{name.capitalize()} is dealing with software development. " \
         f"\nThe programming language he knew best is {language}. " \
         f"\n{language.capitalize()} is an {adj} language to learn. " \
         f"\n{language.capitalize()} is an {oop_func} based language. " \
         f"\n{name.capitalize()} uses {ide}  to write codes. " \
         f"\n{ide.capitalize()} is a widely used platform."

print(madlib)