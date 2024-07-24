class Heart:
    def __init__(self, rate, usage):
        self.rate = rate
        self.usage = usage

    def beat(self):
        return "Heart is beating at {} bpm".format(self.rate)

    def state(self):
        if self.usage > 70:
            return "high blood pressure"
        else:
            return "feeling good"


class Brain:
    def __init__(self, iq, usage):
        self.iq = iq
        self.usage = usage

    def think(self):
        return "Brain is thinking with an IQ of {}".format(self.iq)


class Person:
    def __init__(self, name, age, heart_rate, heart_usage, brain_iq, brain_usage):
        self.name = name
        self.age = age
        self.heart = Heart(heart_rate, heart_usage)
        self.brain = Brain(brain_iq, brain_usage)

    def describe(self):
        return "Person: {}, Age: {}".format(self.name, self.age)

    def heart_status(self):
        return self.heart.beat()

    def heart_state(self):
        return self.heart.state()

    def brain_status(self):
        return self.brain.think()


class Leg:
    def __init__(self, person, moving_speed):
        self.person = person
        self.moving_speed = moving_speed

    def walk(self):
        return "{} is walking.".format(self.person.name)

    def activity(self):
        if self.moving_speed > 10:
            return "running"
        elif self.moving_speed > 0:
            return "walking"
        else:
            return "standing"


person = Person("Bob", 25, 84, 80, 120, 50)
leg = Leg(person, moving_speed=12)

print(person.describe())
print(person.heart_status())
print(person.heart_state())
print(person.brain_status())
print(leg.walk())
print("{} is currently {}.".format(person.name, leg.activity()))
