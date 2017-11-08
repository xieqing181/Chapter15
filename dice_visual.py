from die import Die
import pygal

die1 = Die()
die2 = Die()

results = []

for roll_num in range(1000):
	result = die1.roll() + die2.roll()
	results.append(result)
	
#analyse the result
frequencies = []

max_result = die1.num_sides + die2.num_sides
for value in range(1, max_result+1):
	frequency = results.count(value)
	frequencies.append(frequency)
	
#print(frequencies)
#try to show the result in grafic

hist = pygal.Bar()

hist.title = "Result of rolling D6 1000 times"
hist.x_labels = []

for x in range(1, 13):
	hist.x_labels.append(str(x))
	
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6', frequencies)
hist.render_to_file('dice_visual.svg')
