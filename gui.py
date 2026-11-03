import string
import tkinter as tk
from pathlib import Path
from tkinter import simpledialog, messagebox
import problemlogprocess as dlg
import problemdecription as prob


class PrintWindow(tk.Frame):
    #Read-only, scrollable text area

    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app
        scroll_bar = tk.Scrollbar(self)
        scroll_bar.pack(side="right", fill="y")
        self.output = tk.Text(self, wrap="word", padx=20, pady=20,
                              state="disabled", yscrollcommand=scroll_bar.set)
        self.output.pack(side="left", fill="both", expand=True)
        scroll_bar.config(command=self.output.yview)
        self.apply_theme()

    def apply_theme(self):
        # Style with the current dark mode / text size settings
        # Apply dark mose
        t = self.app.theme()
        self.output.config(bg=t["text_bg"], fg=t["fg"], font=("Arial", self.app.size.get()))

    def show_text(self, text):
        # Unlock the text box, replace its content, lock it again
        self.output.config(state="normal")
        self.output.delete("1.0", "end")
        self.output.insert("end", text)
        self.output.config(state="disabled")


class HelpPage(tk.Frame):
    # The main page

    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app

        self.reported_problem = "" # Variable for the report button

        self.search_area = tk.Frame(self)
        self.search_area.place(relx=0, rely=0, relwidth=0.3, relheight=1)

        self.text_area = PrintWindow(self, app)
        self.text_area.place(relx=0.3, rely=0, relwidth=0.7, relheight=1)

        self.build_search_area()
        self.apply_theme()


    def build_search_area(self):
        # build the search area
        # Each problem here is a button that can be pressed to show text in text_area

        # Search box for filtering the button
        # Report button to report problem currently showed on the text_area
        self.search = tk.StringVar()
        self.search.trace_add("write", lambda *a: self.show_buttons())
        self.search_box = tk.Entry(self.search_area, textvariable=self.search)
        self.report_button = tk.Button(self.search_area, text= "Report Problem", command=lambda: self.addNewLog())
        self.search_box.pack(fill="x", padx=10, pady=10)
        self.report_button.pack(fill="x", padx=10, pady=10)

        # Canvas with scrollbar so the button list can scroll
        # Under the searchbar
        box = tk.Frame(self.search_area)
        box.pack(fill="both", expand=True)
        self.canvas = tk.Canvas(box, highlightthickness=0)
        scroll_bar = tk.Scrollbar(box, command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=scroll_bar.set)
        scroll_bar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)

        # Frame inside the canvas that holds the buttons
        self.button_frame = tk.Frame(self.canvas)
        self.window = self.canvas.create_window((0, 0), window=self.button_frame, anchor="nw")
        self.canvas.bind("<Configure>", lambda e: self.canvas.itemconfig(self.window, width=e.width))
        self.button_frame.bind("<Configure>",
                               lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        # Mouse wheel scrolling while the mouse is over the search_area panel
        self.search_area.bind("<Enter>", lambda e: self.canvas.bind_all("<MouseWheel>", self.scroll_left))
        self.search_area.bind("<Leave>", lambda e: self.canvas.unbind_all("<MouseWheel>"))


    def apply_theme(self):
        # Re-style everything using the current dark mode / text size settings
        t, size = self.app.theme(), self.app.size.get()
        for w in (self.search_area, self.canvas, self.button_frame):
            w.config(bg=t["side"])
        self.search_box.config(bg=t["btn"], fg=t["fg"], insertbackground=t["fg"], font=("Arial", size - 2))
        self.text_area.apply_theme()
        self.show_buttons()


    def show_buttons(self):
        # Rebuild the buttons that match the search text if typing into the button
        t, size = self.app.theme(), self.app.size.get()
        for widget in self.button_frame.winfo_children():
            widget.destroy()
        wrap = int(self.winfo_screenwidth() * 0.3) - 60  # text wraps, so height grows but width stays fixed

        for problem in prob.PROBLIST.getProblemList():
            if self.search.get().lower() in problem.getProblemName().lower():
                tk.Button(self.button_frame, text=problem.getProblemName(), wraplength=wrap, justify="left",
                          anchor="w", padx=10, pady=10, font=("Arial", size - 4),
                          bg=t["btn"], fg=t["fg"], activebackground=t["side"], activeforeground=t["fg"],
                          command=lambda
                          x=f"{problem.getProblemName()}\n\nDescription:\n{problem.getProblemDescription()}\n\nCause:\n{problem.getProblemCause()}\n\nSolution:\n{problem.getProblemSolution()}"
                          ,y = problem.getProblemName()
                          : self.problemSet(x, y)).pack(fill="x", padx=10, pady=3)

    def problemSet(self, text, problem_name):
        # Set the selected problem into reported_problem and print the description
        self.reported_problem = problem_name
        self.text_area.show_text(text)

    def addNewLog(self):
        #Adds a report in the problemlog.jsonl using the addProblemDataLog method logdatabaselogic
        #uses the reported_

        class ProblemNotSelected(Exception): pass

        try:
            if self.reported_problem == "":
                raise ProblemNotSelected
        except ProblemNotSelected:
            tk.messagebox.showerror("Error", "Problem Not Selected")
            return

        is_add_new = tk.messagebox.askokcancel(title="Report Problem", message="Report Problem")
        if is_add_new:
            tk.messagebox.showinfo("Problem Reported", f"Problem Name: {self.reported_problem}")
            dlg.problem_log.addProblemDataLog(self.reported_problem)
            self.apply_theme()

    def scroll_left(self, event):
        self.canvas.yview_scroll(-1 * (event.delta // 120), "units")





class ReportLogPage(PrintWindow):
    # Shows the logs in the Report log page as text

    def apply_theme(self):
        super().apply_theme()
        if dlg.problem_log.is_lost_file():
            messagebox.showerror("Error", "Missing problemlog.jsonl")
        self.show_text(f"""Username: {dlg.problem_log.getNameString()}\n\n{dlg.problem_log.getLogString()}""")





class MainGUI:
    def __init__(self, root):
        self.root = root

        # Window is screen-sized, keeps the title bar, and the resize/maximize button is disabled
        sw, sh = root.winfo_screenwidth(), root.winfo_screenheight()
        root.geometry(f"{sw}x{sh - 80}+0+0")  # -80 leaves room for the title bar and taskbar
        root.resizable(False, False)

        # Sets the icon and the titlebar
        icon_path = Path("pictures")/"icon.png"
        if icon_path.exists():
            icon = tk.PhotoImage(file= icon_path)
            root.iconphoto(True, icon)
        root.title("Computer Network Troubleshoot Assistance")

        # Settings values shared by all pages
        self.dark = tk.BooleanVar(value=False)
        self.size = tk.IntVar(value=16)

        self.username = dlg.problem_log.getNameString()

        if dlg.problem_log.is_lost_file():
            messagebox.showerror("Error", "Missing username.json")

        # Pages (all stacked in the same spot, only one is shown at a time)
        self.pages = {"Help": HelpPage(root, self), "Report Logs": ReportLogPage(root, self)}
        self.build_menu()
        self.show("Help")

    #for dark mode
    def theme(self):
        # Colors for light and dark mode
        if self.dark.get():
            return {"side": "#2b2b2b", "btn": "#444444", "text_bg": "#1e1e1e", "fg": "#ffffff"}
        return {"side": "#d9d9d9", "btn": "#f5f5f5", "text_bg": "#ffffff", "fg": "#000000"}

    def build_menu(self):
        # For Menu bar
        # Has 3 menu: page Main, page Report log, and Setting menu
        # Setting menu has sub-menu for dark mode, 3 text sizes, clear logs, and change name

        # Init the menu bar
        menubar = tk.Menu(self.root)

        # For the page menu
        menubar.add_command(label="Help", command=lambda: self.show("Help"))
        menubar.add_command(label="Report Log", command=lambda: self.show("Report Logs"))

        # Settings menu: dark mode toggle + text size choices
        settings = tk.Menu(menubar, tearoff=0)
        settings.add_checkbutton(label="Dark mode", variable=self.dark, command=self.apply_settings) # Dark Mode
        settings.add_separator()
        for label, value in (("Small text", 12), ("Medium text", 16), ("Large text", 20)):           # Three text sizes
            settings.add_radiobutton(label=label, variable=self.size, value=value,
                                     command=self.apply_settings)
        settings.add_separator()
        settings.add_command(label="Change username...", command=self.change_username)               # Change Username
        settings.add_separator()
        settings.add_radiobutton(label="Clear Log History...", command= self.clearLog)               # Clear Log
        menubar.add_cascade(label="Settings", menu=settings)

        #about
        menubar.add_command(label="About", command=lambda: self.about())


        self.root.config(menu=menubar)


    @staticmethod
    def about():
        # Messagebox for version and Creators/Contributors
        messagebox.showinfo(title="About",
                            message="Computer Network Troubleshoot Assistance V1.0.0\n\n"
                                    "Creators/Contributors:\nMelvin Castillo\nLuis Gabriel Conception", icon="info")

    def show(self, name):
        # Hide every page, then show the chosen one
        for page in self.pages.values():
            page.place_forget()
        self.pages[name].place(relx=0, rely=0, relwidth=1, relheight=1)
        self.apply_settings()

    def change_username(self):
        # Change the username

        #Error Init
        class InvalidUserName(Exception):pass
        class EmptyUserName(Exception):pass

        # Ask for a new name
        # Only accepts alpha-numericals and . and _ characters
        # Throws a messagebox error otherwise

        name = simpledialog.askstring("Change username", "Enter new username:",
                                      initialvalue=self.username, parent=self.root)
        name = str(name).lstrip()
        print(name)
        ALLOWED_CHARACTERS = set(string.ascii_letters + string.digits + "_" + "." + string.whitespace)
        try:
            #if name == "" or not(name.isalnum() and ".","_" in name):
            if name == "" or name is None:
                raise EmptyUserName
            for char in name:
                if char not in ALLOWED_CHARACTERS:
                    raise InvalidUserName
        except InvalidUserName:
            tk.messagebox.showerror("Error: Invalid Character", "Allowed Characters of Username is: A-Z, a-z, 0-9, . ,and _")
        except EmptyUserName:
            tk.messagebox.showerror("Error: Empty Character", "The Username Entry is Blank")
        else:
            dlg.problem_log.rename(name)
            self.username = dlg.problem_log.getNameString()
            self.apply_settings()

    def clearLog(self):
        # Clears the log in problemlog via the clearLog() method in dlg
        is_clear_log = messagebox.askokcancel(title="Clear Log", message="Are you sure you want to clear the log?", icon="warning")
        if is_clear_log:
            dlg.problem_log.clearLog()
            self.apply_settings()

    def apply_settings(self):
        #apply the theme for every page
        for page in self.pages.values():
            page.apply_theme()