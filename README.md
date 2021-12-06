# pyqt-show-button-when-hover-widget
PyQt show the button to the bottom right of the widget when mouse cursor hover

## Requirements
PyQt5 >= 5.8

## Setup
``` pip3 install git+https://github.com/yjg30737/pyqt-show-button-when-hover-widget.git --upgrade```

## Example
Code Example
```python
from PyQt5.QtWidgets import QApplication
from pyqt_show_button_when_hover_widget import ShowButtonWhenHoverWidget

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    dialog = ShowButtonWhenHoverWidget()
    dialog.show()
    sys.exit(app.exec_())
```

## Result
I will upload this after 4 hours or some sort. Kinda busy :(
