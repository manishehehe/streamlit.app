"""Builds question_bank.json for the DSC401-6 AI Quiz Game (Units I & II).

Every search/state-space answer was computed by verify_search.py, not by hand.
Run:  python build_bank.py
"""
import json

AR_OPTIONS = [
    "Both A and R are true, and R is the correct explanation of A",
    "Both A and R are true, but R is NOT the correct explanation of A",
    "A is true, but R is false",
    "A is false, but R is true",
]
AR_A, AR_B, AR_C, AR_D = AR_OPTIONS
TF = ["True", "False"]

# Shared search graph (used by several problem-solving questions)
GRAPH_TEXT = (
    "Graph: S→A(2), S→B(3), A→C(4), A→D(3), B→D(2), B→E(6), C→G(3), "
    "D→G(5), E→G(1).  Heuristic h: S=7, A=5, B=4, C=2, D=4, E=1, G=0.  "
    "Start = S, Goal = G. Ties / children are taken in alphabetical order."
)

Q = []


def add(topic, qtype, diff, question, answer, explanation, hint,
        options=None, pairs=None, accept=None, real_world=False,
        search=False, figure=None):
    Q.append(dict(
        id=f"Q{len(Q) + 1:02d}", topic=topic, type=qtype, difficulty=diff,
        question=question, options=options, pairs=pairs, answer=answer,
        accept=accept, explanation=explanation, hint=hint,
        real_world=real_world, search=search, figure=figure,
    ))


# ---------------------------------------------------------------- Foundations
add("Foundations of AI", "MCQ", "Easy",
    "A chatbot is engineered with one goal: to be indistinguishable from a human "
    "in conversation. Which of Russell & Norvig's four approaches to AI does "
    "this design follow?",
    "Acting humanly",
    "Building a system to pass as human in behaviour is the 'acting humanly' "
    "(Turing Test) approach. 'Acting rationally' would instead optimise for "
    "the best outcome, even if no human would act that way.",
    "Think about what the Turing Test measures: thought or behaviour? "
    "Human-likeness or optimality?",
    options=["Thinking humanly", "Acting humanly", "Thinking rationally",
             "Acting rationally"])

add("Foundations of AI", "Assertion-Reason", "Medium",
    "Assertion (A): The 'laws of thought' (thinking rationally) approach is "
    "hard to apply directly to real-world problems.\n\nReason (R): Informal, "
    "uncertain knowledge is difficult to express in formal logic, and solving "
    "a problem 'in principle' differs greatly from solving it in practice.",
    AR_A,
    "Both statements are true and R is precisely why the logicist tradition "
    "struggles: uncertainty doesn't fit neatly into logic, and even "
    "well-posed logical problems can exhaust computational resources.",
    "Does R explain *why* A happens?",
    options=AR_OPTIONS)

add("Foundations of AI", "Fill in the Blank", "Easy",
    "The term 'Artificial Intelligence' was coined at the ________ workshop "
    "in 1956, organised by John McCarthy.",
    "Dartmouth", accept=["dartmouth", "dartmouth conference",
                         "dartmouth workshop", "dartmouth college"],
    explanation="The 1956 Dartmouth Summer Research Project (McCarthy, Minsky, "
    "Rochester, Shannon) is considered the birth of AI as a field.",
    hint="An Ivy League college in New Hampshire, USA.")

add("Foundations of AI", "True/False", "Medium",
    "Under the 'thinking humanly' (cognitive modelling) approach, a program "
    "is validated only by whether it produces the correct output.",
    "False",
    "Cognitive modelling requires the program's *reasoning steps* to match "
    "human ones (validated against psychological experiments or brain "
    "imaging). Correct output alone is the standard of acting/thinking "
    "rationally.",
    "Cognitive science cares about the *process*, not just the answer.",
    options=TF)

# ---------------------------------------------------------------- Applications
add("Applications of AI", "Scenario-based", "Easy",
    "A hospital deploys a model that reads chest X-rays and flags likely "
    "pneumonia; a radiologist confirms every flagged case. Which statement "
    "best describes this system?",
    "Narrow (weak) AI used as human-in-the-loop decision support",
    "It solves one specific task, has no general intelligence, and a human "
    "makes the final decision — classic narrow AI in a decision-support role.",
    "Can the same model also drive a car or write an essay?",
    options=["Artificial General Intelligence (AGI)",
             "Narrow (weak) AI used as human-in-the-loop decision support",
             "A fully autonomous agent with no human oversight",
             "A production system with no learning component"],
    real_world=True)

add("Applications of AI", "Match the Following", "Easy",
    "Match each real-world application with the AI area it mainly relies on.",
    None,
    "Route planning is search/planning; spam filtering is supervised "
    "classification (ML); voice assistants depend on speech & NLP; lane "
    "detection is computer vision.",
    "Ask: is the input text, images, audio, or a map/graph?",
    pairs={"Google Maps route planning": "Search & planning",
           "Gmail spam filter": "Machine learning (classification)",
           "Alexa understanding a spoken request": "Speech & natural language processing",
           "Self-driving car detecting lane markings": "Computer vision"},
    real_world=True)

