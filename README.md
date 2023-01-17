# RPS-Cell-Simulator
## Pseudocode
**Setup:**
- Create board class
- For each new object, assign an image (acts as the walls and background)
- Divide image into 3 sectors (for each cell type to be placed in)
- Make a cell class
Create n amount of objects (n should be divisible by 3)
- Assign each third into rock, paper or scissors
   - Keep track of their position
- Give players power-ups in their inventory
- 2 power-ups: 
   - Increase speed
   - Apex predator

**UI Loop:**
- Show “rock sector(s)”, then let “player rock” place their cells.
- After all rocks have been placed, 
     - Show “paper sector(s)”, then let “player paper” place their cells.
- After all papers have been placed, 
	   - Show “scissors sector(s)”, then let “player scissors” place their cells.
- After all scissors have been placed,
     - Countdown goes, while cells compute distances to other cells and store numbers into an array.
- If a cell is closer to a prey cell,
	   - Move towards their prey cell.
- Else if a cell is closer to a predator cell,
	   - Move away from their predator cell.
- Else,
	   - Move randomly in a jittery motion.
- If a predator cell touches a prey cell,
	   - The prey cell converts into the predator cell
- If cells of the same type are too close to each other,
     - Bounce off of each other to have an n distance between each other and continue to follow previous motion rules,
- If player(s) use increase speed,
	   - Detect which player used it and increase the speed of all their cells by n.
- If player(s) use “apex predator”,
	   - Detect which player used it and now all of their cells can now eat all cells.
- If 2 or more players use “apex predator”
     - “Apex predator” is no longer in effect and all players who use it, lose their ability to use “apex predator
- Randomly spawn debuffs on the map.
- If a cell picks up a decrease speed,
	   - Decrease speed of all cells of the type
- If a cell picks up a “prey” debuff
- It can no longer prey on any cell
- If a cell activates the “apex predator” buff while on the "prey" debuff
	- It cancels out and turns back to normal



