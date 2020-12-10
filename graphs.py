# First import pygal
import pygal
# Then create a bar graph object
bar_chart = pygal.Bar()
bar_chart.add('C++', [74])  # Add some values
bar_chart.add('Python', [67])  # Add some values
bar_chart.add('C', [77])  # Add some values
bar_chart.add('Java', [98])  # Add some values
# Save the svg to a file
bar_chart.render_to_file('bar_chart.svg')