add("Applications of AI", "Scenario-based", "Medium",
    "A UPI fraud-detection agent is evaluated only on accuracy. Just 0.1% of "
    "transactions are fraudulent. What is the main flaw in this performance "
    "measure?",
    "An agent that labels every transaction 'legitimate' scores 99.9% "
    "accuracy while catching zero fraud",
    "With heavy class imbalance, accuracy rewards doing nothing. A good "
    "performance measure should reflect what we actually want: e.g. recall on "
    "fraud and the real cost of a missed fraud vs a blocked genuine payment.",
    "What would a 'lazy' agent that never flags anything score?",
    options=["Accuracy cannot be computed for real-time systems",
             "An agent that labels every transaction 'legitimate' scores 99.9% "
             "accuracy while catching zero fraud",
             "Accuracy over-penalises false positives",
             "Nothing — accuracy is the ideal measure here"],
    real_world=True)

# ---------------------------------------------------------------- Turing Test
add("Turing Test", "MCQ", "Easy",
    "Why does the standard Turing Test have the interrogator communicate only "
    "through a text (teletype) channel?",
    "So that physical appearance or voice cannot reveal which is the machine",
    "Turing deliberately avoided direct physical interaction because physical "
    "simulation of a person is unnecessary for intelligence.",
    "What would give the machine away instantly if the judge could see it?",
    options=["To make the test faster to run",
             "So that physical appearance or voice cannot reveal which is the machine",
             "Because 1950s computers could not process speech",
             "To test the machine's typing speed"])

add("Turing Test", "Assertion-Reason", "Hard",
    "Assertion (A): A machine that passes the Turing Test has been proven to "
    "genuinely understand language.\n\nReason (R): Searle's Chinese Room "
    "argument claims that manipulating symbols by rules is not sufficient "
    "for understanding.",
    AR_D,
    "A is false — the Turing Test is a behavioural test; passing it shows "
    "indistinguishable behaviour, not proven understanding. R is a true "
    "description of Searle's argument (which is exactly an objection to A).",
    "Is the Turing Test about behaviour or about inner understanding?",
    options=AR_OPTIONS)

add("Turing Test", "True/False", "Medium",
    "The 'Total Turing Test' additionally requires the machine to have "
    "computer vision and robotics capabilities.",
    "True",
    "The Total Turing Test includes a video signal (perception → computer "
    "vision) and the ability to pass physical objects (manipulation → "
    "robotics), on top of NLP, knowledge representation, reasoning and "
    "learning.",
    "The word 'Total' adds perception and physical interaction.",
    options=TF)

add("Turing Test", "Scenario-based", "Medium",
    "When you log in to IRCTC you must solve a CAPTCHA. Why is CAPTCHA often "
    "called a 'reverse Turing Test'?",
    "A computer acts as the judge, deciding whether the user is a human",
    "In the Turing Test a human judges whether the other party is a machine. "
    "In CAPTCHA, the roles are reversed: a machine judges whether you are human.",
    "Who plays the interrogator in a CAPTCHA?",
    options=["A human judges whether the website is a bot",
             "A computer acts as the judge, deciding whether the user is a human",
             "It is solved in reverse order of the Turing Test questions",
             "It tests whether a machine can create images"],
    real_world=True)

# ---------------------------------------------------------------- Rational agents
add("Rational Agents", "MCQ", "Medium",
    "Which statement correctly defines a rational agent?",
    "It selects the action expected to maximise its performance measure, "
    "given its percept sequence and built-in knowledge",
    "Rationality is about *expected* performance given what the agent has "
    "perceived and knows — not about perfect outcomes.",
    "Key words: expected, performance measure, percept sequence.",
    options=["It always achieves the best possible actual outcome",
             "It selects the action expected to maximise its performance "
             "measure, given its percept sequence and built-in knowledge",
             "It thinks the same way a human expert would",
             "It never takes an action that leads to failure"])

add("Rational Agents", "True/False", "Easy",
    "A rational agent must be omniscient, i.e. it must know the actual "
    "outcome of its actions in advance.",
    "False",
    "Rationality ≠ omniscience. Rationality maximises *expected* "
    "performance; an agent crossing a road can be rational and still be hit "
    "by a falling aircraft door it could not have perceived.",
    "Can you be rational without knowing the future?",
    options=TF)

add("Rational Agents", "Fill in the Blank", "Medium",
    "An agent that relies on its designer's prior knowledge rather than on "
    "its own percepts and learning is said to lack ________.",
    "autonomy", accept=["autonomy", "autonomous"],
    explanation="A rational agent should be autonomous — it should learn what "
    "it can to compensate for partial or incorrect prior knowledge.",
    hint="The opposite of being dependent / pre-programmed.")

# ---------------------------------------------------------------- Good behaviour
add("Good Behaviour", "Scenario-based", "Medium",
    "A vacuum-cleaner agent is rewarded +1 for every 'Suck' action it "
    "performs. What is the most likely unintended behaviour?",
    "It cleans, dumps the dirt back, and cleans again forever",
    "Rewarding the action rather than the outcome invites gaming. Russell & "
    "Norvig's rule: design performance measures according to what you want "
    "in the environment (e.g. +1 per clean square per time step), not "
    "according to how you think the agent should behave.",
    "What maximises 'number of Suck actions'?",
    options=["It stops once all squares are clean",
             "It cleans, dumps the dirt back, and cleans again forever",
             "It refuses to move",
             "It becomes an omniscient agent"])

add("Good Behaviour", "Assertion-Reason", "Medium",
    "Assertion (A): A rational agent should look both ways before crossing a "
    "road, even though looking takes time.\n\nReason (R): Rationality "
    "maximises expected performance, and gathering information can raise "
    "the expected value of later actions.",
    AR_A,
    "Information gathering (exploration) is part of rational behaviour "
    "precisely because it improves expected outcomes — R explains A.",
    "Why is 'looking' worth its cost?",
    options=AR_OPTIONS)

