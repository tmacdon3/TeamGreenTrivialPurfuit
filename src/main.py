"""
The main file called to run the whole application
"""

from TrivialPurfuitApp import TrivialPurfuitApp

if __name__ == "__main__":
    pw = input("Enter MySQL root password (if applicable): ")
    app = TrivialPurfuitApp(pw)
    app.mainloop()