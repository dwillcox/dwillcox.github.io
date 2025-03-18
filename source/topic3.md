```yaml
title: Topic 3
subtitle: Topic 3 is Barely An Inconvenience
```

Here is some welcome text that tells you what to expect.

But this section is printed in normal font, it is not part of the title or subtitle.

# First Content

This text explains the first content.

# Second Content

The second content contains text and a figure.

```yaml
class: Figure
title: Second Welcoming Content
source: pic01.jpg
caption: A graphic illustrating the second reason you should feel welcome here. 
```

# Third Content

This text explains the third content.

```yaml
class: Figure
title: Third Welcoming Content
source: pic01.jpg
caption: A graphic illustrating the third reason you should feel welcome here. 
```

---

The three dashes above mark the end of the entry consisting of the set of (First Content, Second Content).

If we were to place those three dashes after this line, then everything between the dashes and "Second Content" above would be part of the same section.

# This new heading is a new entry in this Scene file.

Note that if the first YAML block is not found, use the filename without the extension as the title and leave the subtitle blank.

The file end is the natural end point of this entry, so it consists of one content object.