# ---------------------------------------------------------------- Intelligent agents
add("Intelligent Agents", "Match the Following", "Medium",
    "Match each agent type with the example that best fits it.",
    None,
    "A thermostat maps percept → action directly (simple reflex). Tracking a "
    "car you can no longer see needs an internal model of the world. "
    "Navigation to a destination is goal-based. Trading off time, fare and "
    "comfort requires a utility function.",
    "Ask what extra thing each agent keeps: nothing, a world model, a goal, "
    "or a preference score?",
    pairs={"Simple reflex agent": "Thermostat switching heater on below 20°C",
           "Model-based reflex agent": "Driver tracking a car now in the blind spot",
           "Goal-based agent": "Robot planning a path to reach the charging dock",
           "Utility-based agent": "Ride app choosing the route balancing time, fare & comfort"})

add("Intelligent Agents", "Scenario-based", "Easy",
    "A smart traffic signal switches to green for the lane whose current "
    "queue sensor reading is longest, using only IF-THEN rules on the present "
    "reading. What type of agent is it?",
    "Simple reflex agent",
    "It acts on the current percept only via condition-action rules — no "
    "memory of past queues, no explicit goal or utility.",
    "Does it remember anything from the previous cycle?",
    options=["Simple reflex agent", "Model-based reflex agent",
             "Goal-based agent", "Learning agent"],
    real_world=True)

add("Intelligent Agents", "MCQ", "Medium",
    "In a learning agent, which component suggests exploratory actions that "
    "may lead to new and informative experiences?",
    "Problem generator",
    "Performance element chooses actions; critic gives feedback against a "
    "performance standard; learning element improves the performance "
    "element; problem generator proposes exploratory actions.",
    "It 'generates' new situations to learn from.",
    options=["Performance element", "Critic", "Learning element",
             "Problem generator"])

add("Intelligent Agents", "Assertion-Reason", "Easy",
    "Assertion (A): Simple reflex agents work reliably only in fully "
    "observable environments.\n\nReason (R): They select actions based only "
    "on the current percept and ignore percept history.",
    AR_A,
    "Because they have no memory, anything not visible in the current percept "
    "is lost — so they fail (e.g. loop forever) under partial observability.",
    "If the agent can't see everything now and remembers nothing...",
    options=AR_OPTIONS)

# ---------------------------------------------------------------- Agents & environments
add("Agents and Environments", "Fill in the Blank", "Easy",
    "Mathematically, an agent function maps any given percept ________ to "
    "an action.",
    "sequence", accept=["sequence", "percept sequence", "history",
                        "percept history"],
    explanation="The agent function f: P* → A takes the complete history of "
    "everything the agent has perceived.",
    hint="Not just the current percept — the whole ...")

add("Agents and Environments", "True/False", "Medium",
    "The agent function and the agent program are the same thing.",
    "False",
    "The agent function is an abstract mathematical mapping; the agent "
    "program is its concrete implementation running on a physical "
    "architecture. Agent = architecture + program.",
    "One is a mathematical description; the other is code.",
    options=TF)

add("Agents and Environments", "MCQ", "Easy",
    "Which equation describes an agent according to Russell & Norvig?",
    "Agent = Architecture + Program",
    "The architecture is the computing device with sensors and actuators; "
    "the program implements the agent function on it.",
    "Hardware + software.",
    options=["Agent = Sensors + Goals", "Agent = Architecture + Program",
             "Agent = Environment + Percepts", "Agent = Knowledge + Search"])

# ---------------------------------------------------------------- Nature of environments
add("Nature of Environments", "Match the Following", "Hard",
    "Match each task environment with the property that best distinguishes it.",
    None,
    "Crossword: deterministic and static. Poker: hidden cards and an "
    "opponent → partially observable, multi-agent. Taxi driving: world "
    "changes while you think and positions/speeds are continuous. Defect "
    "inspection on an assembly line: each image is judged independently → "
    "episodic.",
    "Which one has hidden information? Which one keeps moving while you "
    "decide? Which one treats every item independently?",
    pairs={"Crossword puzzle": "Deterministic and static",
           "Poker": "Partially observable, multi-agent",
           "Taxi driving": "Dynamic and continuous",
           "Inspecting parts on a conveyor belt": "Episodic"})

add("Nature of Environments", "Scenario-based", "Easy",
    "PEAS for a food-delivery routing agent (Swiggy/Zomato). Which of these "
    "is a SENSOR?",
    "Live GPS location of the rider",
    "GPS feed is a percept source (sensor). Sending the route to the rider "
    "app is an actuator, minimising delivery time is the performance "
    "measure, and roads/traffic are the environment.",
    "Sensors bring information *in* to the agent.",
    options=["Live GPS location of the rider",
             "Pushing the route to the rider's app",
             "Minimising average delivery time",
             "City roads and traffic"],
    real_world=True)

add("Nature of Environments", "MCQ", "Medium",
    "Chess played with a clock is best classified as:",
    "Semi-dynamic",
    "The board doesn't change while you think, but your performance score "
    "(remaining time) does — that is semi-dynamic.",
    "The board waits for you; the clock doesn't.",
    options=["Static", "Dynamic", "Semi-dynamic", "Continuous"])

