class Student:
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

    def change_name (self, accept_newName):
        self.name = accept_newName
    def change_age (self, accept_newAge):
        self.age = accept_newAge
    def add_track (self, accept_newTrack):
        self.tracks.append(accept_newTrack)
    def get_score(self):
        return self.score

Bob = Student(name="Bob", age="26", tracks=["nodejs", "python"], score=20.90)

Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()

print(f"{Bob.name} is {Bob.age} years old and is taking the {Bob.tracks[0], Bob.tracks[1], Bob.tracks[2]} track with a score of {Bob.score}")