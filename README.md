# Getting stock quotes from public sources

A simple module to retrieve stock quotes from public sources. The current version uses WSJ.com to get the last price of the stock, it's intraday high, low and volume.

I created the module to be used few minutes after the market close, not sure if it works properly during trading sessions.

Since the WSJ.com site does not provide the opening price, the module returns 0 as the opening price.

Should you want to add another public sources, feel free to create a new pull request.
