"""Initializing an empty list to hold our data"""
party_list = []


class Party:

    def __init__(self):
        """Initializing class instance variables"""
        self.party = party_list


    def get_party_by_id(self, party_id):
        if self.party:
            for party in self.party:
                if party.get('party_id') == party_id:

                    return party


 