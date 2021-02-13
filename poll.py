class Poll:

    def __init__(self, id, budget, user_list=[], option_list=[]):
        self.id = id
        self.budget = budget
        self.user_list = user_list
        self.option_list = option_list
        self.vote_list = {} # dict[Option] = [User]

    def add_user(self, user):
        pass

    def add_option(self, option):
        self.vote_list[option] = []
        pass

    def modify_option(self, option):
        pass

    def change_budget(self, budget):
        """Implement this such that only people with a certain privilege level can modify this"""
        pass

    def process_vote(self, user, voted_options):
        """Process when a voter votes in this poll

           Check if user has already voted; if so, remove all existing votes by that user first
           Checks that every option in voted_options exists in option_list
           Checks that the voted_options list is in budget
           For each option in voted_options add User"""
        pass

    def close_poll(self): # figure out which options won the election, output [Option]
        pass