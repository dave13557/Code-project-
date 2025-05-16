def send_alert():
    print("\n📢 --- Send Disaster Alert ---")
    message = input("Enter alert message: ")
    area = input("Enter target area: ")
    print(f"\n🚨 ALERT SENT to {area}:\n\"{message}\"")
