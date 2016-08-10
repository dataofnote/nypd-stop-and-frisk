# NYPD Stop and Frisk Database



## Notes


### Year 2006

The 2006 data file has many cleanliness issues.

#### detailCM column missing

Doing a quick frequency count shows that instead of `detailCM`, the 2006 data has two identical columns -- `detail1_` and `details_` -- that seem to share the same kind of values as the `detailCM` columns in all the other years.


```sh
csvcut -c \
    detail1_ data/fetched/nypd-stop-and-frisk/csv/2006.csv \
    | sort | uniq -c | sort -rn | head -n 10
```


#### wepfound column

No other year has a `wepfound` column. So we omit it from the compiled file.
