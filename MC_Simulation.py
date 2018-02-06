import random
import matplotlib.pyplot as plt


# simulate how far from the initial point after taking n steps
def random_walk(n):
    x, y = 0, 0
    for _ in range(n):
        direction = random.choice(['N', 'S', 'W', 'E'])
        if direction == 'N':
            y += 1
        elif direction == 'S':
            y -= 1
        elif direction == 'W':
            x -= 1
        else:
            x += 1

    return x, y


# test
for _ in range(30):
    walk = random_walk(10)
    print walk, 'Distance from home =', abs(walk[0])+abs(walk[1])


# what is the longest random walk you take so that
# on average you will end up 4 blocks or fewer from home?

# 50% of the distance from home is less than 4
num_walks = 10000

# for each walk length, we do num_walks simulation
walk_length_plot = []
percentage_plot = []
for walk_length in range(1, 31):
    fewer_than_4 = 0
    for _ in range(num_walks):
        walk = random_walk(walk_length)
        if abs(walk[0])+abs(walk[1]) <= 4:
            fewer_than_4 += 1
    percentage = float(fewer_than_4)/num_walks
    # store the length and percentage to plot
    walk_length_plot.append(walk_length)
    percentage_plot.append(percentage)

    print 'Walk length is: ', walk_length, \
        '| The percentage of less than 4 is :', percentage


plt.scatter(walk_length_plot, percentage_plot)
plt.plot(walk_length_plot, percentage_plot)
plt.axhline(y=.5, color='r', linestyle='--')
plt.xlabel('WALK LENGTH')
plt.ylabel('PERCENTAGE')

