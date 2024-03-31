import rumps
from datetime import datetime
import webbrowser
import os
from update_check import isUpToDate
import json

def get_week_number():
    today = datetime.now()
    week_number = today.isocalendar()[1]
    return week_number

class SettingsManager:
    def __init__(self, settings_file='user_settings.json'):
        self.settings_file = settings_file
        self.settings = self.load_settings()

    def load_settings(self):
        if os.path.exists(self.settings_file):
            try:
                with open(self.settings_file, 'r') as f:
                    return json.load(f)
            except IOError as e:
                print(f"Error loading settings: {e}")
        return {}

    def save_settings(self):
        try:
            with open(self.settings_file, 'w') as f:
                json.dump(self.settings, f, indent=4)
        except IOError as e:
            print(f"Error saving settings: {e}")

    def get_setting(self, key, default=None):
        return self.settings.get(key, default)

    def update_setting(self, key, value):
        self.settings[key] = value
        self.save_settings()

class PrefixFormatter:
    def __init__(self):
        self.sm = SettingsManager()
        self.prefix_formats = self.load_prefixes_from_file()
        self.current_format = self.load_format()  # Ensure current format is correctly loaded

    def format_with_week(self, week_number):
        self.current_format_formatted = f"{self.current_format} {week_number}"
        return self.current_format_formatted

    def save_format(self, format_str):
        try:
            self.sm.update_setting('current_prefix', format_str)
            self.current_format = format_str  # Update current format immediately
        except IOError as e:
            rumps.alert(f"Error saving current prefix format: {e}")

    def load_format(self):
        # Properly load and return the current format
        format_str = self.sm.get_setting('current_prefix', self.prefix_formats[0])
        self.current_format = format_str  # Ensure current format is updated here
        return format_str

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
        self.settings_manager = SettingsManager()

        self.menu = ["WeeNu v0.2", None]

        self.format_menu = rumps.MenuItem("Prefix")
        for format_option in self.prefix_formatter.prefix_formats:
            menu_item = rumps.MenuItem(format_option, callback=self.change_prefix_format)
            menu_item.state = format_option == self.prefix_formatter.current_format
            self.format_menu.add(menu_item)
        self.menu.add(self.format_menu)
        
        settings_menu = rumps.MenuItem('Update checks')
        auto_check_updates = rumps.MenuItem("Enable", callback=self.toggle_auto_update)
        auto_update_check_setting = self.settings_manager.get_setting('auto_update_check', False)
        auto_check_updates.state = auto_update_check_setting
        settings_menu.add(auto_check_updates)
        settings_menu.add(None)
        check_version_item = rumps.MenuItem("Check now", callback=lambda _: self.check_version(manual_mode=True))
        settings_menu.add(check_version_item)
        
        self.menu.add(settings_menu)
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
        
    def check_version(self, _=None, manual_mode=False):
        is_latest = isUpToDate('version', "https://raw.githubusercontent.com/mullweisser/mac-weenu/main/version")
        if is_latest and manual_mode:
            rumps.notification(title="WeeNu", subtitle="", message="You are running the latest version.", sound=False)
        elif not is_latest:
            rumps.notification(title="WeeNu", subtitle="", message="Newer version is available.", sound=False)
    
    def toggle_auto_update(self, sender):
        new_state = not sender.state
        sender.state = new_state
        self.settings_manager.update_setting('auto_update_check', new_state)
        if new_state:
            self.check_version()
    
    @rumps.timer(86400)
    def auto_check_version(self, _=None):
        if self.settings_manager.get_setting('auto_update_check', False):
            self.check_version(manual_mode=False)

if __name__ == "__main__":
    app = WeeNu()
    app.run()