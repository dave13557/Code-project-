class VolunteerNode:
    def __init__(self, name, skill):
        self.name = name
        self.skill = skill
        self.next = None

class VolunteerList:
    def __init__(self):
        self.head = None

    def register(self, name, skill):
        new_volunteer = VolunteerNode(name, skill)
        if not self.head:
            self.head = new_volunteer
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_volunteer
        print(f"✅ Volunteer '{name}' with skill '{skill}' has been registered.")

    def list_volunteers(self):
        if not self.head:
            print("No volunteers registered yet.")
            return
        print("\n📋 Registered Volunteers:")
        current = self.head
        while current:
            print(f"- {current.name} ({current.skill})")
            current = current.next

    def to_list(self):
        data = []
        current = self.head
        while current:
            data.append({"name": current.name, "skill": current.skill})
            current = current.next
        return data

    def load_from_list(self, data):
        for item in data:
            self.register(item['name'], item['skill'])
