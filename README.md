# ekonomy_ai
Scripts and experiments for stock analysis etc

``` bash
git clone git@github.com:nakceb/ekonomy_ai.git
cd scripts
./install.sh
```

## Example usage:

``` python
from alpha_vantage.alpha_vantage import AlphaVantage, IntervalOptions, SliceOptions, OutputSizeOptions
# Get your API key from: https://www.alphavantage.co/support/#api-key
alpha_vantage = AlphaVantage(api_key='<paste_your_api_key>') 
# Use wrapped methods, ex:
ts_df, meta_data = alpha_vantage.time_series_daily(symbol='IBM', outputsize=OutputSizeOptions.full)
print(ts_df)
```
