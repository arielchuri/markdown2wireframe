<!--div class="page"-->

<!--header class=" flex space-between"-->
<div>
LOGO
</div>
<!--nav-->
- [one](sub/sub.md)
- [two](two.md)
- [three](three.md)
<!--/nav-->
<!--/header-->
---------------------
# Wireframes from markdown
<!--div class="block center hatch"-->
<div class="sign">
HERO IMAGE
</div>
<!--/div-->
## A brief overview.

This is a first pass at generating responsive wireframes from simple **markdown** files. I love creating notes in **markdown** and creating an outline of content for a page in a text file is standard procedure. It is a simple matter to convert **markdown** to **HTML** so *why not include some blocks to show basic page layout* and have it be responsive.

With this short python script and CSS file, you can convert a folder of markdown files into HTML files with blocks or rows of blocks that are in a column on mobile.

### 2 Blocks
<!--div class="flex"-->
<!--div class="block"-->
**What does markdown look like?**

It is just plain text with a few extra characters.

    #### This is a headline.

    This is some text with
    a **bold** word.

    - Here
    - is a
    - list.
<!--/div-->
<!--div class="block"-->
**What do I need to add to the markdown file to show the wireframe elements?**

Add *div* elements with the classes you want in the form of *HTML comments*. They will be uncommented by the script. If the **markdown** inside the tag does not need to be converted to **HTML**, you can use an **HTML** tag directly.

Here is what the<mark> hero image </mark> box above looks like in the markdown file:

    <!--div class="block center hatch"-->
    <div class="sign">
    HERO IMAGE
    </div>
    <!--/div-->
<!--/div-->
<!--/div-->

### 3 Blocks

<!--div class="flex"-->
<!--div class="block center hatch"-->
<div class="sign">
FPO IMAGE
</div>
<!--/div-->
<!--div class="block center"-->
<a href="https://github.com/arielchuri/markdown2wireframe"><button>gitHub</button></a>
<!--/div-->
<!--div class="block center dashed"-->
Block 3
<!--/div-->
<!--/div-->

Here is a row of three blocks.
The markdown to create them is shown below.

    ### 3 Blocks
    <!--div class="flex"-->
    <!--div class="block center hatch"-->

    <div class="sign">
    FPO IMAGE
    </div>
    <!--/div-->

    <!--div class="block center"-->
    <button>Button</button>
    <!--/div-->

    <!--div class="block center dashed"-->
    Block 3
    <!--/div-->
    <!--/div-->

## Instructions
<!--div class="block"-->
1. Download the [repository](https://github.com/arielchuri/markdown2wireframe/archive/refs/heads/main.zip).
1. Use the<mark> Terminal </mark> application to navigate into the downloaded folder.
1. Edit the _index.md_ file in a <mark>text editor</mark> and add any other **markdown** files you want.
1. Run the script on the current folder by typing ` python md2wire.py . ` in the<mark> terminal </mark>.
1. **HTML** files will be created next to the **markdown** files.
1. Open the [index.html](index.html) file to view your work.
<!--/div-->
## Examples
<!--div class="flex space-between pad"-->
<div class="shape triangle">Research</div>
<div class="shape square">Design</div>
<div class="shape circle">Technology</div>
<!--/div-->
<!--div-->
2nd paragraph. *Italic*, **bold**, and `monospace`. Itemized lists
look like:

  * this one
  * that one
  * the other one

Note that --- not considering the asterisk --- the actual text
content starts at 4-columns in.

> Block quotes are
> written like so.
>
> They can span multiple paragraphs,
> if you like.

Use 3 dashes for an em-dash. Use 2 dashes for ranges (ex., "it's all
in chapters 12--14"). Three dots ... will be converted to an ellipsis.
Unicode is supported. ☺
Here's a numbered list:

 1. first item
 2. second item
 3. third item

Note again how the <mark>actual text</mark> starts at 4 columns in (4 characters
from the left side). Here's a code sample:

    # Let me re-iterate ...
    for i in 1 .. 10 { do-something(i) }
As you probably guessed, indented 4 spaces. By the way, instead of
indenting the block, you can use delimited blocks, if you like:

```
define foobar() {
    print "Welcome to flavor country!";
}
```

<!--/div-->

### An h3 header

Now a nested list:

 1. First, get these ingredients:

      * carrots
      * celery
      * lentils

 2. Boil some water.

 3. Dump everything in the pot and follow
    this algorithm:

        find wooden spoon
        uncover pot
        stir
        cover pot
        balance wooden spoon precariously on pot handle
        wait 10 minutes
        goto first step (or shut off burner when done)

    Do not bump wooden spoon or it will fall.

Notice again how text always lines up on 4-space indents (including
that last line which continues item 3 above).

Here's a link to [a website](http://foo.bar), to a [local
doc](local-doc.html), and to a [section heading in the current
doc](#an-h2-header).

Tables can look like this:

| size | material    | color       |
|------|-------------|-------------|
| 9    | leather     | brown       |
| 10   | hemp canvas | natural     |
| 11   | glass       | transparent |

Table: Shoes, their sizes, and what they're made of

<!--div class="flex"-->
<!--div-->
![example image](cat.jpg)
<!--/div-->
<!--div-->
![example image](cat.jpg)
<!--/div-->
<!--div-->
![example image](cat.jpg)
<!--/div-->
<!--div-->
![example image](cat.jpg)
<!--/div-->
<!--div-->
![example image](cat.jpg)
<!--/div-->

<!--/div-->
