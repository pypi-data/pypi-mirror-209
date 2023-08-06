# FlapGUI
Flap (Framework for making Lightweight and Automatic Programs) is a GUI framework for creating cross-platform GUI applications easily using Tkinter. 
# Purpose
FlapGUI is designed to make writing GUI applications as simple as possible, eliminating the learning curve for making functional programs. 

Most GUI frameworks (tkinter, qt, gtk, etc.) have a steep learning curve, which FlapGUI intends to fix.

**Flap is in beta and is not complete. It is subject to rapid and signigicant change at the moment.**
# Module Functions

1. window(title="flapWindow", width=250, height=250)
   - Creates a window.

2. subWindow(root, title=None, width=250, height=250, close_parent=True)
   - Creates a sub-window.

3. disableElement(element)
   - Makes the specified element greyed out/disabled.

4. createCheckbox(root, label, isChecked=False, fg="black")
   - Creates a checkbox widget.

5. getCheckboxState(checkbox)
   - Returns the state of the checkbox widget.

6. changeWidgetColor(widget, background_color, text_color=None)
   - Changes the color of the specified widget.

7. changeAccentColor(root, background_color, text_color=None)
   - Changes the accent color of the root window and its child widgets.

8. createFrame(root)
   - Creates a frame widget.

9. lockWindowPos(root)
   - Locks the window at its current position.

10. unlockWindowPos(root)
    - Allows the window to be moved.

11. createHyperlinkText(root, label_text, url)
    - Creates a label with a hyperlink.

12. changeTitle(root, new_title)
    - Changes the title of the root window.

13. autoScaleResolution(window)
    - Automatically scales the window resolution based on widget sizes.

14. scaleResolution(window, width, height)
    - Scales the window resolution to the specified width and height.

15. maximiseWindow(window)
    - Maximizes the window to full screen.

16. addText(root, text)
    - Adds a text label to the root window.

17. textEntry(width, height, fg=None, bg=None)
    - Creates a text entry widget.

18. framedTextEntry(window, width=40, bg="#FFFFFF", fg="#000000")
    - Creates a framed text entry widget.

19. lockText(text)
    - Disables editing of the text widget.

20. unlockText(text)
    - Enables editing of the text widget.

21. makeTabbable(text)
    - Makes the text widget navigable using the Tab key.

22. makeUnclosable(root)
    - Prevents the root window from being closed.

23. makeReclosable(root)
    - Allows the root window to be closed.

24. menuBar(root)
    - Creates a menu bar widget.

25. addCascade(menuBar, label)
    - Adds a cascade menu to the menu bar.

26. addCommand(cascade, label, command=None, accelerator=None)
    - Adds a command to the cascade menu.

27. keyBind(root, binding, command=None)
    - Binds a key press event to a command.

28. addText(root, label_text)
    - Adds a text label to the root window.

29. addFrameScrollbar(frame)
    - Adds a scrollbar to a frame with a canvas.

30. messageBox(title, message)
    - Displays a message box with the specified title and message.

31. addScrollbar(root, text)
    - Adds a scrollbar to a text widget.

32. selectAll(text, event=None)
    - Selects all text in the text widget.

33. disallowEnter(text)
    - Disallows the newline character in the text widget.

34. setText(text_widget, text)
    - Sets the text content of the text widget.

35. getText(text_widget)
    - Retrieves the text content of the text widget.

36. createButton(root, label, command=None)
    - Creates a button widget.

37. appendText(text_widget, string)
    - Appends a string to the text widget.

38. createGrid(root)
    - Creates a grid widget
