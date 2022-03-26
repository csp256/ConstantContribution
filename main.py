x = 50 # initial value
c = 66 # contribution
g = 1.07 # growth 
n = 10 # periods (years)
y = 10 # periods to make contribution 

########################################
# You only need to edit the above,
# and then click green "Run" button.
# Click on image filenames to the left.
########################################

import matplotlib.pyplot as plt

current_value = []
terminal_value = []

print("year :: value :: end value if you stopped investing")
for i in range(n + 1):
  current_value.append(x)
  terminal_value.append(x * (g**(n-i)))
  print('{:3d}'.format(i) + " :: " + '{:15,.2f}'.format(x) + " :: " + '{:15,.2f}'.format(terminal_value[-1]))
  if i < y:
    x += c 
  x *= g

plt.plot(current_value)
plt.grid('both')
plt.xlabel('year')
plt.ylabel('value')
plt.title('current value')
plt.savefig('portfolio_value.png')

plt.clf()
plt.plot(terminal_value)
plt.grid('both') 
plt.xlabel('year')
plt.ylabel('future value')
plt.title('future value at year {} of current portfolio if you stopped contributing now'.format(n))
plt.savefig('terminal_value_if_stop_contribution.png')