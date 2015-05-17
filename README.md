# fungusfun
Fungus Fun 2.0: Networked.

## Directory Structure
Client-only code goes in fungusfun/client
Server-only code goes in fungusfun/server
Shared code (game engine, map structure, etc.) goes in fungusfun/game
The startup scripts for the server and client go in the root directory. This makes the imports work.

## Branching
**master** is for stable releases.
**dev** is for general dev work. Small changes can be done directly on **dev**.
For larger features or fixes, make branches off of **dev**. Use underscores for branch names.