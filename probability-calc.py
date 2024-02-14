import random
import copy
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs) -> None:
        self.contents = []
        for key, value in kwargs.items():
            for i in range(value):
                self.contents.append(f"{key}")
    
    def draw(self,num_of_balls:int)->list:
        if num_of_balls > len(self.contents):
            num_of_balls = len(self.contents)
        ret_arr = []
        for i in range(num_of_balls):
            ret_arr.append(self.contents.pop(random.randint(0, len(self.contents)-1)))
        return ret_arr
    
    def __str__(self):
        return str(self.contents)

def experiment(hat, expected_balls:dict, num_balls_drawn:int, num_experiments:int) -> float:
    successful = 0
    for i in range(num_experiments):
        experiment = copy.deepcopy(hat).draw(num_balls_drawn)
        test_length = len(experiment)
        for key, value in expected_balls.items():
            for i in range(value):
                try:
                    experiment.remove(key)
                except ValueError:
                    pass
                test_length -=1
        if len(experiment) == test_length:
            successful+=1
    return successful/num_experiments


random.seed(95)
hat = Hat(blue=3,red=2,green=6)
probability = experiment(hat=hat, expected_balls={"blue":2,"green":1}, num_balls_drawn=1, num_experiments=1000)
print(probability)
