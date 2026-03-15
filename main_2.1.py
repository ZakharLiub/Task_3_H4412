import random
class Human:
    def __init__(self, name, job=None, home=None, car=None):
        self.name = name
        self.money = 100
        self.job = job
        self.gladness = 50
        self.satiety = 50
        self.car = car
        self.home = home
    def get_home(self):
        pass
    def get_car(self):
        pass
    def get_job(self):
        self.job = Job(job_list)
    def eat(self):
        pass
    def work(self):
        pass
    def shopping(self):
        self.gladness += 10
        self.money -= 20
    def clean_home(self):
        self.gladness -= 5
    def chill(self):
        self.gladness += 15

job_list = {
    "Java developer": {"salary":50, "gladness_less":3}
    "Python": {"salary":150, "gladness_less":5}
}

class Job:
    def __init__(self, job_list):
        self.job = random.choice(job_list)
        print(self.job)

nick = Human(name="Nick")
nick.get_job()