import dateutil.parser


THRESHOLD = 2016

def main():
    result = []
    dates = ["2020-05-01", "June 1 1980", "12/15/2017", "12-25-2000",
             "23/1/99", "24/7/1999", "2/13/78", "02/05/88",
             "01/04/65", "1/4/66"]
    for date in dates:
        dt = dateutil.parser.parse(date)
        if dt.year > THRESHOLD:
            dt = dt.replace(year=dt.year - 100)
        result.append(dt.strftime("%Y-%m-%d"))

    print(result)



if __name__ == "__main__":
    main()


