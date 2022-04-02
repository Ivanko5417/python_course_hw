from tkinter import *
import time


def __prettify_dict__(dictionary):
    prettified_dict = ""
    for value in dictionary.items():
        prettified_dict += "{:<12}: {:<4}\n".format(f"<{value[0]}>", str(value[1]))
    return prettified_dict


class GUI:
    def __init__(self, get_url_data, view_url_data):
        self.__get_url_data__ = get_url_data
        self.__view_url_data__ = view_url_data

        window = Tk()

        get_btn = Button(window, text='Load', command=self.on_load_click)
        view_btn = Button(window, text='View', command=self.on_view_click)
        site_input = Entry(width=100)
        result_input = Text(height=15, wrap=WORD)
        status_label_text = StringVar()
        status_label = Label(height=15, textvariable=status_label_text)

        self.__site_input__ = site_input
        self.__result_input__ = result_input
        self.__status_label_text__ = status_label_text

        site_input.pack()
        get_btn.pack()
        view_btn.pack()
        result_input.pack()
        status_label.pack()

        window.mainloop()

    def put_dict_to_text(self, dictionary):
        self.__result_input__.delete('1.0', END)
        self.__result_input__.insert(INSERT, __prettify_dict__(dictionary))

    def on_load_click(self):
        start_time = time.time()
        url_or_alias = self.__site_input__.get()
        try:
            dictionary = self.__get_url_data__(url_or_alias)
            self.put_dict_to_text(dictionary)
            self.__status_label_text__.set(f'Loading finished successfully. Execution time = {round(time.time() - start_time, 2)} seconds')
        except BaseException:
            self.__status_label_text__.set('Error occurred during loading')

    def on_view_click(self):
        url_or_alias = self.__site_input__.get()
        try:
            url_data = self.__view_url_data__(url_or_alias)
            if url_data is None:
                self.__result_input__.delete('1.0', END)
                self.__status_label_text__.set('Nothing found')
                return
            self.put_dict_to_text(url_data[3])
            self.__status_label_text__.set('Viewing finished successfully')
        except BaseException:
            self.__status_label_text__.set('Error occurred viewing loading')

