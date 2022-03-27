from tkinter import *


def __prettify_dict__(dictionary):
    prettified_dict = ""
    for value in dictionary.items():
        print(value)
        prettified_dict += "{:<10}: {:<4}\n".format(f"<{value[0]}>", str(value[1]))
    return prettified_dict


class GUI:
    def __init__(self, get_url_data, view_url_data):
        self.__get_url_data__ = get_url_data
        self.__view_url_data__ = view_url_data

        window = Tk()

        get_btn = Button(window, text='Load', command=self.on_load_click)
        view_btn = Button(window, text='View', command=self.on_view_click)
        site_input = Entry(width=100)
        status_label = Text(height=15, wrap=WORD)
        self.__site_input__ = site_input
        self.__status_label__ = status_label

        site_input.pack()
        get_btn.pack()
        view_btn.pack()
        status_label.pack()

        window.mainloop()

    def put_dict_to_text(self, dictionary):
        self.__status_label__.delete('1.0', END)
        self.__status_label__.insert(INSERT, __prettify_dict__(dictionary))

    def on_load_click(self):
        url_or_alias = self.__site_input__.get()
        dictionary = self.__get_url_data__(url_or_alias)
        self.put_dict_to_text(dictionary)

    def on_view_click(self):
        url_or_alias = self.__site_input__.get()
        url_data = self.__view_url_data__(url_or_alias)
        self.put_dict_to_text(url_data[3])
