import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Set up parameters
length = 1
g = 9.81
damping_coefficient = 0.2
omega = np.sqrt(g/length)

# Set up time vector
t_max = 20
t = np.arange(0, t_max, 0.02)

# Set the initial angle 
theta0 = np.pi/2

# Set up figure and axis
fig = plt.figure(figsize=(10, 6))
ax1 = plt.subplot2grid((2, 2), (0, 0), rowspan=2)
ax2 = plt.subplot2grid((2, 2), (0, 1))
ax3 = plt.subplot2grid((2, 2), (1, 1))

# Adjust the spacing between the plots
fig.subplots_adjust(wspace=0.25,hspace=0.4)

# Set up pendulum position as a function of time
def pendulum_position(t):
    theta = theta0 * np.exp(-t*damping_coefficient/2) * np.cos(omega*t)
    x = length*np.sin(theta)
    y = -length*np.cos(theta)

    return x, y

# Set up pendulum animation
pendulum, = ax1.plot([], [], 'o-', lw=2)

# Set up circle plot
x, y = pendulum_position(t[0])
circle, = ax1.plot(x, y, 'o', ms = 10)
circle.set_markeredgecolor('red')

def update(num):
    x, y = pendulum_position(t[num])
    pendulum.set_data([0,x], [0,y])
    circle.set_data(x, y)
    angle_plot.set_data(t[:num], np.rad2deg(np.arcsin(pendulum_position(t[:num])[0])))

    # Calculate and plot the acceleration
    acceleration = -(g/length) * np.sin(np.arcsin(pendulum_position(t[:num])[0]))
    acceleration_plot.set_data(t[:num], acceleration)

    # Set the title of the plot to the current time value
    ax1.set_title("Time: {:.2f} s".format(t[num]))

    return pendulum, circle, angle_plot, acceleration_plot

# Set up angle plot
angle_plot, = ax2.plot(t, np.rad2deg(np.arcsin(pendulum_position(t)[0])))
ax2.set_title("Angle over time t")

# Set up acceleration plot
acceleration_plot, = ax3.plot(t, -(g/length) * np.sin(np.arcsin(pendulum_position(t)[0])))
ax3.set_title("Acceleration over time t")

# Set up plot limits
ax1.set_xlim(-1.1*length, 1.1*length)
ax1.set_ylim(-1.1*length, 0.1*length)
ax1.set_aspect('equal')
ax1.grid()

# Add a horizontal line at y=0 to the second and third plots
ax2.axhline(y=0, color='grey', linestyle='--',lw = 1)
ax3.axhline(y=0, color='grey', linestyle='--',lw = 1)

ax2.set_xlabel("t (s)")
ax2.set_ylabel(r'$\theta$ (deg)')
ax2.grid()

ax3.set_xlabel("t (s)")
ax3.set_ylabel("Acceleration (m/s^2)")
ax3.grid()

# Set the x,y-axis limits of the second and third plots
ax2.set_xlim(0, t_max)
ax3.set_xlim(0, t_max)
ax2.set_ylim(-100, 100)
ax3.set_ylim(-10, 10)

# Set the y-axis tick marks for the second plot
ax2.set_yticks([-np.rad2deg(theta0), -45, 0, 45, np.rad2deg(theta0)]) 

animation = FuncAnimation(fig, update, frames=range(len(t)), interval=1)

plt.show()