add("Nature of Environments", "True/False", "Easy",
    "A medical-diagnosis agent operates in a partially observable and "
    "stochastic environment.",
    "True",
    "The patient's internal state can't be observed directly (partially "
    "observable) and disease progression / treatment response are uncertain "
    "(stochastic).",
    "Can a doctor see the disease directly? Is the outcome of a treatment "
    "certain?",
    options=TF)

# ---------------------------------------------------------------- Problems & problem spaces
add("Problems and Problem Spaces", "MCQ", "Easy",
    "Which of the following is NOT part of a formal problem definition for "
    "search?",
    "Heuristic function",
    "A problem is defined by initial state, actions, transition model, goal "
    "test and path cost. A heuristic belongs to a particular search "
    "strategy, not to the problem itself.",
    "Uninformed search solves the problem without this component.",
    options=["Initial state", "Goal test", "Path cost", "Heuristic function"])

add("Problems and Problem Spaces", "Problem-solving", "Hard",
    "Water-jug problem: a 4-litre jug and a 3-litre jug, both empty, with an "
    "unlimited tap. Operators: fill a jug, empty a jug, pour one into the "
    "other until one is full/empty. What is the MINIMUM number of operations "
    "to get exactly 2 litres in the 4-litre jug?",
    "6", accept=["6", "six"],
    explanation="BFS over states (x, y) gives a shortest path of 6: "
    "(0,0)→(4,0)→(1,3)→(1,0)→(0,1)→(4,1)→(2,3). (A different 6-step route "
    "via filling the 3-litre jug first also exists.)",
    hint="Start by filling the 4-litre jug and pouring into the 3-litre one.",
    search=True)

add("Problems and Problem Spaces", "Fill in the Blank", "Easy",
    "The set of all states reachable from the initial state by any sequence "
    "of actions is called the ________.",
    "state space", accept=["state space", "statespace", "problem space",
                           "search space"],
    explanation="The state space forms a directed graph whose nodes are "
    "states and whose edges are actions.",
    hint="Two words: '_____ space'.")

# ---------------------------------------------------------------- State space search
add("State Space Search", "Problem-solving", "Medium",
    "How many distinct states of the 8-puzzle are reachable from any given "
    "start configuration?",
    "181,440",
    "There are 9! = 362,880 arrangements, but they split into two disjoint "
    "halves by parity; only 9!/2 = 181,440 are reachable from any start.",
    "Start from 9!, then remember half the configurations are unsolvable.",
    options=["362,880", "181,440", "40,320", "9"],
    search=True)

add("State Space Search", "Problem-solving", "Medium",
    "Missionaries & Cannibals: state = (M, C, B) on the LEFT bank, start "
    "(3, 3, 1). Missionaries must never be outnumbered on either bank where "
    "missionaries are present. Which state is INVALID?",
    "(1, 2, 1)",
    "(1, 2, 1): the left bank has 1 missionary and 2 cannibals → missionary "
    "is outnumbered. The others are safe on both banks, e.g. (0,3,0) leaves "
    "no missionary on the left and 3 M vs 0 C on the right.",
    "Check both banks: right bank = (3 − M, 3 − C).",
    options=["(3, 1, 0)", "(2, 2, 1)", "(1, 2, 1)", "(0, 3, 0)"],
    search=True)

add("State Space Search", "True/False", "Easy",
    "Tree search on a state space containing cycles can loop forever unless "
    "repeated states are detected.",
    "True",
    "Without an explored set (graph search) or cycle check, a path like "
    "A→B→A→B… can be generated indefinitely.",
    "Think of the 8-puzzle: moving a tile left then right.",
    options=TF)

# ---------------------------------------------------------------- Production systems
add("Production Systems", "MCQ", "Easy",
    "In a production system, when several rules match the current working "
    "memory, which component decides which one fires?",
    "Control strategy (conflict resolution)",
    "A production system = set of rules + database/working memory + control "
    "strategy + rule applier. The control strategy resolves conflicts.",
    "It's the 'strategy' part.",
    options=["The rule base", "Working memory",
             "Control strategy (conflict resolution)", "The goal test"])

add("Production Systems", "Match the Following", "Hard",
    "Match each problem with its production-system class (Rich & Knight).",
    None,
    "Theorem proving: monotonic & partially commutative. Robot navigation: "
    "non-monotonic but partially commutative. Chemical synthesis: monotonic "
    "but not partially commutative (order of reactions matters). Bridge "
    "(card game): non-monotonic and not partially commutative.",
    "Can an action be undone (monotonic?) and does the order of actions "
    "matter (partially commutative?)",
    pairs={"Theorem proving": "Monotonic, partially commutative",
           "Robot navigation": "Non-monotonic, partially commutative",
           "Chemical synthesis": "Monotonic, not partially commutative",
           "Playing bridge": "Non-monotonic, not partially commutative"})

add("Production Systems", "Assertion-Reason", "Medium",
    "Assertion (A): A good control strategy for a production system must "
    "cause motion.\n\nReason (R): A strategy that, for example, always fires "
    "the first applicable rule may keep producing the same state and never "
    "reach a solution.",
    AR_A,
    "Rich & Knight's two requirements: the control strategy must cause "
    "motion, and it must be systematic. R illustrates exactly why motion is "
    "required.",
    "Example: water jug — always 'fill the 4-litre jug'.",
    options=AR_OPTIONS)

