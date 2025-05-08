from user import login
from alert import send_alert 
from evacuation_center import list_centers
from route import view_routes
from volunteer import register_volunteer

def main():
    print("Welcome to SDREMS - Smart Disaster Response and Evacuation Management System")
    
    
    user = login()
    
    
    if user:
        while True:
            print("\nMenu:")
            print("1. Send Alert")
            print("2. View Evacuation Centers")
            print("3. View Evacuation Routes")
            print("4. Register Volunteer")
            print("5. Exit")

            choice = input("Choose an option: ")
            
            # Menu options and corresponding function calls
            if choice == "1":
                send_alert()
            elif choice == "2":
                list_centers()
            elif choice == "3":
                view_routes()
            elif choice == "4":
                register_volunteer()
            elif choice == "5":
                print("Exiting SDREMS. Stay safe!")
                break
            else:
                print("Invalid choice. Try again.")
    else:
        print("Login failed. Exiting program.")

if __name__ == "__main__":
    main()