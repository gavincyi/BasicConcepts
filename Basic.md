# Basic Concepts

- 8 bits = 1 bytes; int32_t = 4 bytes; char = 1 byte

- word = 2 bytes, upon the system

- A pointer points into a place in memory, so it would be 32 bits on a 32-bit system, and 64 bits in 64-bit system.

#### What is data segment?

A data segment (often denoted .data) is a portion of an object file or the corresponding virtual address space of 
a program that contains initialized static variables, that is, global variables and static local variables.

- Text (Code segment): Executable instruction and read-only

- Data (Initialized data/.data): Any global or static variables which have a pre-defined value and can be modified.

- BSS (Uninitialized data): All global variables and static variables that are initialized to zero or do not have 
explicit initialization in source code.

- Heap: Shared by all threads, shared libraries, and dynamically loaded modules in a process. Managed by malloc, 
calloc, realloc, and free

- Stack: Located in the higher parts of the memory. A "stack pointer" register tracks the top of the stack.

[Reference](https://en.wikipedia.org/wiki/Data_segment)

![StackHeap](https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Program_memory_layout.pdf/page1-299px-Program_memory_layout.pdf.jpg)

