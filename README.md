1. About this program:
    The `find_route` program is a Python script designed to find the shortest route between two cities using either uninformed or informed search strategies. For uninformed search, it implements Uniform Cost Search (UCS), and for informed search, it uses the A* algorithm with provided heuristic values.

2. Information about Programming language used and libraries:
    Python 3.x
    No external libraries are required as the script uses only the Python Standard Library.

3. Input files
    `input_filename`: A text file that describes the road connections between cities. 
                    Each line should contain a source city, a destination city, and the distance between them, separated by spaces. 
                    The file should end with "END OF INPUT".

    `heuristic_filename` (optional for informed search): A text file that provides heuristic values for the estimated distance from each city to the destination city. Each line should contain a city name and its heuristic value, separated by a space. The file should end with "END OF INPUT".

4. To run this program:

    Format for command line: python find_route.py [input_filename] origin_city destination_city [heuristic_filename]

    origin_city, destination_city : Give any city names

    For example:
    Command for Uninformed search: python find_route.py input1.txt Bremen Kassel
    Command for informed search: python find_route.py input1.txt Bremen Kassel h_kassel.txt

5. Output:
    The program will output the following information:
    - Nodes Popped: The total number of nodes taken out of the frontier for processing.
    - Nodes Expanded: The number of unique nodes that were expanded to generate new nodes.
    - Nodes Generated: The total number of nodes that were created and placed into the frontier.
    - Distance: The total distance of the found route; "infinity" if no route exists.
    - Route: A list of roads and distances comprising the route; "None" if no route exists.

If any issue occurs, please ensure that the input files are correctly formatted and in the same directory as this .readme file, or provide the absolute paths to them. 
If you encounter any errors regarding file paths or syntax, verify that Python is correctly installed and that the command is typed correctly.
