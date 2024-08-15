
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint
class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = []

    # This method generates a unique 'id' when adding members into the list
    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):
        # Ensure the member has the correct structure
        if not all(key in member for key in ['first_name', 'age', 'lucky_numbers']):
            raise ValueError("Member must have 'first_name', 'age', and 'lucky_numbers'")
        if not isinstance(member['age'], int) or member['age'] <= 0:
            raise ValueError("'age' must be a positive integer")
        if not isinstance(member['lucky_numbers'], list) or not all(isinstance(num, int) for num in member['lucky_numbers']):
            raise ValueError("'lucky_numbers' must be a list of integers")

        # Add the last name and generate an id
        member['last_name'] = self.last_name
        member['id'] = self._generate_id()
        self._members.append(member)

    def delete_member(self, id):
        # Remove member by id
        self._members = [member for member in self._members if member['id'] != id]

    def get_member(self, id):
        # Find and return the member by id
        for member in self._members:
            if member['id'] == id:
                return member
        return None

    def get_all_members(self):
        return self._members
