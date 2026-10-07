# The hero section of my website

The hero section is the first thing a visitor sees on my website, before
they scroll. Copy this file, fill in the block below for your own
business, put it in an empty folder with your files, and ask the AI to
build the hero section by it.

## Fill in once

- My business, in one sentence:
- Who the visitor is:
- The ONE thing they should do on the page:
- One proof I have (a number, a type of client):
- 2 sites I like:
- My files:

Rule: if a line above is empty, ask me for it. Never guess it.

## How to work

- Do the steps in order, one at a time.
- Each step reads only the file of the step right before it, and writes
  its own file. Step 1 is the only step that reads the block above.
- Each step's file ends with `## Carried forward`: copy that part of the
  file before it whole, then add what the step says. What a later step
  needs travels in it; never go back to an older file.
- In every step: ask what the step says to ask, do the work, show it to
  me, then stop and wait for my word. My answers go into the step's file
  before you go on.
- Redoing a step rewrites its file; every step after it is then out of
  date and is done again.
- Write no code before step 5.

## Steps

### 1. Understand the visitor

Reads: the block above.
Writes: `01-visitor.md`.

Ask first: the empty lines of the block, then these three questions,
one at a time:
- What does my visitor struggle with?
- What words do they use for it, when they say it themselves?
- What makes them trust someone like me?

Do: write one paragraph called "The visitor, in their words", built
from my answers. Show it, then stop.
Carry forward: every line of the block, filled.

Done when:
- Every line of the block is filled.
- The paragraph uses the words I gave you, not yours.
- I approved the paragraph.

### 2. The design

Reads: `01-visitor.md`.
Writes: `02-design.md`.

Ask first: what I like about each of the two sites in the carried block.

Do: open the two sites and propose two design directions, each grounded
on one of them: the layout, the colours, the type, where the text sits
on the background. Describe them in words or a rough sketch, no code.
Show both, then stop. I pick one and we change it until I am happy.
Carry forward: what `01-visitor.md` carried, its paragraph, and the
design I chose.

Done when:
- Each direction names the site it comes from.
- No code was written.
- I said the design is done. Until I say it, we keep changing it.

### 3. Pictures and video

Reads: `02-design.md`.
Writes: `03-files.md`.

Ask first: which of my files I want in the section.

Do: use only the files listed in the carried block. If the design needs
something I do not have, write a list of what to shoot or get. Never
download, generate or invent a picture or a video. Show the files you
will use, each with its alt text, then stop.
Carry forward: what `02-design.md` carried, plus the files to use with
their alt text.

Done when:
- Every picture and the video are my own files.
- Every picture has alt text that says what is in it.
- Anything missing is on the list for me, not replaced by something else.

### 4. The words

Reads: `03-files.md`.
Writes: `04-words.md`.

Ask first: nothing new.

Do: write three headlines, each built from the visitor's own words in
the carried paragraph. Test each one: could a competitor say this too?
If yes, rewrite it. Under the headline, one sentence. Then one button.
Show the three, then stop. I pick one.
Carry forward: what `03-files.md` carried, plus the headline, the
sentence and the button I chose.

Done when:
- Each headline uses words from the carried paragraph.
- No headline could stand on a competitor's site unchanged.
- No hype words and no exclamation marks.
- There is one button, and it does the ONE thing from the carried block.

### 5. Build it and check it

Reads: `04-words.md`.
Writes: `index.html` (with its CSS inside) and `05-check.md`.

Ask first: nothing new.

Do: build the section from the design, the files and the words carried
in `04-words.md`. Then go through every point below, one at a time, and
write pass or fail for each into `05-check.md`, with what you checked.

Done when:
- It opens in a browser with no internet connection.
- The video plays as the background, silent, in a loop.
- The text is easy to read on top of the video.
- It reads well on a phone screen and on a laptop.
- The video file is under 5 MB, so the page loads fast.
- `05-check.md` has pass or fail for every point of this step.
- I said it is done.
