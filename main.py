from auth import login
from alert import send_alert
from centers import list_centers
from routes import view_routes
from volunteer import VolunteerList
from file_handler import save_volunteers, load_volunteers

def main():
    print("Welcome to EDRESMS System")
    print("EDRESMS - Enhancing Disaster Response and Evacuation through " \
    "a Smart Management System")

    volunteers = VolunteerList()
    volunteer_data = load_volunteers()
    volunteers.load_from_list(volunteer_data)

    user = login()
    if not user:
        return

    while True:
        print("\n📘 Main Menu:")
        print("1. Send Alert")
        print("2. View Evacuation Centers")
        print("3. View Evacuation Routes")
        print("4. Register Volunteer")
        print("5. List Registered Volunteers")
        print("6. Save Volunteers")
        print("7. Exit")

        choice = input("Choose an option (1-7): ")

        if choice == "1":
            send_alert()
        elif choice == "2":
            list_centers()
        elif choice == "3":
            view_routes()
        elif choice == "4":
            name = input("Volunteer Name: ")
            skill = input("Skill (e.g., medic, rescuer): ")
            volunteers.register(name, skill)
        elif choice == "5":
            volunteers.list_volunteers()
        elif choice == "6":
            save_volunteers(volunteers.to_list())
        elif choice == "7":
            print("👋 Exiting EDRESMS. Stay alert and safe!")
            break
        else:
            print("❗ Invalid input. Please choose a number from 1 to 7.")

if __name__ == "__main__":
    main()
