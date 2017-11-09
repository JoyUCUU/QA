from die import Die
import pygal

#创建一个D6
die_1 = Die()
die_2 = Die()

#投掷几次骰子，并把结果存储在一个列表中
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

#分析结果
frequencies = []
max_result = die_1.num_sizes + die_2.num_sizes
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

#对结果进行可视化
hist = pygal.Bar()

hist.title = "Result of rolling one D6 1000 times."
hist.x_labels = ['2','3','4','5','6','7','8','9','10','11','12','13']
hist.x_title = 'Result'
hist._y_title = 'Frequency of Result!'

hist.add('D6 + D6', frequencies)
hist.render_to_file('die_visual.svg')


