#this function is to be able to compare the tools to conduct the data analysis of energy output from experimental renewable energy resources. all results will be listed in a paragraph 
def compare_tool_outputs(energy_outputs, tool_names):
    max_energy = max(energy_outputs)
    min_energy = min(energy_outputs)
    max_index = energy_outputs.index(max_energy)
    min_index = energy_outputs.index(min_energy)
    print(f"Tool '{tool_names[max_index]}' produces the highest energy output: {max_energy} megawatt hours")
    print(f"Tool '{tool_names[min_index]}' produces the lowest energy output: {min_energy} megawatt hours")
    return tool_names[max_index], tool_names[min_index]

#this contains the formula to calculate the total energy output produced. this allows for us to conduct data analysis to decide which methods of energy production are more practical for widespread usage.
def calculate_total_energy(solar_energy, wind_energy, hydro_energy, biomass_energy, geothermal_energy):
    total_energy_output = solar_energy + wind_energy + hydro_energy + biomass_energy + geothermal_energy
    return total_energy_output

#a function to compare this to the energy output necessary to be a sustainable source for household use. this is done to assess the usefullness of the option of renewable energy production.
def compare_results(actual_output, anticipated_output):
    if actual_output == anticipated_output:
        print("This energy source is sufficient to supply power to a household! This is an economically efficient, and sustainable route for energy supply in everyday homes.")
    else:
        print("The energy source," + str(tool_names) + " is not producing a the amount of energy for the power usage of an average family household. This may require some further analysis.")
        difference = actual_output - anticipated_output
        if difference > 0:
            print("This energy source, " + str(tool_names) + " has shown, the production of energy it outputs exceeds the need for an average household by", difference, "megawatt hours. This is a positive direction to lead further studies on renewable energy sources. If this tool for renewable energy persists in production results such as these, we may even be able to use this resource for larger energy needs. This finding could help save the world!")
        else:
            print("This energy source, " + tool_names + " has shown, the production of energy it outputs is less than the need for an average household by", abs(difference), "megawatt hours. This is an indication of this method being insufficient to power an average household. This tool may need be good for smaller usages of power. This, however, means it is not an efficient resource for daily household power generation.")

#this creates a list to hold the names of tools and energy outputs entered by researcher.
tool_names = []
tool_energy_outputs = []
energy_outputs = []

#this creates a loop that collects data for each tool.
for i in range(5):
    tool_name = input(f"Enter the name of tool {i+1}: ")
    tool_names.append(tool_name)

#a function to collect the data from the respective energy sources being studied. this allows for an iterative research process for an engineer or scientist to use for many different tools, methods, and resources.
    solar_energy = float(input(f"Enter the recorded solar energy output produced by "+tool_name+" in number of megawatt hours (megawatt hours): "))
    wind_energy = float(input(f"Enter the recorded wind energy output produced by "+tool_name+" in number of megawatt hours (megawatt hours): "))
    hydro_energy = float(input(f"Enter the recorded hydroelectric energy output produced by "+tool_name+" in number of megawatt hours (megawatt hours): "))
    biomass_energy = float(input(f"Enter the recorded biomass energy output produced by "+tool_name+" in number of megawatt hours (megawatt hours): "))
    geothermal_energy = float(input(f"Enter the recorded geothermal energy outputproduced by "+tool_name+" in number of megawatt hours (megawatt hours): "))   
    total_energy_output = calculate_total_energy(solar_energy, wind_energy, hydro_energy, biomass_energy, geothermal_energy)
    tool_energy_outputs.append(total_energy_output)
    energy_outputs.append(total_energy_output)

for tool_name, energy_output in zip(tool_names, tool_energy_outputs):
    print("The total renewable energy output from " + tool_name + " is " + str(energy_output) + " megawatt hours")

#comparative data. this is the average energy usage for an american household. this would be the amount of energy to sufficiently power an average house's generator.
anticipated_total_output = 8000  #this statistic was googled for this purpose.

#this calculates the energy that the respective tool, method, or otherwise resource is outputting in the time decided by researcher. 
energy_outputs.append(total_energy_output)

#this prints the energy output from this resource.
energy_output_strings = [str(output) for output in tool_energy_outputs]
print("The produced output from " + str(tool_names) + " is " + ", ".join(energy_output_strings) + " megawatt hours")

#this compares the experimental resources' energy output, to the output produced by a typical household generator.
compare_results(sum(tool_energy_outputs), anticipated_total_output)


#this simply points out which tool in those collected were able to produce the most energy, and which was the least.
best_tool, worst_tool = compare_tool_outputs(tool_energy_outputs, tool_names)
print(f"The tool that produced the most energy of those being compared is: {best_tool}. This discovery could be groundbreaking! Keep going!")
print(f"The tool that produced the least energy of those being compared is: {worst_tool}. Maybe it could be better. Keep trying!")