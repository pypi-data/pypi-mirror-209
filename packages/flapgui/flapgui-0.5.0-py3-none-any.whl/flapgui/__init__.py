#!/usr/bin/python

# FlapGUI 0.5

import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import tkinter.colorchooser
import webbrowser
import functools

global app_version
app_version = [0,5,0]
global verbose
verbose = False

def ignore_tcl_error(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except tk.TclError:
            pass  # Ignore the error
    return wrapper

def window(title="flapWindow", width=250, height=250):
    """
Creates a window.
    """
    if verbose:
        print(f"Flap: Created window \"{title}\" with resolution {width}x{height}")
    window = tk.Tk()
    #setattr(root,"defaultColor",root.cget("background"))
    window.title(title)
    window.geometry(f"{width}x{height}")
    return window

def subWindow(root, title=None, width=250, height=250, close_parent=True):
    child_window = tk.Toplevel(root)
    child_window.title(title)
    child_window.geometry(f"{width}x{height}")
    
    if close_parent:
        child_window.protocol("WM_DELETE_WINDOW", child_window.destroy)
    else:
        child_window.protocol("WM_DELETE_WINDOW", root.destroy)
    
    return child_window
def disableElement(element):
    """
    Makes the element specified greyed out/disabled.
    
    Args:
        element (tkinter.Widget): The tkinter widget to be disabled.
    """
    if isinstance(element, tk.Menu):
        element.entryconfig(0, foreground='gray')
    else:
        element.configure(state='disabled')
def changeAlignment(widget, alignment):
    """
    Aligns a widget to a specific alignment.

    Args:
        widget: The widget to be aligned.
        alignment: The desired alignment. Possible values: 'left', 'right', 'top', 'bottom', 'center'.

    Raises:
        ValueError: If an invalid alignment value is provided.
    """
    valid_alignments = ['left', 'right', 'top', 'bottom', 'center']

    if alignment not in valid_alignments:
        raise ValueError("Invalid alignment value. Please use one of the following: 'left', 'right', 'top', 'bottom', 'center'.")

    # Clear any existing alignment
    widget.pack_forget()
    widget.pack(fill=tk.BOTH, expand=True)

    if alignment == 'left':
        widget.pack_configure(anchor=tk.W)
    elif alignment == 'right':
        widget.pack_configure(anchor=tk.E)
    elif alignment == 'top':
        widget.pack_configure(anchor=tk.N)
    elif alignment == 'bottom':
        widget.pack_configure(anchor=tk.S)
    elif alignment == 'center':
        widget.pack_configure(anchor=tk.CENTER)
def createCheckbox(root, label, isChecked=False, fg="black"):
    checkbox_var = tk.BooleanVar(value=isChecked)
    checkbox = tk.Checkbutton(root, text=label, variable=checkbox_var, fg=fg)
    checkbox.pack()
    return checkbox

def getCheckboxState(checkbox):
    checkbox_var = checkbox.cget("variable")
    return checkbox_var.get()
@ignore_tcl_error
def changeWidgetColor(widget, background_color, text_color=None):
    widget.configure(selectcolor=background_color)
    if text_color:
        widget.configure(fg=text_color)
    widget.update_idletasks()
@ignore_tcl_error
def changeAccentColor(root, background_color, text_color=None):
    root.tk_setPalette(background=background_color)
    for widget in root.winfo_children():
        if isinstance(widget, tk.Checkbutton):
            changeWidgetColor(widget, background_color, text_color)
        else:
            changeWidgetColor(widget, background_color, text_color)
            if isinstance(widget, tk.Toplevel):
                changeAccentColor(widget, background_color, text_color)
def createDropDown(root, strings=[]):
    # Create a drop down widget
    drop_down = ttk.Combobox(root, values=strings)
    drop_down.pack()
    
    return drop_down

def getDropDownState(drop_down):
    # Get the selected option in the drop down
    selected_option = drop_down.get()
    
    return selected_option

def createRadioButtons(root, buttons=[],alignment=None):
    # Create radio buttons
    selected_button = tk.StringVar()
    
    for button_text in buttons:
        radio_button = tk.Radiobutton(root, text=button_text, variable=selected_button, value=button_text)
        if alignment:
            changeAlignment(radio_button,alignment)
        radio_button.pack(anchor=tk.W)
    
    return selected_button

def getRadioButtonState(radio_buttons):
    # Get the selected radio button's value
    selected_value = radio_buttons.get()
    
    return selected_value
def createFrame(root):
    frame = tk.Frame(root)
    frame.pack()
    return frame
def lockWindowPos(root):
    """Locks the window from being moved at its current position."""
    root.attributes("-topmost", True)

def unlockWindowPos(root):
    """Allows the window to be moved."""
    root.attributes("-topmost", False)
def createHyperlinkText(root, label_text, url):
    label = tk.Label(root, text=label_text, fg='blue', cursor='hand2')
    label.pack()
    label.bind('<Button-1>', lambda e: webbrowser.open(url))
def changeTitle(root, new_title):
    root.title(new_title)
def autoScaleResolution(window):
    window.update_idletasks()  # Update window to ensure accurate widget sizes
    width = window.winfo_reqwidth()
    height = window.winfo_reqheight()
    scaleResolution(window,width,height)
def scaleResolution(window, width, height):
    if verbose:
        print(f"Flap: Scaled Resolution to {width}x{height}")
    window.geometry(f"{width}x{height}")
def maximiseWindow(window):
    window.attributes('-zoomed', True)
def addText(root, text):
    label = tk.Label(root, text=text)
    label.pack()
def textEntry(width, height,fg=None,bg=None):
    if verbose:
        print(f"Flap: Made new text entry: bg {bg} fg {fg}")
    text_box = tk.Text(width=width, height=height,fg=fg,bg=bg,insertbackground=fg)
    return text_box
def framedTextEntry(window, width=40, bg="#FFFFFF", fg="#000000"):
    if verbose:
        print(f"Flap: Made new framed text entry: bg {bg} fg {fg}")

    # Create a frame to hold the Text widget and scrollbar
    frame = tk.Frame(window)
    frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Create a Text widget with the specified width
    text = tk.Text(frame, width=width, bg=bg, fg=fg, insertbackground=fg)
    text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Create a Scrollbar widget
    scrollbar = ttk.Scrollbar(frame, command=text.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Configure the Text widget to use the Scrollbar
    text.configure(yscrollcommand=scrollbar.set)

    return text
def lockText(text):
    if verbose:
        print("Flap: Locked text")
    text.config(state="disabled")

def unlockText(text):
    text.config(state="normal")
def makeTabbable(text):
    def handle_tab(event):
        event.widget.tk_focusNext().focus()
        return "break"  # Prevent default tab behavior

    text.bind("<Tab>", handle_tab)

def makeUnclosable(root):
    if verbose:
        print("Made window unclosable")
    def disable_close_button():
        pass

    root.protocol("WM_DELETE_WINDOW", disable_close_button)
def makeReclosable(root):
    if verbose:
        print("Made window closable")
    root.protocol("WM_DELETE_WINDOW", root.destroy)
def menuBar(root):
    if verbose:
        print(f"Flap: Added Menu Bar")
    # create the menu bar widget
    menu_bar = tk.Menu(root)
    root.config(menu=menu_bar)
    return menu_bar
def addCascade(menuBar,label):
    if verbose:
        print(f"Flap: New Cascade \"{label}\"")
    # create a new menu
    cascade_menu = tk.Menu(menuBar, tearoff=0)
    # add the cascade menu to the menu bar
    menuBar.add_cascade(label=label, menu=cascade_menu)
    return cascade_menu
def addCommand(cascade, label, command=None, accelerator=None):
    if verbose:
        print(f"Flap: Added Command To Cascade: {label}")
    cascade.add_command(label=label, command=command,accelerator=accelerator)  
def keyBind(root,binding,command=None):
    if verbose:
        print(f"Flap: Added Binding: {binding}")
    root.bind(binding,command)
def addText(root, label_text):
    label = tk.Label(root, text=label_text)
    label.pack()
def addFrameScrollbar(frame):
    scrollbar = tk.Scrollbar(frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    canvas = tk.Canvas(frame, yscrollcommand=scrollbar.set)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar.config(command=canvas.yview)

    content_frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=content_frame, anchor="nw")

    def configure_scrollbar(event):
        canvas.configure(scrollregion=canvas.bbox("all"), width=200, height=200)

    content_frame.bind("<Configure>", configure_scrollbar)

    return content_frame
def messageBox(title,message,root=None):
    if root:
        w=subWindow(root,title)
    else:
        w=window(title)
    addText(w,message)
    createButton(w,"OK",w.destroy)
    keyBind(w,"<Return>",lambda event:w.destroy())
    keyBind(w,"<Escape>",lambda event:w.destroy())
    keyBind(w,"<Control-q>",lambda event:w.destroy())
    autoScaleResolution(w)
def addScrollbar(root, text):
    scrollbar = tk.Scrollbar(root)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    scrollbar.config(command=text.yview)
    text.config(yscrollcommand=scrollbar.set)
    text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
def selectAll(text,event=None):
    if verbose:
        print("Flap: Selected All Text")
    text.tag_add(tk.SEL, "1.0", tk.END)
    text.mark_set(tk.INSERT, "1.0")
    text.see(tk.INSERT)
def disallowEnter(text):
    def handle_return(event):
        return "break"  # Prevent newline insertion

    text.bind("<Return>", handle_return)
def setText(text_widget, text):
    if verbose:
        print(f"Set Text To {text}")
    
    # Check if the text widget is locked
    is_locked = text_widget.cget("state") == "disabled"
    
    # Temporarily unlock the text widget if it is locked
    if is_locked:
        text_widget.config(state="normal")
    
    text_widget.delete('1.0', tk.END)
    text_widget.insert(tk.END, text)
    
    # Lock the text widget again if it was initially locked
    if is_locked:
        text_widget.config(state="disabled")
def getText(text_widget):
    text = text_widget.get("1.0", tk.END).strip()
    return text
def createButton(root,label,command=None):
    if verbose:
        print(f"Flap: Made button \"{label}\"")
    button = tk.Button(root, text=label, command=command)
    button.pack()
    return button
def appendText(text_widget,string):
    if verbose:
        print(f"Flap: Added \"{string}\" to text widget")
    set_text(text_widget,getText(text_widget)+string)
def createGrid(root):
    grid = tk.Frame(root)
    grid.pack()
    return grid
def addGridButton(grid, label, function, x, y, buttonDimensionX=2, buttonDimensionY=1):
    button = tk.Button(grid, text=label, command=function)
    button.config(width=buttonDimensionX, height=buttonDimensionY)
    button.grid(row=x, column=y)

def fileSelector(is_file=True):
    if verbose:
        print("Flap: Open File Selector: IsFile",str(is_file))
    root = tk.Tk()
    root.withdraw()
    if is_file:
        file_path = filedialog.askopenfilename()
    else:
        file_path = filedialog.askdirectory()
    if verbose:
        print("Flap: User Selected",file_path)
    return file_path
def colorChoose():
    color = tk.colorchooser.askcolor(title="Choose color")
    if color:
        r, g, b = map(int, color[0])
        return f"#{r:02x}{g:02x}{b:02x}"
    else:
        return None
def getVersion():
    return app_version
def lockWindowSize(root):
    root.resizable(0, 0)
def unlockWindowSize(root):
    root.resizable(1, 1)
class FlowLayout(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.widgets = []

    def add_widget(self, widget):
        self.widgets.append(widget)
        self._update_layout()

    def _update_layout(self):
        # Clear the frame
        for widget in self.winfo_children():
            widget.pack_forget()

        # Add widgets to the frame
        for widget in self.widgets:
            widget.pack(side=tk.LEFT)

        # Update the frame's size
        self.update_idletasks()
        self.config(width=self.winfo_reqwidth(), height=self.winfo_reqheight())
def addFlowButton(flowLayout, label, command=None, width=2, height=1):
    button = tk.Button(flowLayout, text=label, command=command, width=width, height=height)
    button.pack()
    flowLayout.add_widget(button)

def addFlowText(flowLayout, label):
    text = tk.Label(flowLayout, text=label)
    text.pack()
    flowLayout.add_widget(text)
print(f"Flap: Initialised Framework ({app_version[0]}.{app_version[1]}.{app_version[2]})")
