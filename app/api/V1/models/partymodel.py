"""Initializing an empty list to hold our data"""
party_list = []


class Party:

    def __init__(self):
        """Initializing class instance variables"""
        self.party = party_list

  """defines arguments for delete party route"""
   def delete_party(self, party_id):
        for party in party_list:
            if party in self.party:
                party_list.remove(party)


 