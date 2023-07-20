import copy
import random

class Hat:

    def __init__(self, **kwargs):
        self.contents = list()
        for key, value in kwargs.items():
            for _ in range(value):
                self.contents.append(str(key))

    def __str__(self):
        str_final = " ".join(self.contents)
        return str_final

    def draw(self, draw_number):
        str_final = ""
        if draw_number > len(self.contents):
            str_final += " ".join(self.contents)
        else:
            removed_balls = list()
            for _ in range(draw_number):
                random_elem = random.choice(self.contents)
                removed_balls.append(random_elem)
                self.contents.remove(random_elem)
            str_final += " ".join(removed_balls)
        return list(str_final.split(" "))

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    # Number of times program chooses 'at least' number of expected_balls
    successes = 0

    for _ in range(num_experiments):
        # Create a copy of the original hat object
        hat_copy = copy.deepcopy(hat)

        # Create dictionary to see if expected_balls outcome is matched to drawn_balls
        drawn_balls = hat_copy.draw(num_balls_drawn)
        drawn_balls_dic = dict()
        for value in drawn_balls:
            drawn_balls_dic[value] = drawn_balls_dic.get(value, 0) + 1

        criteria_met = 0
        criteria_required = len(expected_balls)
        for k, v in expected_balls.items():
            if k in drawn_balls_dic.keys():
                if drawn_balls_dic[k] >= expected_balls[k]:
                    criteria_met += 1
                else:
                    break
        if criteria_met == criteria_required:
            successes += 1

    return successes / num_experiments

