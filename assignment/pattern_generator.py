"""
DIGM 131 - Assignment 2: Procedural Pattern Generator
======================================================

OBJECTIVE:
    Use loops and conditionals to generate a repeating pattern of 3D objects
    in Maya. You will practice nested loops, conditional logic, and
    mathematical positioning.

REQUIREMENTS:
    1. Use a nested loop (a loop inside a loop) to create a grid or pattern
       of objects.
    2. Include at least one conditional (if/elif/else) that changes an
       object's properties (type, size, color, or position offset) based
       on its row, column, or index.
    3. Generate at least 25 objects total (e.g., a 5x5 grid).
    4. Comment every major block of code explaining your logic.

GRADING CRITERIA:
    - [25%] Nested loop correctly generates a grid/pattern of objects.
    - [25%] Conditional logic visibly changes object properties based on
            position or index.
    - [20%] At least 25 objects are generated.
    - [15%] Code is well-commented with clear explanations.
    - [15%] Pattern is visually interesting and intentional.

TIPS:
    - A 5x5 grid gives you 25 objects. A 6x6 grid gives you 36.
    - Use the loop variables (row, col) to calculate X and Z positions.
    - The modulo operator (%) is great for alternating patterns:
          if col % 2 == 0:    # every other column
    - You can vary: primitive type, height, width, position offset, etc.

COMMENT HABITS (practice these throughout the course):
    - Add a comment before each logical section explaining its purpose.
    - Use inline comments sparingly and only when the code is not obvious.
    - Keep comments up to date -- if you change the code, update the comment.
"""

import maya.cmds as cmds

# Clear the scene.
cmds.file(new=True, force=True)


def generate_pattern():
    """Generate a procedural pattern of objects using nested loops.

    This function should:
        1. Define variables for rows, columns, and spacing.
        2. Use a nested for-loop to iterate over rows and columns.
        3. Inside the loop, use a conditional to vary object properties.
        4. Create and position each object.
    """
    # --- Configuration variables ---
    num_rows = 5        # Number of rows in the pattern.
    num_cols = 5        # Number of columns in the pattern.
    spacing = 3.0       # Distance between object centers.

    # loop controling rows for Z
    for current_row in range(num_rows):
        # loop controls columns for Z
        for current_column in range(num_cols):
             
               # Calculate position for each object
                position_x = current_column * spacing
                position_z = current_row * spacing
    
                # Use modulo 3 to go through the 3 object types
                pattern_index = (current_row + current_column) % 3

                # Use (row+column) % 3 to create patterns
                if pattern_index == 0:
                    # create first pattern type: Cube
                    created_object = cmds.polyCube()[0]
                    object_height_scale = 1 + (current_row * 0.3)
                    object_color = (1, 0, 0)  # Red

                elif pattern_index == 1:
                    # create second pattern type: Sphere
                    created_object = cmds.polySphere()[0]
                    object_height_scale = 1 + (current_column * 0.3)
                    object_color = (0, 0, 1)  # Blue

                else:
                    # create pattern type: Cylinder 
                    created_object = cmds.polyCylinder()[0]
                    object_height_scale = 1 + ((current_row + current_column) * 0.2)
                    object_color = (0, 1, 0)  # Green


                # Move object into grid position using the calculated coordinates
                cmds.move(position_x, 0, position_z, created_object)

                # Scale only in Y to show height variety while keeping base consistent
                cmds.scale(1, object_height_scale, 1, created_object)
            
                # Each object gets its own shader so color differs are clear
                material_shader = cmds.shadingNode("lambert", asShader=True)

                # Apply RGB values defined in the conditional
                cmds.setAttr(material_shader + ".color",object_color[0],object_color[1],object_color[2],type="double3")

                # Assign the shader to the object
                cmds.select(created_object)
                cmds.hyperShade(assign=material_shader)





# ---------------------------------------------------------------------------
# Run the generator
# ---------------------------------------------------------------------------
generate_pattern()

# Frame everything in the viewport.
cmds.viewFit(allObjects=True)
print("Pattern generated successfully!")
