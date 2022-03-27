import argparse


def __prettify_dict__(dictionary):
    prettified_dict = ""
    for value in dictionary.items():
        prettified_dict += "{:<12}: {:<4}\n".format(f"<{value[0]}>", str(value[1]))
    return prettified_dict


class Console:
    def __init__(self, get_url_data, view_url_data):
        self.__get_url_data__ = get_url_data
        self.__view_url_data__ = view_url_data

        parser = argparse.ArgumentParser(prog='tagcounter', description='Counts tags on website', add_help=False)
        parser.add_argument('--view', nargs=1, type=str, )
        parser.add_argument('--get', nargs=1, type=str, )
        args = parser.parse_args()

        if args.view is not None and args.get is not None:
            raise GeneratorExit('Only one argument is allowed')

        if args.view is not None:
            self.on_view(args.view[0])

        if args.get is not None:
            self.on_get(args.get[0])

    def on_get(self, url_or_alias):
        dictionary = self.__get_url_data__(url_or_alias)
        print(__prettify_dict__(dictionary))

    def on_view(self, url_or_alias):
        url_data = self.__view_url_data__(url_or_alias)
        if url_data is None:
            print('Nothing found')
            return

        dictionary = url_data[3]
        print(__prettify_dict__(dictionary))
