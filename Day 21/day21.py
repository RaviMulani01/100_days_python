class Animal:

    def __init__(self):
        self.num_eye = 2

    
    def breathe(self):
        print("Inhale, exhale.")


class Fish(Animal):

    def __init__(self):
        # Recomnded not Mendetory.
        super().__init__()

    def breathe(self):
        super().breathe()
        print("doing this under water")

    def swim(self):
        print("moving in water.")


nemo = Fish()
nemo.breathe()
print(nemo.num_eye)
nemo.swim()