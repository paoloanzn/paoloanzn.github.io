# AI Can’t Code But You Can Code With AI

The claim that “AI can’t code” is, at its surface, empirically defensible. A growing population of users-many of whom possess little or no formal training in computer science-routinely produce code with AI assistance that appears to work, yet fails under scrutiny. The failures are not marginal; they are structural. Types are wrong, invariants are violated, edge cases are unhandled, and the architectural assumptions embedded in the generated code are frequently contradictory across modules. This is the phenomenon most critics observe, and it is real.

But the claim becomes false when generalized. Producing correct, maintainable code with AI is not only possible-it is, under the right conditions, reliable. The determining factor is not the model, nor the prompt, nor the tooling layer. It is the **level of abstraction at which the human operator directs the system.**

To make this precise, we can decompose the act of programming into three distinct layers of abstraction. These are not arbitrary categories; they correspond to genuinely different cognitive activities, each with its own requirements, failure modes, and relationship to correctness.

## The Three Layers of Programming Abstraction

### Layer 1 - Business Requirements

The topmost layer concerns the *what*: what the system must do for its users, what problem it solves, what constraints it operates under, and what outcomes define success. This is the domain of product thinking, stakeholder negotiation, and domain modeling at the level of human intent. It is essential, but it is not programming in any technical sense. A clear specification at this layer answers questions like “the system must allow users to submit a claim and receive a resolution within 48 hours,” but it says nothing about data structures, control flow, or invariants.

### Layer 2 - Data Structures Design and Data Modeling

The middle layer concerns the *how* at the level of structure: how the domain is represented as data, how entities relate to one another, what invariants must hold, what state transitions are legal, and what the boundaries of the system are. This is the layer of schema design, type systems, state machines, and the deliberate construction of abstractions that make correctness *provable* or at least *checkable*. It is the layer where a skilled engineer decides that a given operation must be atomic, that a given field must be non-nullable, that a given relationship is one-to-many and not many-to-many, and that a given state transition requires a guard condition.

### Layer 3 - Direct Implementation

The bottom layer concerns the *how* at the level of code: the concrete instructions, function bodies, loops, conditionals, and API calls that realize the design. This is the layer most people associate with “programming,” and it is precisely the layer at which contemporary AI models are most capable-and most dangerous. A model can write a function that sorts a list, parses a JSON payload, or constructs an HTTP request with high reliability. But a function is not a system, and a collection of individually plausible functions does not constitute a coherent program.

## The Core Argument

The central thesis of this article is straightforward: **the correct locus of human control in AI-assisted programming is Layer 2.**

When the human operator remains at Layer 1-describing business requirements in natural language and expecting the AI to infer both the data model and the implementation-the result is the familiar catastrophe of “partially working” code. The model is forced to make architectural decisions it is not equipped to make reliably, because those decisions depend on domain knowledge, constraint analysis, and invariant reasoning that are either not present in the prompt or not recoverable from it. The output looks plausible because each individual component is syntactically valid and locally reasonable, but the system as a whole is incoherent. In the domain of software, there is no such thing as “partially correct” code. A program that crashes on one input is not ninety percent correct; it is broken. Correctness is a binary property, not a gradient, because the semantics of computation do not accommodate approximation. A bridge that stands under most loads is not a bridge; it is a liability.

When the human operator descends to Layer 3-writing or reviewing every line of implementation-the AI becomes a glorified autocomplete. This is functional but wasteful. It ignores the model’s genuine capability at the implementation layer while forcing the human to spend cognitive energy on the very thing the model does well. It is the equivalent of a senior architect hand-pouring concrete.

**Layer 2 is the leverage point.** When the human operator defines the data model, the invariants, the type boundaries, and the state transitions-and then delegates the implementation of those constraints to the AI-the model operates within a space where correctness is *constrained by design*. Each generated function is checked not by the model’s judgment but by the structure the human has imposed: the type system rejects invalid operations, the schema rejects invalid data, the state machine rejects invalid transitions. The AI is no longer making architectural decisions; it is filling in the body of a skeleton whose shape is already determined.

