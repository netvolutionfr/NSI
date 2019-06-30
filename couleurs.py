import matplotlib
import matplotlib.pyplot as plt


def couleur(r, v, b):
    return True


rectangle = matplotlib.patches.Rectangle((-200, -100), 400, 200, color='#EB70AA')


fig = plt.figure()
ax = fig.add_subplot(111)
ax.add_patch(rectangle)

plt.xlim([-200, 200])
plt.ylim([-100, 100])
plt.axis('off')
plt.show()
