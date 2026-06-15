###  **The Mass & Energy Balance Solver**

**Chemistry anchor: Mass and Energy Balances**

Build a tool that solves steady-state mass and energy balances for a simple flowsheet: mixer \+ CSTR reactor \+ splitter with recycle. Define streams as unknowns, write balance equations as a matrix system, solve with linear algebra.

|  |  |
| :---- | :---- |
| **You provide** | The engineering: how to write balance equations, what species, what reactions, what the recycle does |
| **Noah provides** | Project setup: repo, venv, Git, matrix operations |
| **You both learn** | `numpy.linalg.solve`, translating engineering equations into Ax=b, pandas for stream tables |
| **Tech stack** | Python, numpy, pandas, matplotlib |
| **Deliverable** | CLI tool: define a flowsheet in a config file, get back a complete stream table with all flows and compositions |

**The exercise:** Three-stream mixer feeding a CSTR with 80% conversion. Product splits: 70% product, 30% recycle. Reaction: A \-\> B \+ C. Solve for all unknowns.

**Why it matters:** Mass balances are the skeleton of every process. Doing them programmatically means doing them faster, with fewer errors, and parameterized — change one input, all outputs update.