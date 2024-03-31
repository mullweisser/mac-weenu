import rumps
from datetime import datetime
import webbrowser
import os

def get_week_number():
    today = datetime.now()
    week_number = today.isocalendar()[1]
    return week_number

class PrefixFormatter:
    def __init__(self):
        self.prefix_formats = self.load_prefixes_from_file()
        self.current_format = self.load_format()

    def format_with_week(self, week_number):
        self.current_format_formatted = f"{self.current_format} {week_number}"
        return self.current_format_formatted

    def save_format(self, format_str):
        try:
            with open('user_settings', 'w') as f:
                f.write(format_str)
                self.current_format = format_str
        except IOError as e:
            rumps.alert(f"Error saving current prefix format: {e}")

    def load_format(self):
        if not os.path.exists('user_settings'):
            return self.prefix_formats[0]  # Return the first format if the file doesn't exist
        try:
            with open('user_settings', 'r') as f:
                format_str = f.read().strip()
                if format_str in self.prefix_formats:
                    return format_str
        except IOError as e:
            rumps.alert(f"Error loading prefix format: {e}")
        return self.prefix_formats[0]

    def load_prefixes_from_file(self):
        try:
            with open('prefix_list', 'r') as file:
                prefixes = [line.strip() for line in file.readlines()]
        except IOError as e:
            raise Exception(f"Error reading file: 'prefix_list'")
        return prefixes

class WeeNu(rumps.App):
    def __init__(self):
        super(WeeNu, self).__init__("WeeNu")
        self.prefix_formatter = PrefixFormatter()

        self.menu = ["WeeNu v0.2", None]

        self.format_menu = rumps.MenuItem("Prefix")
        for format_option in self.prefix_formatter.prefix_formats:
            menu_item = rumps.MenuItem(format_option, callback=self.change_prefix_format)
            menu_item.state = format_option == self.prefix_formatter.current_format
            self.format_menu.add(menu_item)

        self.menu.add(self.format_menu)
        self.menu.add(None)
        self.github_link_item = rumps.MenuItem("About WeeNu", callback=self.open_github)
        self.menu.add(self.github_link_item)

        self.update_title()

    @rumps.timer(60)
    def update_title(self, _=None):
        week_number = get_week_number()
        self.title = self.prefix_formatter.format_with_week(week_number)

    def change_prefix_format(self, sender):
        literal_format = sender.title
        self.prefix_formatter.save_format(literal_format)
        for item in self.format_menu.values():
            item.state = item.title == literal_format
        self.update_title()

    def open_github(self, _):
        webbrowser.open('https://github.com/mullweisser/mac-weenu')

if __name__ == "__main__":
    WeeNu().run()