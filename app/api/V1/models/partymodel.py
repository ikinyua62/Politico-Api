"""Initializing an empty list to hold our data"""
party_list = []


class Party:

    def __init__(self):
        """Initializing class instance variables"""
        self.party = party_list

  """defines arguments for edit party route/ end point"""
    def edit_party(self, party_id, data):
        for party in party:
            if party('party_id') == party_id:
                name = data.get("name")
            if name:
                party["name"] = name
            return party


 