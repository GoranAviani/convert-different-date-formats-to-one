import dateutil.parser
def main():
    result = []
    dates = ["2020-05-01", "June 1 1980", "12/15/2017", "12-25-2000",
             "23/1/99", "24/7/1999", "2/13/78", "02/05/88",
             "01/04/65", "1/4/66"]
    #TODO parser displyas 60' as 2060
    for date in dates:
        fixed_date = dateutil.parser.parse(date).strftime("%Y-%m-%d")
        result.append(fixed_date)

    print(result)



if __name__ == "__main__":
    main()


