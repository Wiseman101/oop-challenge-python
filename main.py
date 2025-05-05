# main.py

from pet import Pet
import time

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def intro():
    print("=" * 50)
    slow_print("🐾 Welcome to the Virtual Pet World 🐾")
    print("=" * 50)
    pet_name = input("🧸 What do you want to name your pet? 👉 ")
    pet = Pet(pet_name.capitalize())
    slow_print(f"\n✨ Great! You adopted {pet.name} 🐶. Take good care of them!\n")
    return pet

def menu():
    print("\n🕹️ What do you want to do?")
    print("1️⃣ Feed your pet")
    print("2️⃣ Put your pet to sleep")
    print("3️⃣ Play with your pet")
    print("4️⃣ Teach your pet a new trick")
    print("5️⃣ Show pet's tricks")
    print("6️⃣ Show pet status")
    print("7️⃣ Exit")

def game_loop(pet):
    while True:
        menu()
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            pet.eat()
        elif choice == '2':
            pet.sleep()
        elif choice == '3':
            pet.play()
        elif choice == '4':
            trick = input("🎓 Enter the trick you want to teach: ")
            pet.train(trick)
        elif choice == '5':
            pet.show_tricks()
        elif choice == '6':
            pet.get_status()
        elif choice == '7':
            slow_print(f"\n👋 Bye bye! {pet.name} will miss you... 🐾\n")
            break
        else:
            print("❌ Invalid choice. Try again.")

        time.sleep(1)

if __name__ == "__main__":
    my_pet = intro()
    game_loop(my_pet)
