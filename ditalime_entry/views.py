import tkinter as tk
from . import widgets as w


class DataMetaRecordForm(tk.Frame):
    """The input form for mete record form"""

    def __init__(self, parent, fields, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # A dict to keep track of input widgets
        self.inputs = {}

        # Build the form
        # recordinfo section
        recordinfo = tk.LabelFrame(self)

        self.inputs["topic"] = w.LabelInput(
            recordinfo, "Topic",
            field_spec=fields["topic"]
        )
        # Default value
        self.inputs["topic"].set("concept")
        self.inputs["topic"].grid(row=1, column=0)

        recordinfo.grid(row=0, column=0, sticky="ew")

    def get(self):
        """Retrieve data from form as a dict"""

        # We need to retrieve the data from Tkinter variables
        # and place it in regular Python objects

        data = {}
        for key, widget in self.inputs.items():
            data[key] = widget.get()
        return data


class DataRecordForm(tk.Frame):
    """The input form for our widgets"""

    def __init__(self, parent, fields, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # A dict to keep track of input widgets
        self.inputs = {}

        # Build the form
        # recordinfo section
        recordinfo = tk.LabelFrame(self, text="Record Information")

        # Contents section
        self.inputs["contents"] = w.LabelInput(
            self, "Contents",
            field_spec=fields["contents"],
            input_args={"width": 100, "height": 20}
        )
        self.inputs["contents"].grid(sticky="w", row=2, column=0)
        recordinfo.grid(row=3, column=0, sticky="ew")

    def get(self):
        """Retrieve data from form as a dict"""

        # We need to retrieve the data from Tkinter variables
        # and place it in regular Python objects

        data = {}
        for key, widget in self.inputs.items():
            data[key] = widget.get()
        return data

    def set_from_template(self, template):
        """Update value from the template"""
        self.inputs["contents"].set(template)