# ---------------------------------------------------------------- Problem characteristics
add("Problem Characteristics", "Match the Following", "Medium",
    "Match each problem with how its solution steps can be treated.",
    None,
    "Theorem proving: a useless lemma can simply be ignored. 8-puzzle: a "
    "wrong move can be undone (recoverable). Chess: a move once made cannot "
    "be taken back (irrecoverable).",
    "Can a bad step be ignored, undone, or neither?",
    pairs={"Theorem proving": "Ignorable",
           "8-puzzle": "Recoverable",
           "Chess": "Irrecoverable"})

add("Problem Characteristics", "MCQ", "Medium",
    "Which of the following problems is DECOMPOSABLE into independent "
    "sub-problems?",
    "Symbolic integration of ∫(x² + 3x + sin²x·cos²x) dx",
    "The integral splits into three independent integrals solved separately "
    "and summed. In the blocks world, sub-goals interact, so it is not "
    "simply decomposable.",
    "Which one splits into pieces that don't affect each other?",
    options=["Symbolic integration of ∫(x² + 3x + sin²x·cos²x) dx",
             "Blocks-world stacking with interacting sub-goals",
             "Playing a game of chess", "Solving the 8-puzzle"])

add("Problem Characteristics", "True/False", "Medium",
    "The Travelling Salesman Problem is an 'any-path' problem: any tour that "
    "visits every city is an acceptable solution.",
    "False",
    "TSP is a 'best-path' problem — we need the shortest tour, so a good "
    "solution is relative, not absolute. Any-path search is not enough.",
    "Is any tour good enough, or do we want the cheapest?",
    options=TF)

add("Problem Characteristics", "Scenario-based", "Hard",
    "A banking chatbot must interpret the query 'Block the card I used at "
    "the mall yesterday'. In Rich & Knight's terms, what is the solution to "
    "this problem?",
    "A state — the correct interpretation — not the reasoning path used",
    "Natural-language interpretation is a 'solution is a state' problem: "
    "what matters is the final interpretation, not the record of how it was "
    "reached (unlike, say, the water-jug problem where the path is the "
    "answer).",
    "Does the user care *how* the bot understood the sentence?",
    options=["A path — the sequence of reasoning steps",
             "A state — the correct interpretation — not the reasoning path used",
             "Both — the path must be shown to the user",
             "Neither — it is a decomposable problem"],
    real_world=True)

# ---------------------------------------------------------------- Issues in search design
add("Issues in Search Program Design", "MCQ", "Hard",
    "When is backward search (from goal to start) generally preferable to "
    "forward search?",
    "When there are fewer goal states than start states and the backward "
    "branching factor is smaller",
    "The direction choice depends on the relative number of start vs goal "
    "states and the branching factor in each direction (e.g. theorem proving "
    "or diagnosis often reason backward).",
    "Which direction fans out less?",
    options=["Always — backward search is optimal",
             "When there are fewer goal states than start states and the "
             "backward branching factor is smaller",
             "When the goal state is unknown",
             "Only when the state space is infinite"])

add("Issues in Search Program Design", "True/False", "Medium",
    "Using graph search instead of tree search avoids re-expanding repeated "
    "states, at the cost of extra memory for the explored set.",
    "True",
    "Representing the space as a graph (with a closed/explored list) trades "
    "memory for not duplicating work — one of the design issues Rich & "
    "Knight list (tree vs graph).",
    "What must be stored to know a state was already seen?",
    options=TF)

# ---------------------------------------------------------------- BFS
add("Breadth-First Search", "Problem-solving", "Medium",
    GRAPH_TEXT + "\n\nIgnoring costs, in what order does BFS EXPAND nodes "
    "until it expands G (goal test on expansion, repeated states skipped)?",
    "S, A, B, C, D, E, G",
    "Level 0: S. Level 1: A, B. Level 2: C, D (from A), E (from B; D already "
    "queued). Level 3: G. BFS returns S→A→C→G.",
    "Expand level by level, left to right.",
    options=["S, A, C, G", "S, A, B, C, D, E, G", "S, B, E, G",
             "S, A, B, D, C, E, G"],
    search=True, figure="graph")

add("Breadth-First Search", "Assertion-Reason", "Medium",
    "Assertion (A): BFS is optimal when all step costs are equal.\n\nReason "
    "(R): BFS always expands the shallowest unexpanded node first.",
    AR_A,
    "Expanding shallowest first means the first goal found has the fewest "
    "steps; when every step costs the same, fewest steps = lowest cost.",
    "Fewest edges vs lowest cost — when are they the same?",
    options=AR_OPTIONS)

add("Breadth-First Search", "Scenario-based", "Easy",
    "LinkedIn labels people as 1st, 2nd or 3rd-degree connections. Which "
    "search strategy naturally computes these degrees?",
    "Breadth-First Search",
    "BFS from your profile visits all people 1 hop away, then 2 hops, then "
    "3 — exactly the 'degree' of connection.",
    "Degrees are explored layer by layer.",
    options=["Depth-First Search", "Breadth-First Search",
             "Hill Climbing", "Greedy Best-First Search"],
    real_world=True)

add("Breadth-First Search", "MCQ", "Medium",
    "With branching factor b and shallowest goal at depth d, what is the "
    "space complexity of BFS?",
    "O(b^d)",
    "BFS must keep the whole frontier in memory, which is O(b^d) — memory, "
    "not time, is usually its real bottleneck.",
    "BFS stores every node of the deepest level it reaches.",
    options=["O(b·d)", "O(d)", "O(b^d)", "O(d^b)"])

