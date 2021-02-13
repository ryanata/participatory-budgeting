class User:

    def __init__(self, id, voted_dict=[]):
        self.id = id
        self.voted_dict = voted_dict # [Poll], can be set too
        