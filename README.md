# leetcode_journal

archive of attempts, solutions, and ai conversations.

## structure

organized by blind 75 / neetcode 150 patterns.

```text
leetcode_journal/
├── arrays-hashing/
├── two-pointers/
├── ...
├── _TEMPLATES/      <-- copy these
│   ├── notes.md
│   └── solution.py
├── PROMPTS.md       <-- sanitizer prompt
└── README.md
```

## workflow

mobile-first with gemini 3 pro.

1. **solve & chat**: natural conversation with the llm.
2. **sanitize**: open `PROMPTS.md`, copy the prompt, paste into chat.
3. **transfer**: copy the clean markdown block output.
4. **archive**: paste into `notes.md` when back at terminal.

## conventions

*   **folders**: `difficulty-problem-name` (e.g. `easy-two-sum`)
*   **files**: `notes.md` and `solution.py` only.