# ---------------------------------------------------------------- DFS
add("Depth-First Search", "Problem-solving", "Easy",
    GRAPH_TEXT + "\n\nHow many nodes does DFS expand (including S and G) "
    "before reaching the goal?",
    "4",
    "DFS goes S → A → C → G, expanding 4 nodes, and returns S→A→C→G "
    "(cost 9). It got lucky here — on other graphs DFS can return a long, "
    "costly path.",
    "Always go to the alphabetically first child and keep going deeper.",
    options=["3", "4", "6", "7"],
    search=True, figure="graph")

add("Depth-First Search", "True/False", "Easy",
    "DFS is complete even on state spaces of infinite depth.",
    "False",
    "DFS can go down an infinite branch forever. It is complete only on "
    "finite spaces (with repeated-state checking).",
    "What happens if one branch never ends?",
    options=TF)

add("Depth-First Search", "Fill in the Blank", "Easy",
    "DFS stores its frontier in a ________ (LIFO) data structure.",
    "stack", accept=["stack", "lifo stack"],
    explanation="BFS uses a FIFO queue; DFS uses a LIFO stack (or recursion, "
    "which uses the call stack).",
    hint="Last in, first out.")

# ---------------------------------------------------------------- Iterative deepening
add("Iterative Deepening", "Problem-solving", "Hard",
    GRAPH_TEXT + "\n\nRun Iterative Deepening DFS with limits 0, 1, 2, … "
    "(no repeated-state checking; stop as soon as G is expanded). What is "
    "the TOTAL number of node expansions across all iterations?",
    "15",
    "Limit 0: S (1). Limit 1: S, A, B (3). Limit 2: S, A, C, D, B, D, E (7 — "
    "D appears twice, via A and via B). Limit 3: S, A, C, G (4). "
    "Total = 1 + 3 + 7 + 4 = 15.",
    "Count each iteration separately; D is reachable from both A and B.",
    options=["7", "12", "15", "19"],
    search=True, figure="graph")

add("Iterative Deepening", "Assertion-Reason", "Hard",
    "Assertion (A): Iterative deepening regenerates upper levels many times, "
    "yet its time overhead over BFS is small.\n\nReason (R): In a tree with "
    "a constant branching factor, most nodes lie at the deepest level.",
    AR_A,
    "Total generated ≈ d·b + (d−1)·b² + … + 1·b^d = O(b^d). Because the "
    "bottom level dominates, repeating the shallow levels adds only a "
    "small constant factor (~b/(b−1)).",
    "Compare b^d with the sum of all shallower levels.",
    options=AR_OPTIONS)

add("Iterative Deepening", "Scenario-based", "Medium",
    "Chess engines such as Stockfish use iterative deepening under a game "
    "clock. What is the main practical benefit?",
    "When time runs out, the engine can play the best move from the last "
    "fully completed depth",
    "Iterative deepening is an 'anytime' strategy: it always has an answer "
    "from the deepest finished iteration, and earlier iterations also give "
    "good move ordering for the next.",
    "What happens if the clock stops halfway through a search?",
    options=["It uses more memory than BFS so it is more accurate",
             "When time runs out, the engine can play the best move from the "
             "last fully completed depth",
             "It guarantees a checkmate is found",
             "It removes the need for an evaluation function"],
    real_world=True)

# ---------------------------------------------------------------- Hill climbing
add("Hill Climbing", "Problem-solving", "Medium",
    "Objective values along a 1-D landscape (index 0–9): "
    "[3, 5, 8, 6, 4, 7, 9, 12, 10, 2]. Neighbours are index ± 1. "
    "Steepest-ascent hill climbing (maximising) starts at index 0. "
    "What value does it stop at?",
    "8",
    "0 (3) → 1 (5) → 2 (8). Both neighbours of index 2 (5 and 6) are lower, "
    "so it halts at a LOCAL maximum of 8 — the global maximum 12 (index 7) "
    "is never reached.",
    "Move uphill only; stop when no neighbour is better.",
    options=["8", "9", "12", "10"],
    search=True, figure="landscape")

add("Hill Climbing", "Match the Following", "Medium",
    "Match each hill-climbing failure with the remedy suggested by Rich & Knight.",
    None,
    "Local maximum → backtrack to an earlier node and try another direction. "
    "Plateau → make a big jump to a new region. Ridge → apply two or more "
    "rules (move in several directions) before testing.",
    "Plateau = flat; ridge = narrow slope that single moves can't follow.",
    pairs={"Local maximum": "Backtrack and try a different direction",
           "Plateau": "Make a big jump to a new part of the space",
           "Ridge": "Apply two or more rules before testing"})

add("Hill Climbing", "MCQ", "Hard",
    "In simulated annealing a worse move (ΔE < 0) is accepted with "
    "probability e^(ΔE/T). As the temperature T → 0, the algorithm behaves "
    "like:",
    "Hill climbing (only uphill moves)",
    "As T → 0, e^(ΔE/T) → 0 for any ΔE < 0, so downhill moves are never "
    "accepted — it degenerates into (stochastic) hill climbing. At high T it "
    "behaves like a random walk.",
    "Evaluate e^(negative / tiny number).",
    options=["A random walk", "Hill climbing (only uphill moves)",
             "Breadth-first search", "A* search"])

add("Hill Climbing", "Scenario-based", "Medium",
    "A quick-commerce company uses hill climbing to choose a dark-store "
    "location that minimises average delivery distance. Different starting "
    "points give different final locations. What is the most practical fix?",
    "Random-restart hill climbing: run from many random starts and keep the best",
    "Different results from different starts = local optima. Random restarts "
    "explore several basins and keep the best one, approaching the global "
    "optimum with probability → 1 as restarts increase.",
    "The problem is the starting point, so change the starting point.",
    options=["Use a smaller step size only",
             "Random-restart hill climbing: run from many random starts and "
             "keep the best",
             "Switch to DFS",
             "Stop after the first improving move"],
    real_world=True)

