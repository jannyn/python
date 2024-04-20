import pytest
from television import *


class Test:

    def setup_method(self):
        self.tv = Television()

    def teardown_method(self):
        del self.tv

    def test_init(self):
        assert self.tv.__str__() == 'Power = False, Channel = 0, Volume = 0'  # default values

    def test_power(self):
        self.tv.power()
        assert self.tv.__str__() == 'Power = True, Channel = 0, Volume = 0'  # when tv is on
        self.tv.power()
        assert self.tv.__str__() == 'Power = False, Channel = 0, Volume = 0'  # when tv is off

    def test_mute(self):
        self.tv.power()
        self.tv.volume_up()
        self.tv.mute()
        assert self.tv.__str__() == 'Power = True, Channel = 0, Volume = 0'  # when tv is on, volume
        # increase once, and then tv muted

        self.tv.mute()
        assert self.tv.__str__() == 'Power = True, Channel = 0, Volume = 1'  # when the tv is on and unmuted

        self.tv.power()
        self.tv.mute()
        assert self.tv.__str__() == 'Power = False, Channel = 0, Volume = 1'  # when the tv is off and muted

        self.tv.mute()
        assert self.tv.__str__() == 'Power = False, Channel = 0, Volume = 1'  # when the tv is off and unmuted

    def test_channel_up(self):
        self.tv.channel_up()
        assert self.tv.__str__() == 'Power = False, Channel = 0, Volume = 0'  # when tv is off and the channel has
        # been increased

        self.tv.power()
        self.tv.channel_up()
        assert self.tv.__str__() == 'Power = True, Channel = 1, Volume = 0'  # when tv is on and the channel has been
        # increased

        self.tv.channel_up()
        self.tv.channel_up()
        self.tv.channel_up()
        assert self.tv.__str__() == 'Power = True, Channel = 0, Volume = 0'  # when tv is on and channel is increased
        # past the maximum value

    def test_channel_down(self):
        self.tv.channel_down()
        assert self.tv.__str__() == 'Power = False, Channel = 0, Volume = 0'  # when tv is off and the channel has
        # been decreased

        self.tv.power()
        self.tv.channel_down()
        assert self.tv.__str__() == 'Power = True, Channel = 3, Volume = 0'  # when tv is on and the channel has been
        # decreased past the minimum value

    def test_volume_up(self):
        self.tv.volume_up()
        assert self.tv.__str__() == 'Power = False, Channel = 0, Volume = 0'  # when tv is off and the volume has been
        # increased

        self.tv.power()
        self.tv.volume_up()
        assert self.tv.__str__() == 'Power = True, Channel = 0, Volume = 1'  # when the tv is on and the volume has
        # been increased

        self.tv.mute()
        self.tv.volume_up()
        assert self.tv.__str__() == 'Power = True, Channel = 0, Volume = 2'  # when the tv is on, muted, and the
        # volume has been increased

        self.tv.volume_up()
        assert self.tv.__str__() == 'Power = True, Channel = 0, Volume = 2'  # when the tv is on and volume is
        # increased past the maximum value

    def test_volume_down(self):
        self.tv.volume_down()
        assert self.tv.__str__() == 'Power = False, Channel = 0, Volume = 0'  # when tv is off and volume has been
        # decreased

        self.tv.power()
        self.tv.volume_up()
        self.tv.volume_up()
        self.tv.volume_down()
        assert self.tv.__str__() == 'Power = True, Channel = 0, Volume = 1'  # when tv is on and volume has been
        # decreased (volume set to max before decreasing)

        self.tv.mute()
        self.tv.volume_down()
        assert self.tv.__str__() == 'Power = True, Channel = 0, Volume = 0'  # when tv is on, muted, and volume has
        # been decreased

        self.tv.volume_down()
        assert self.tv.__str__() == 'Power = True, Channel = 0, Volume = 0'  # when tv is on and volume is decreased
        # past the minimum value
