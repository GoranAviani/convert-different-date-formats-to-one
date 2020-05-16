import dateutil.parser
def main():
    result = []
    dates = ["2020-05-01", "June 1 1980", "12/15/2017", "12-25-2000"]
    for date in dates:
        fixed_date = dateutil.parser.parse(date).strftime("%Y-%m-%d")
        result.append(fixed_date)

    print(result)



if __name__ == "__main__":
    main()


