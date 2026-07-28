import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, GLib
import subprocess
import os

ICON_PATH = "/system/assets/bergo_icon.png"
IMAGE_PATH = "/system/bergo_os.img"   # Dein Image
TARGET_DEVICE = "/dev/sdX"            # Ziel (später dynamisch machen)

class FlasherTab(Gtk.Box):
    def __init__(self):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        self.set_margin_top(20)
        self.set_margin_bottom(20)
        self.set_margin_start(20)
        self.set_margin_end(20)

        self._setup_css()

        title = Gtk.Label(label="Bergo Flasher")
        title.add_css_class("flasher-title")

        self.progress = Gtk.ProgressBar()
        self.progress.set_show_text(True)
        self.progress.set_text("Bereit zum Flashen")

        self.status_label = Gtk.Label(label="Kein Vorgang aktiv.")
        self.status_label.add_css_class("flasher-status")

        self.flash_button = Gtk.Button(label="Image auf Gerät flashen")
        self.flash_button.add_css_class("flasher-button")
        self.flash_button.connect("clicked", self.on_flash_clicked)

        self.append(title)
        self.append(self.progress)
        self.append(self.status_label)
        self.append(self.flash_button)

    def _setup_css(self):
        css = Gtk.CssProvider()
        css_data = f"""
        .flasher-bg {{
            background-image: url('{ICON_PATH}');
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
        }}
        .flasher-title {{
            font-size: 24px;
            font-weight: bold;
            color: #FFA500;
        }}
        .flasher-status {{
            color: #FFFFFF;
            font-size: 12px;
        }}
        .flasher-button {{
            background-color: #FFA500;
            color: #000000;
            font-weight: bold;
        }}
        """
        css.load_from_data(css_data.encode("utf-8"))
        Gtk.StyleContext.add_provider_for_display(
            Gtk.Display.get_default(),
            css,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )
        self.get_style_context().add_class("flasher-bg")

    def on_flash_clicked(self, _button):
        if not os.path.exists(IMAGE_PATH):
            self.status_label.set_text("❌ Image nicht gefunden.")
            return

        self.status_label.set_text("🚀 Flash-Vorgang gestartet...")
        self.progress.set_text("Flash läuft...")
        self.progress.set_fraction(0.0)

        # Hier sehr einfache dd-Nutzung – später sicherer machen!
        cmd = [
            "pkexec", "dd",
            f"if={IMAGE_PATH}",
            f"of={TARGET_DEVICE}",
            "bs=4M",
            "status=progress",
            "conv=fsync"
        ]

        try:
            subprocess.Popen(cmd)
        except Exception as e:
            self.status_label.set_text(f"❌ Fehler: {e}")
            return

        # Dummy-Progress (nur optisch)
        GLib.timeout_add(300, self._pulse_progress)

    def _pulse_progress(self):
        current = self.progress.get_fraction()
        if current < 0.95:
            self.progress.set_fraction(current + 0.02)
            return True
        else:
            self.progress.set_fraction(1.0)
            self.progress.set_text("✅ Flash abgeschlossen")
            self.status_label.set_text("Fertig – Gerät kann entfernt werden.")
            return False


if __name__ == "__main__":
    app = Gtk.Application()

    def on_activate(app):
        win = Gtk.ApplicationWindow(application=app)
        win.set_title("Bergo Flasher Tab Test")
        win.set_default_size(600, 400)
        tab = FlasherTab()
        win.set_child(tab)
        win.present()

    app.connect("activate", on_activate)
    app.run()