This is not a new idea. It is the same principle that underlies type-driven design, design-by-contract, and the broader tradition of making incorrect states unrepresentable. What is new is that the availability of capable code-generating models makes this discipline not merely virtuous but *necessary*. In a world where implementation is cheap, the scarce resource is structure. The engineer who can define a correct data model is now the bottleneck, not the engineer who can write a correct loop.

## Why Layer 1 Fails in Practice

The failure mode of Layer 1 is not stochastic; it is systematic. A model given only business requirements must, by necessity, invent the data model. It does so by drawing on statistical patterns from its training data, which means it produces the *most common* model for a given domain description, not the *correct* model for the specific system being built. Common is not correct. The most common data model for a “user with a subscription” might use a boolean flag for active status, where the actual system requires a state machine with billing, grace period, suspension, and cancellation states. The model will not discover this distinction from a requirements document, because the distinction is not present in the requirements-it is present in the engineer’s knowledge of the domain’s failure modes.

Furthermore, the invariants that hold at Layer 2 are frequently *invisible* at Layer 1. A requirement that says “users can transfer funds between accounts” does not specify that transfers must be atomic, that the source account must have sufficient balance at the moment of debit (not at the moment of submission), and that the transfer must be idempotent to survive network failures. These are not implementation details; they are structural constraints that determine whether the system is correct. They belong to Layer 2, and omitting them from the AI’s instructions is equivalent to omitting them from the design entirely.

## Why Layer 3 Is Insufficient

The argument for operating at Layer 3 rather than Layer 2 is sometimes framed as a matter of trust: the operator does not trust the model to implement correctly, so they retain control over implementation. But this conflates two different kinds of control. Controlling the implementation means controlling *how* a constraint is satisfied; controlling the data model means controlling *what* the constraints are. The former is labor; the latter is judgment. A skilled engineer who insists on writing every function body is exercising labor that the model can perform, while leaving the judgment-the part that actually determines correctness-either to the model’s implicit inference or to an ad hoc, undocumented process that lives only in the engineer’s head.

The result is code that is locally correct but globally unprincipled. Each function works, but the system has no coherent data model, no documented invariants, and no structure that a second engineer (or a second AI session) can build upon without re-deriving the entire design from the implementation. This is the opposite of what good engineering produces. Good engineering produces systems where the structure is explicit, the invariants are visible, and the implementation is the least interesting part.

## The Discipline of Layer 2

Operating effectively at Layer 2 requires a specific discipline. It requires the engineer to think not in terms of functions or features but in terms of **types, invariants, and state spaces**. Before any code is written-or before any prompt is given to the model-the following questions must be answered:

1. **What are the entities in this system, and what are their relationships?** Not “what tables do I need,” but what are the real-world objects the system models, and how do they relate? A user has one account or many? A subscription belongs to one plan or can span multiple? Is an order always tied to a customer, or can it exist independently?
1. **What are the invariants that must hold at all times?** An account balance must never be negative. A subscription that is cancelled must not be billed. A transfer that is pending must eventually resolve to either completed or failed-never both, never neither. These invariants are not features; they are laws.
1. **What are the legal state transitions?** An order can go from pending to paid, but not from paid to pending. A subscription can go from active to suspended, but not from cancelled to active without an explicit reactivation. These transitions define the boundaries of correct behavior.
1. **What are the boundaries of the system?** What data is owned by this service, and what is borrowed? What operations are synchronous, and what are asynchronous? Where does the system’s responsibility end?
When these questions are answered, the AI’s role becomes tractable. The model is no longer asked to *design* the system; it is asked to *implement* a design that is already specified. The type system becomes the specification language, and the compiler (or runtime, or test suite) becomes the verification mechanism. The model’s output is checked not against the engineer’s intuition but against the structure the engineer has built.

This is the meaning of “AI can’t code, but you can code with AI.” The model cannot make the decisions that matter. It can make the decisions that don’t. The engineer who understands which are which-and who places the boundary between them at Layer 2-will produce correct software with AI assistance at a speed and scale that manual implementation cannot match. The engineer who does not will produce broken software at a speed and scale that manual debugging cannot rescue.
