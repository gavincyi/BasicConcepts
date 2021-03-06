# Basic Concepts

- 8 bits = 1 bytes; int32_t = 4 bytes; char = 1 byte

- word = 2 bytes, upon the system

- A pointer points into a place in memory, so it would be 32 bits on a 32-bit system, and 64 bits in 64-bit system.

#### [Data segment](https://en.wikipedia.org/wiki/Data_segment)

A data segment (often denoted .data) is a portion of an object file or the corresponding virtual address space of 
a program that contains initialized static variables, that is, global variables and static local variables.

- Text (Code segment): Executable instruction and read-only

- Data (Initialized data/.data): Any global or static variables which have a pre-defined value and can be modified.

- BSS (Uninitialized data): All global variables and static variables that are initialized to zero or do not have 
explicit initialization in source code.

- Heap: Shared by all threads, shared libraries, and dynamically loaded modules in a process. Managed by malloc, 
calloc, realloc, and free

- Stack: LIFO. Located in the higher parts of the memory. A "stack pointer" register tracks the top of the stack.
For local data storage.

[Reference]

![StackHeap](https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Program_memory_layout.pdf/page1-299px-Program_memory_layout.pdf.jpg)

#### Process v.s. Thread

- Both processes and threads are independent sequences of execution.

- The typical difference is that threads (of the same process) run in a shared memory space, while processes run 
in separate memory spaces.

#### Interprocess Communication

##### [Shared memroy](http://advancedlinuxprogramming.com/alp-folder/alp-ch05-ipc.pdf)

- To use a shared memory segment, one process must allocate the segment.

- Then each process desiring to access the segment must attach the segment.

- After finishing its use of the segment, each process detaches the segment.

- At some point, one process must deallocate the segment.

##### [pipe](http://man7.org/linux/man-pages/man7/pipe.7.html)/[fifo](http://man7.org/linux/man-pages/man7/fifo.7.html)

- More preferable than shm 

- [https://stackoverflow.com/questions/43923518/how-to-put-a-variable-in-a-shared-memory](https://stackoverflow.com/questions/43923518/how-to-put-a-variable-in-a-shared-memory)

- [https://stackoverflow.com/questions/9701757/when-to-use-pipes-vs-when-to-use-shared-memory](https://stackoverflow.com/questions/9701757/when-to-use-pipes-vs-when-to-use-shared-memory)

#### TCP vs UDP

##### TCP

- Guarantees that all sent packets will reach the destination in the correct order.

- Acknowledgement packets sent back to the sender, and automatic retransmission.

##### UDC

- Communication is datagram oriented.

- Datagrams reach destination and can arrive out of order or don't arrive at all.

#### [Consumer and Producer Problem](https://en.wikipedia.org/wiki/Producer%E2%80%93consumer_problem)

##### Using semaphore

```
semaphore fillCount = 0; // items produced
semaphore emptyCount = BUFFER_SIZE; // remaining space

procedure producer() {
    while (true) {
        item = produceItem();
        down(emptyCount);
        putItemIntoBuffer(item);
        up(fillCount);
    }
}

procedure consumer() {
    while (true) {
        down(fillCount);
        item = removeItemFromBuffer();
        up(emptyCount);
        consumeItem(item);
    }
}
```

##### Using monitor

```
monitor ProducerConsumer {
    int itemCount;
    condition full;
    condition empty;

    procedure add(item) {
        while (itemCount == BUFFER_SIZE) {
            wait(full);
        }

        putItemIntoBuffer(item);
        itemCount = itemCount + 1;

        if (itemCount == 1) {
            notify(empty);
        }
    }
    procedure remove() {
        while (itemCount == 0) {
            wait(empty);
        }

        item = removeItemFromBuffer();
        itemCount = itemCount - 1;

        if (itemCount == BUFFER_SIZE - 1) {
            notify(full);
        }


        return item;
    }
}

procedure producer() {
    while (true) {
        item = produceItem();
        ProducerConsumer.add(item);
    }
}

procedure consumer() {
    while (true) {
        item = ProducerConsumer.remove();
        consumeItem(item);
    }
}
```