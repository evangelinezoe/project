

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.slider import Slider
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
from kivy.uix.label import Label

# Define a custom widget to display the current color
class ColorDisplay(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            self.color = Color(1, 1, 1, 1)
            self.rect = Rectangle(pos=self.pos, size=self.size)
        self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def set_color(self, r, g, b):
        self.color.rgb = (r, g, b)

# Main application class
class ColorMixerApp(App):
    def build(self):
        self.title = "Color Mixer"

        # Main vertical layout
        main_layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        # Color display widget
        self.color_display = ColorDisplay(size_hint=(1, 0.6))
        main_layout.add_widget(self.color_display)

        # Sliders layout
        sliders_layout = BoxLayout(orientation='vertical', spacing=10)

        # --- Red slider and label ---
        self.red_slider = Slider(min=0, max=1, value=1)
        self.red_value_label = Label(text='100%', size_hint_x=0.2)
        self.red_slider.bind(value=self.update_red_label)
        sliders_layout.add_widget(self.create_slider_box('Red', self.red_slider, self.red_value_label))

        # --- Green slider and label ---
        self.green_slider = Slider(min=0, max=1, value=1)
        self.green_value_label = Label(text='100%', size_hint_x=0.2)
        self.green_slider.bind(value=self.update_green_label)
        sliders_layout.add_widget(self.create_slider_box('Green', self.green_slider, self.green_value_label))

        # --- Blue slider and label ---
        self.blue_slider = Slider(min=0, max=1, value=1)
        self.blue_value_label = Label(text='100%', size_hint_x=0.2)
        self.blue_slider.bind(value=self.update_blue_label)
        sliders_layout.add_widget(self.create_slider_box('Blue', self.blue_slider, self.blue_value_label))

        # Add sliders layout to main layout
        main_layout.add_widget(sliders_layout)

        # Initialize color display
        self.update_color()

        return main_layout

    def create_slider_box(self, label_text, slider, value_label):
        box = BoxLayout(size_hint_y=None, height=40, spacing=10)
        label = Label(text=label_text, size_hint_x=0.2)
        box.add_widget(label)
        box.add_widget(slider)
        box.add_widget(value_label)
        return box

    def update_red_label(self, instance, value):
        self.red_value_label.text = f'{int(value * 100)}%'
        self.update_color()

    def update_green_label(self, instance, value):
        self.green_value_label.text = f'{int(value * 100)}%'
        self.update_color()

    def update_blue_label(self, instance, value):
        self.blue_value_label.text = f'{int(value * 100)}%'
        self.update_color()

    def update_color(self, *args):
        r = self.red_slider.value
        g = self.green_slider.value
        b = self.blue_slider.value
        self.color_display.set_color(r, g, b)

# Run the app
if __name__ == '__main__':
    ColorMixerApp().run()