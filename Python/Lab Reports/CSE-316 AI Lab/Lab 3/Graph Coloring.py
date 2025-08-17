# Map of Australia using an adjacency list(map is collected form the lab manual)
australia_map = { #Dictionary
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW', 'T'],
    'T': ['V']
}

colors_sample = ['Red', 'Green', 'Blue', 'Yellow', 'Violet', 'Pink', 'White', 'Black', 'Purple', 'Grey'] # List of colors to use

numb_of_color = int(input("Enter the number of color: ")) #taking the inpurt from the user

colors=colors_sample[:numb_of_color] #taking the colors from the color set

# Dictionary to hold the assigned color of each region/vertics
region_colors = {}

def is_valid(region, color):
    for neighbor in australia_map[region]:
        if neighbor in region_colors and region_colors[neighbor] == color:
            return False
    return True

def color_map(region_index=0): #start with 0 number index.
    regions = list(australia_map.keys()) #collect the all region from the map list.

    if region_index == len(regions): #if all the region/vertics is visited/colored
        return True

    region = regions[region_index] #getting a region
    for color in colors: # taking colors
        if is_valid(region, color): # check if that color is valid to assign or not.
            region_colors[region] = color # if valid that means all neighbor has different color then assign that perticular color to that region.
            if color_map(region_index + 1): #recursion
                return True
            # Backtrack
            del region_colors[region] #if there is no solution for that colour then remove the color and try another one and procced.
    return False

#start
if color_map(): #if there is a solution
    print("Coloring is possible:")
    for region in australia_map:
        print(f"{region}: {region_colors[region]}")
else:
    print("No valid coloring found.")
