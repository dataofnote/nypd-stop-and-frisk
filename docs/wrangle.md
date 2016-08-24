# Things cleaned

- windows text format to utc
- fields that should be Y/N, changing 1 to Y
- fixing wonky headers in 2006
- renaming headers to more human readable versions
- converting xcoord,ycoord to longitude latitude
- 


# Finding enumerate values


```sh
  cat wrangle/corral/homogenized/*.csv \
    | csvcut -c  \
    | ack ',,|[^,YN\n]'
```

```sh
ls wrangle/corral/homogenized/*.csv | while read -r fname; do
  echo $fname
  csvcut -c additional_details,additional_reports,arrest_made\
      $fname \
    | csvformat -T \
    | sed '1d' \
    | tr '\t' '\n' \
    | sort | uniq -c
done
```


```sh
ls wrangle/corral/homogenized/*.csv | while read -r fname; do
(>&2 echo "$fname")
  csvcut -c additional_details,additional_reports,arrest_made\
      $fname \
    | csvformat -T \
    | sed '1d' \
    | tr '\t' '\n' \
    | sort | uniq -c
done
```


```sh

tr ',' '\n' < wrangle/scripts/etc/headers_homogenized.txt \
  | while read -r field; do
  (>&2 echo "  Field: $field")
    ls wrangle/corral/homogenized/*.csv | while read -r fname; do
      (>&2 echo "      - $fname")
      csvcut -c "$field" "$fname"
    done
done

ls wrangle/corral/homogenized/*.csv | while read -r fname; do
  (>&2 echo "\t$fname")
  csvcut -c additional_details,additional_reports,arrest_made\
      $fname \
    | csvformat -T \
    | sed '1d' \
    | tr '\t' '\n' \
    | sort | uniq -c
done
```






# arrest_offense
# assault_weapon
# complaint_precinct
# complaint_year
