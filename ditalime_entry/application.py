import codecs
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from . import models as m
from . import views as v


class Application(tk.Tk):
    """Application root window"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Ditalime - DITA Entry Support Application")
        self.resizable(width=False, height=False)

        # Value Holder for saving filename
        self.filename = tk.StringVar()

        # Topic selection form
        self.meta_recordform = v.DataMetaRecordForm(
            self, m.DitaMetaModel.fields)
        self.meta_recordform.grid(row=1, padx=10)

        self.loadbutton = ttk.Button(
            self, text="Load", command=self.on_load_topic)
        self.loadbutton.grid(sticky="e", row=2, padx=10)

        # Content entry form
        self.recordform = v.DataRecordForm(
            self, m.DitaModel.fields)
        self.recordform.grid(row=3, padx=10)

        self.savebutton = ttk.Button(
            self, text="Save", command=self.on_file_select)
        self.savebutton.grid(sticky="e", row=5, padx=10)

    def on_load_topic(self):
        """Load topic with template"""

        meta_info = self.meta_recordform.get()
        topic_name = meta_info["topic"]

        if topic_name is not None:
            template = self.load_template(topic_name)
            self.recordform.set_from_template(template)

    def load_template(self, topic_name):
        """Read local template contents"""

        base_dir = os.path.dirname(__file__)
        template = base_dir + "/templates/template-" + topic_name + ".md"
        with codecs.open(template, "r", "utf-8") as f:
            return f.read()

    def on_file_select(self):
        """Handle on save action"""

        filename = filedialog.asksaveasfilename(
            title='Select the target file for saving contents',
            defaultextension=".md",
            filetypes=[('Markdown', '*.md *.MD')]
        )
        if filename:
            self.filename.set(filename)
            self.on_save()

    def on_save(self):
        """Write the contents on the file"""

        model = m.DitaModel(self.filename.get())
        data = self.recordform.get()
        model.save_record(data)
