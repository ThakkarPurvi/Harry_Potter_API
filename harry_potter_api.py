import requests

def random_character(character_number):
    response = requests.get('http://hp-api.herokuapp.com/api/characters/students')
    harryPotter = response.json()

    return {
        'name': harryPotter[character_number]['name'],
        'house': harryPotter[character_number]['house'],
        'gender': harryPotter[character_number]['gender'],
        'eyeColour': harryPotter[character_number]['eyeColour']}

def save_results(character_name, character):
    with open(f"{character_name}.txt", "w") as file_results:
        output = f"{character}"
        file_results.write(output)

def run():
    character_number = int(input("What is the Character number you would like to see?"))
    character = random_character(character_number)
    name = character["name"]
    house = character["house"]
    gender = character["gender"]
    eyeColour = character["eyeColour"]
    name_text = f"\nName of the Character: {name}"
    house_text = f"House of the Character: {house}"
    gender_text = f"Character gender is: {gender}"
    eyeColour = f"Character eyeColour is: {eyeColour}"
    formatted_text = "\n".join([name_text, house_text, gender_text, eyeColour])

    if not character:
        print("No Characters found")
        return
    print(formatted_text)
    character_name = character["name"]
    save_results(character_name, formatted_text)
    return formatted_text

run()