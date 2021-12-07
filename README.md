# pyqt-show-button-when-hover-widget
PyQt show the button to the bottom right of the widget when mouse cursor hover

## Overview
<b>This package is for the one who needs tutorial or example. Examine the code whatever you want.</b>

Base widget is QGraphicsView. 

When mouse cursor hover on the widget addBtn(plus icon, QPushButton type) and delBtn(minus icon) will be appeared.

You can show image on the QGraphicsView by clicking addBtn and select the image file.

If image file is shown, you can delete it by clicking delBtn.

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

https://user-images.githubusercontent.com/55078043/144965498-637807de-4dce-423a-a509-d26ce1c39bcc.mp4



