# Copyright (c) 2021 Emanuele Bellocchia
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

#
# Imports
#
from telegram_crypto_price_bot.bot_base import BotBase
from telegram_crypto_price_bot.coin_info_scheduler import CoinInfoScheduler
from telegram_crypto_price_bot.price_bot_config_cfg import PriceBotConfigCfg
from telegram_crypto_price_bot.price_bot_handlers_cfg import PriceBotHandlersCfg


#
# Classes
#

# Price bot class
class PriceBot(BotBase):
    # Constructor
    def __init__(self,
                 config_file: str) -> None:
        super().__init__(config_file,
                         PriceBotConfigCfg,
                         PriceBotHandlersCfg)
        # Initialize coin info scheduler
        self.coin_info_scheduler = CoinInfoScheduler(self.client,
                                                     self.config,
                                                     self.logger,
                                                     self.translator)
