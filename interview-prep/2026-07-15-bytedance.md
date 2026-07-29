# Interview retro — 2026-07-15 ByteDance

## Whiteboard problems

1. **Quicksort** — wrote it, but explained the `partition` boundary conditions poorly; got pushed on it twice.
2. **LRU Cache** — nailed it with `OrderedDict`, but when asked "without built-ins?" I couldn't write it.
3. **Binary tree diameter** — had done it before, but misremembered the definition (thought it was edge count; it's node count - 1).

## Retro

- Quicksort `partition` needs more handwriting practice, not muscle memory.
- LRU with doubly-linked list + HashMap — must fill this gap; can't only know the library version.
- Binary-tree diameter = `left_depth + right_depth`, not edges. Second time hitting this.

## Next focus

- [ ] Hand-write LRU (no OrderedDict)
- [ ] Explain quicksort partition boundaries clearly
- [ ] Binary trees: diameter, LCA, serialization
