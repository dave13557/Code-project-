def list_centers():
    print("\nEvacuation Centers:")
    centers = [
        {"name": "Central Elementary School", "capacity": 500},
        {"name": "Barangay Hall", "capacity": 300},
        {"name": "City Gymnasium", "capacity": 1000},
    ]
    for center in centers:
        print(f"- {center['name']} (Capacity: {center['capacity']})")
