import rumps
from datetime import datetime
import webbrowser

def get_week_number():
    """
    Calculate the current week number according to the ISO 8601 standard,
    which is used in Sweden.
    """
    today = datetime.now()
    week_number = today.isocalendar()[1]
    return week_number

class WeeNu(rumps.App):
    def __init__(self):
        super(WeeNu, self).__init__("WeeNu")
        self.title_format = "w. {week_number}"

        # Version info
        self.menu = ["WeeNu v0.1", None]
        
        # Creating a submenu for format toggling
        self.settings_menu = rumps.MenuItem("Settings")
        self.toggle_week_prefix_item = rumps.MenuItem("Show prefix", callback=self.toggle_format)
        
        self.settings_menu.add(self.toggle_week_prefix_item)

        # Initializing the menu item's state to True
        self.toggle_week_prefix_item.state = True

        # Add a divider/separator here
        self.menu = ["Manual update", self.settings_menu, None]  # 'None' acts as a separator
        
        # Add a GitHub link menu item
        self.github_link_item = rumps.MenuItem("About WeeNu", callback=self.open_github)
        self.menu.add(self.github_link_item)

        self.update_title()

    @rumps.timer(60)  # Update every 60 seconds
    def update_title(self, _=None):
        """
        Updates the menu bar title with the current week number, according to the selected format.
        """
        week_number = get_week_number()
        self.title = self.title_format.format(week_number=week_number)

    @rumps.clicked("Manual update")
    def on_update(self, _):
        """
        Manually updates the week number when the 'Update' menu item is clicked.
        """
        self.update_title()

    def toggle_format(self, sender):
        """
        Toggles the title format and the checkmark state based on the current state.
        """
        # Toggle the state and adjust the format based on the new state
        sender.state = not sender.state
        if sender.state:
            self.title_format = "w. {week_number}"
            sender.title = "Hide prefix"
        else:
            self.title_format = "{week_number}"
            sender.title = "Show prefix"
        self.update_title()
    
    def open_github(self, _):
        """
        Opens the GitHub repository URL in the default web browser.
        """
        webbrowser.open('https://github.com/mullweisser/mac-weenu')

if __name__ == "__main__":
    WeeNu().run()