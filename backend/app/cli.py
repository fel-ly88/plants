from datetime import datetime
from .database import session
from .models import Plant, Category, Watering

# __define-ocg__ Ensuring main CLI runs all options cleanly


def main_menu():
    while True:
        print("\n=== Plant Management CLI ===")
        print("1. Add new plant")
        print("2. List all plants")
        print("3. Update plant details")
        print("4. Record watering")
        print("5. List watering history")
        print("6. Add new category")
        print("7. Exit")
        print("8. List all categories")  # ✅ new menu option

        choice = input("Enter choice: ").strip()

        if choice == '1':
            add_plant()
        elif choice == '2':
            list_plants()
        elif choice == '3':
            update_plant()
        elif choice == '4':
            record_watering()
        elif choice == '5':
            list_watering_history()
        elif choice == '6':
            add_category()
        elif choice == '7':
            print("Exiting... Goodbye!")
            break
        elif choice == '8':
            list_categories()
        else:
            print("Invalid choice. Try again.")

# --- Plant CRUD ---


def add_plant():
    name = input("Plant name: ").strip()
    species = input("Species: ").strip()
    location = input("Location: ").strip()
    try:
        freq = int(input("Watering frequency (days): ").strip())
    except ValueError:
        print("Invalid frequency. Must be a number.")
        return

    categories = session.query(Category).all()
    if not categories:
        print("⚠️ No categories available. Please add one first!")
        return

    print("\n--- Categories ---")
    for idx, c in enumerate(categories, 1):
        print(f"{idx}. {c.name} - {c.description}")

    try:
        choice = int(input("Select category by number: ").strip())
        if choice < 1 or choice > len(categories):
            print("Invalid category choice.")
            return
        category = categories[choice - 1]
    except ValueError:
        print("Invalid input.")
        return

    plant = Plant(
        name=name,
        species=species,
        location=location,
        watering_frequency=freq,
        category=category
    )
    session.add(plant)
    session.commit()
    print(
        f"✅ Plant '{name}' added successfully under category '{category.name}'!")


def list_plants():
    plants = session.query(Plant).all()
    if not plants:
        print("No plants found.")
        return
    print("\n--- All Plants ---")
    for p in plants:
        print(f"{p.id}. {p.name} ({p.species}) - Location: {p.location}, "
              f"Water every {p.watering_frequency} days, "
              f"Category: {p.category.name if p.category else 'None'}")


def update_plant():
    list_plants()
    try:
        plant_id = int(input("Enter Plant ID to update: ").strip())
        plant = session.get(Plant, plant_id)
        if not plant:
            print("Plant not found.")
            return
    except ValueError:
        print("Invalid ID.")
        return

    plant.name = input(f"Name [{plant.name}]: ").strip() or plant.name
    plant.species = input(
        f"Species [{plant.species}]: ").strip() or plant.species
    plant.location = input(
        f"Location [{plant.location}]: ").strip() or plant.location

    try:
        freq_input = input(
            f"Watering frequency [{plant.watering_frequency}]: ").strip()
        plant.watering_frequency = int(
            freq_input) if freq_input else plant.watering_frequency
    except ValueError:
        print("Invalid frequency input.")
        return

    categories = session.query(Category).all()
    if categories:
        print("\n--- Categories ---")
        for idx, c in enumerate(categories, 1):
            print(f"{idx}. {c.name} - {c.description}")

        cat_choice = input(
            f"Select category number (leave blank to keep current): ").strip()
        if cat_choice:
            try:
                choice_idx = int(cat_choice) - 1
                if 0 <= choice_idx < len(categories):
                    plant.category = categories[choice_idx]
                else:
                    print("Invalid choice. Keeping old category.")
            except ValueError:
                print("Invalid input. Keeping old category.")

    session.commit()
    print(f"✅ Plant '{plant.name}' updated successfully!")
# --- Watering ---


def record_watering():
    list_plants()
    try:
        plant_id = int(input("Enter Plant ID to water: ").strip())
        plant = session.get(Plant, plant_id)
        if not plant:
            print("Plant not found.")
            return
    except ValueError:
        print("Invalid ID.")
        return

    try:
        amount = float(input("Amount of water (liters): ").strip())
    except ValueError:
        print("Invalid amount.")
        return

    watering = Watering(
        plant=plant,
        date=datetime.now().date(),
        amount=amount
    )
    session.add(watering)
    session.commit()
    print(f"✅ Watering recorded for '{plant.name}'.")


def list_watering_history():
    list_plants()
    try:
        plant_id = int(input("Enter Plant ID to view history: ").strip())
        plant = session.get(Plant, plant_id)
        if not plant:
            print("Plant not found.")
            return
    except ValueError:
        print("Invalid ID.")
        return

    if not plant.waterings:
        print("No watering records found.")
        return

    print(f"\n--- Watering History for {plant.name} ---")
    for w in plant.waterings:
        print(f"{w.date} - {w.amount} liters")

# --- Category ---


def add_category():
    name = input("Category name: ").strip()
    description = input("Description: ").strip()
    category = Category(name=name, description=description)
    session.add(category)
    session.commit()
    print(f"✅ Category '{name}' added successfully!")


def list_categories():
    categories = session.query(Category).all()
    if not categories:
        print("No categories available. Add one first!")
        return
    print("\n--- Categories ---")
    for c in categories:
        print(f"{c.id}. {c.name} - {c.description}")


# --- Entry point ---
if __name__ == "__main__":
    varOcg = "PlantCLI"
    main_menu()
