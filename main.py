import re

def main():
    print("hello world")
    input_filepath = r"C:\Users\cianj\Downloads\Revolut-EUR-Statement-Oct 2018–Mar2019"
    output_filepath = input_filepath + "_fixed.csv"
    input_filepath = input_filepath + ".csv"
    with open(input_filepath, encoding="utf8") as revolut_statement:
        full_statement = revolut_statement.readlines()

    regex = re.compile(r"( +)?;( +)?")
    output_statement = []
    for line in full_statement:
        line = line.replace(",", "")
        output_statement.append(regex.sub(",", line))

        # regex = ( +)?;( +)?
    with open(output_filepath, "w", encoding="utf8") as fixed_statement:
        for line in output_statement:
            fixed_statement.write(line)

    print(output_statement)


if __name__ == "__main__":
    main()