# ---------------------------------------------------------------- Heuristic search
add("Heuristic Search", "Problem-solving", "Medium",
    "8-puzzle. Start:  2 8 3 / 1 6 4 / 7 _ 5.   Goal:  1 2 3 / 8 _ 4 / 7 6 5. "
    "h1 = number of misplaced tiles, h2 = sum of Manhattan distances (blank "
    "not counted). What are h1 and h2 for the start state?",
    "h1 = 4, h2 = 5",
    "Misplaced: 2, 8, 1, 6 → h1 = 4. Manhattan: 2→1, 8→2, 1→1, 6→1, others "
    "0 → h2 = 5. (The true optimal solution is 5 moves, so h2 is exact here.)",
    "Tiles 3, 4, 5 and 7 are already in place.",
    options=["h1 = 4, h2 = 5", "h1 = 5, h2 = 4", "h1 = 3, h2 = 5",
             "h1 = 4, h2 = 6"],
    search=True, figure="puzzle")

add("Heuristic Search", "Assertion-Reason", "Hard",
    "Assertion (A): For A* on the 8-puzzle, Manhattan distance (h2) is a "
    "better heuristic than misplaced tiles (h1).\n\nReason (R): Both are "
    "admissible, and h2(n) ≥ h1(n) for every state n (h2 dominates h1).",
    AR_A,
    "A dominating admissible heuristic is closer to the true cost, so A* "
    "with h2 never expands more nodes than with h1 (apart from ties).",
    "Bigger-but-still-admissible means...?",
    options=AR_OPTIONS)

add("Heuristic Search", "True/False", "Medium",
    "If a heuristic overestimates the true cost to the goal, A* may return a "
    "non-optimal solution.",
    "True",
    "Admissibility (never overestimating) is what guarantees A* (tree search) "
    "optimality. An overestimate can make the optimal path look worse than "
    "a sub-optimal one.",
    "What property is A*'s optimality proof based on?",
    options=TF)

# ---------------------------------------------------------------- Best-first search
add("Best First Search", "Problem-solving", "Medium",
    GRAPH_TEXT + "\n\nWhich path does GREEDY best-first search (f = h) "
    "return, and what is its cost?",
    "S → B → E → G, cost 10",
    "From S, B (h=4) beats A (h=5). From B, E (h=1) beats D (h=4). E → G. "
    "Path cost 3 + 6 + 1 = 10 — not optimal (S→A→C→G costs 9), showing "
    "greedy search ignores g(n).",
    "Always move to the child with the smallest h, ignoring edge costs.",
    options=["S → A → C → G, cost 9", "S → B → E → G, cost 10",
             "S → B → D → G, cost 10", "S → A → D → G, cost 10"],
    search=True, figure="graph")

add("Best First Search", "Problem-solving", "Hard",
    GRAPH_TEXT + "\n\nWhich path does A* search (f = g + h) return, and what "
    "is its cost?",
    "S → A → C → G, cost 9",
    "f(A)=2+5=7, f(B)=3+4=7; f(C)=6+2=8 is lowest next; G via C has "
    "f=9+0=9, while every alternative route to G costs 10. Since h is "
    "admissible (h ≤ true cost at every node), A* returns the optimal path "
    "S→A→C→G with cost 9.",
    "Compute f = g + h for every frontier node; also total each complete path.",
    options=["S → B → E → G, cost 10", "S → A → C → G, cost 9",
             "S → B → D → G, cost 10", "S → A → D → G, cost 10"],
    search=True, figure="graph")

add("Best First Search", "Fill in the Blank", "Easy",
    "In A* search, the evaluation function is f(n) = g(n) + ________.",
    "h(n)", accept=["h(n)", "h", "hn", "heuristic", "h of n",
                    "heuristic function"],
    explanation="g(n) = cost so far from the start; h(n) = estimated cost "
    "from n to the goal.",
    hint="The estimated cost-to-go.")

add("Best First Search", "Scenario-based", "Medium",
    "A navigation app runs A* using straight-line (as-the-crow-flies) "
    "distance to the destination as h(n). Why is this heuristic admissible?",
    "No road route can be shorter than the straight-line distance",
    "The straight line is the shortest possible distance between two "
    "points, so it never overestimates the true road distance — that is "
    "admissibility.",
    "Can driving ever beat a straight line?",
    options=["Because roads are always straight",
             "No road route can be shorter than the straight-line distance",
             "Because it is computed with GPS",
             "Because it always equals the road distance"],
    real_world=True)

# ---------------------------------------------------------------- CSP
add("Constraint Satisfaction Problems", "MCQ", "Medium",
    "Australia map colouring (WA, NT, SA, Q, NSW, V, T) with 3 colours. At "
    "the very start, with all domains equal, which variable does the DEGREE "
    "heuristic choose first?",
    "SA (South Australia)",
    "SA borders 5 regions (WA, NT, Q, NSW, V) — the most constraints on "
    "other unassigned variables. MRV can't break the tie at the start, so "
    "degree picks SA.",
    "Which region touches the most others?",
    options=["WA (Western Australia)", "SA (South Australia)",
             "T (Tasmania)", "NSW (New South Wales)"],
    figure="australia")

