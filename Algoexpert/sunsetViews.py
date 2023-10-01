"""
Sunset Views:
This is an interesting question, we are supposed to say whether a building can view sunset based on the height of the building and the neighbouring height of the building.

"""

#  Time O(N) | Space O(N)
def sunsetViews(buildings, direction):
    building_with_views = []
    # Default iteration
    iter = range(len(buildings))
    if direction == 'EAST':
        iter = range(len(buildings) - 1, -1, -1)
    
    for idx in iter:
        if not building_with_views or buildings[idx] > buildings[building_with_views[-1]]:
            building_with_views.append(idx)
        
    return building_with_views if direction == 'WEST' else building_with_views[::-1]
