class printer():
    _colors_ = {
        **dict.fromkeys(("RED", "ERROR", "NO"), "\033[1;31m"),
        **dict.fromkeys(("GREEN", "OK", "YES"), "\033[0;32m"),
        **dict.fromkeys(("YELLOW", "WARN", "MAYBE"), "\033[0;93m"),
        "BLUE": "\033[1;34m",
        "CYAN": "\033[1;36m",
        "RESET": "\033[0;0m",
        "BOLD": "\033[;1m",
        "REVERSE": "\033[;7m"
    }

    def _get_color_(self, key):
        """Gets the corresponding color ANSI code... """
        try:
            return self._colors_[key]
        except:
            return self._colors_["RESET"]

    def print(self, msg, color="RESET", saltarlinha="null"):
        """Main print function..."""

        # Get ANSI color code.
        color = self._get_color_(key=color)

        # Printing...
        if saltarlinha == "1x":
            print("{}{}{}".format(color, msg, self._colors_["RESET"]))
        elif saltarlinha == "2x":
            print("{}{}{}".format(color, msg, self._colors_["RESET"]), end='\n\n')
        else:
            print("{}{}{}".format(color, msg, self._colors_["RESET"]), end='')