add("Constraint Satisfaction Problems", "Fill in the Blank", "Medium",
    "Crypt-arithmetic: SEND + MORE = MONEY, each letter a distinct digit and "
    "no leading zeros. The letter M must equal ________.",
    "1", accept=["1", "one"],
    explanation="Adding two 4-digit numbers gives at most 19,998, so the "
    "carry into the 5th digit (M) can only be 1. Full solution: "
    "9567 + 1085 = 10652.",
    hint="What is the largest possible carry out of adding two digits plus a carry?",
    search=True)

add("Constraint Satisfaction Problems", "Scenario-based", "Easy",
    "Christ University models end-semester exam timetabling as a CSP "
    "(variables = exams, domains = time slots). Which of the following is a "
    "CONSTRAINT?",
    "No student can have two exams in the same slot",
    "Variables are exams, domains are slots, and constraints restrict which "
    "combinations of assignments are allowed — e.g. exams sharing a student "
    "must get different slots.",
    "Constraints restrict combinations of assignments.",
    options=["Each exam is a variable",
             "The available time slots",
             "No student can have two exams in the same slot",
             "The list of courses offered"],
    real_world=True)

add("Constraint Satisfaction Problems", "Assertion-Reason", "Medium",
    "Assertion (A): Forward checking can detect a dead end earlier than plain "
    "backtracking.\n\nReason (R): After each assignment, forward checking "
    "deletes inconsistent values from the domains of unassigned neighbouring "
    "variables.",
    AR_A,
    "If any neighbour's domain becomes empty, forward checking backtracks "
    "immediately — before plain backtracking would have reached that variable.",
    "What happens when a neighbour's domain becomes empty?",
    options=AR_OPTIONS)

add("Constraint Satisfaction Problems", "True/False", "Easy",
    "The Minimum Remaining Values (MRV) heuristic selects the variable with "
    "the MOST legal values left.",
    "False",
    "MRV ('fail-first') picks the variable with the FEWEST legal values, so "
    "failures are found early and the tree is pruned.",
    "It's also called the 'fail-first' heuristic.",
    options=TF)

# ---------------------------------------------------------------- Means-end analysis
add("Means-End Analysis", "MCQ", "Easy",
    "Means-End Analysis was the central technique of which early AI system?",
    "General Problem Solver (GPS) by Newell & Simon",
    "GPS (Newell, Shaw & Simon, 1957–59) solved problems by repeatedly "
    "reducing the difference between the current and goal states.",
    "A 'general' solver from the late 1950s.",
    options=["ELIZA by Weizenbaum", "General Problem Solver (GPS) by Newell & Simon",
             "MYCIN by Shortliffe", "Deep Blue by IBM"])

add("Means-End Analysis", "Scenario-based", "Medium",
    "A warehouse robot must PUSH a desk to another room, but the desk has a "
    "lamp on it and PUSH requires the desk top to be clear. What does "
    "Means-End Analysis do next?",
    "Sets up a sub-goal to satisfy PUSH's precondition (remove the lamp), "
    "then resumes",
    "This is operator sub-goaling: when the chosen operator's preconditions "
    "aren't met, MEA recursively solves the problem of reaching a state "
    "where they are, then applies the operator and continues toward the goal.",
    "The operator is right; its precondition isn't satisfied yet.",
    options=["Abandons PUSH and picks a random operator",
             "Sets up a sub-goal to satisfy PUSH's precondition (remove the "
             "lamp), then resumes",
             "Restarts the search from the initial state",
             "Applies PUSH anyway and ignores the precondition"],
    real_world=True)

add("Means-End Analysis", "Assertion-Reason", "Hard",
    "Assertion (A): Means-End Analysis mixes forward and backward reasoning."
    "\n\nReason (R): It first reduces the most important difference with a "
    "chosen operator, then solves the sub-problems of reaching that "
    "operator's preconditions and of getting from its result to the goal.",
    AR_A,
    "Choosing an operator for the biggest difference and then working on "
    "its preconditions is backward-style; moving from the operator's result "
    "to the goal is forward-style. R describes exactly that mix.",
    "Which part works back from what's needed, and which part moves forward?",
    options=AR_OPTIONS)

add("Means-End Analysis", "MCQ", "Medium",
    "In Means-End Analysis, what does a 'difference table' record?",
    "Which operators can reduce each kind of difference between current and "
    "goal states",
    "The difference table indexes operators by the differences they reduce, "
    "so MEA can look up a relevant operator for the most important "
    "difference.",
    "It links 'what's wrong' to 'what can fix it'.",
    options=["The heuristic value of each state",
             "Which operators can reduce each kind of difference between "
             "current and goal states",
             "The cost of every path explored so far",
             "The order in which nodes were expanded"])


if __name__ == "__main__":
    # integrity checks
    for q in Q:
        if q["pairs"] is None and q["accept"] is None:
            assert q["answer"] in q["options"], q["id"]
        if q["type"] == "Assertion-Reason":
            assert q["options"] == AR_OPTIONS
    with open("question_bank.json", "w", encoding="utf-8") as f:
        json.dump(Q, f, ensure_ascii=False, indent=1)
    from collections import Counter
    print(len(Q), "questions")
    print(Counter(q["type"] for q in Q))
    print(Counter(q["difficulty"] for q in Q))
    print("real-world:", sum(q["real_world"] for q in Q),
          " search:", sum(q["search"] for q in Q))
    print("topics:", len({q["topic"] for q in Q}))
