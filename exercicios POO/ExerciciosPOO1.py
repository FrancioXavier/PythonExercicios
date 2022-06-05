import matplotlib.pyplot as plt


class Circle:
    def __init__(self, xCenter, yCenter, radius):
        self.xcenter = xCenter
        self.ycenter = yCenter
        self.radius = radius

    def CreateCircle(self):
        circle = plt.Circle((self.xcenter, self.ycenter), radius=self.radius, fc='g')
        return circle

    def ShowShape(self, patch):
        patch = patch
        ax = plt.gca()
        ax.add_patch(patch)

        plt.axis('scaled')
        plt.show()
