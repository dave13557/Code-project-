def list_centers():
    centers = {
        "Central Elementary School": 500,
        "Barangay Hall": 300,
        "City Gymnasium": 1000,
        "Covered Court": 200,
    }
    print("\n🏠 Evacuation Centers:")
    for name, capacity in centers.items():
        print(f"- {name} (Capacity: {capacity})")
