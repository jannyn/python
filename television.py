class Television:
    """
    class that represents a TV's settings
    """
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """
        method which sets the default settings of the TV
        """
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        method that sets the TV to either off or on
        """
        if self.__status:
            self.__status = False
        else:
            self.__status = True

    def mute(self) -> None:
        """
        method that either mutes or unmutes the TV
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            else:
                self.__muted = True

    def channel_up(self) -> None:
        """
        method that switches the TV channel to one channel value higher
        """
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """
        method that switches the TV channel to one channel value lower
        """
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        """
        method that turns up the TV volume by 1
        """
        if self.__status:
            if self.__volume != Television.MAX_VOLUME:
                self.__volume += 1
                self.__muted = False

    def volume_down(self) -> None:
        """
        method that turns down the TV volume by 1
        """
        if self.__status:
            if self.__volume != Television.MIN_VOLUME:
                self.__volume -= 1
                self.__muted = False

    def __str__(self) -> str:
        """
        method that prints out the current TV settings
        :return: the TV's current settings
        """
        if self.__muted:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'

