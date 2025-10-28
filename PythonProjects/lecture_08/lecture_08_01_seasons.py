"""
This is CS50P Seasons of Love. We’ll:
read a date of birth in YYYY-MM-DD
compute how many minutes from that midnight to today’s midnight
print the amount in English words (no “and”), e.g.,
Five hundred twenty-five thousand, six hundred minutes
We’ll use datetime.date for dates and the inflect package to spell numbers.


"""
# pip install inflect


from datetime import date
import sys
import inflect


def parse_iso_date_or_exit(s: str) -> date:
    # date got from YYYY-MM-DD, sys.exit on bad input
    try:
        return date.fromisoformat(s)
    except ValueError:
        sys.exit('Invalid date')


def minutes(start: date, end: date) -> int:
    # both starting from midnight
    delta_days = (end - start).days
    return round(delta_days * 24 * 60)


def to_english(n: int) ->str:
    p = inflect.engine()
    words = p.number_to_words(n, andword='')  # no and, use''
    return f'{words.capitalize()} minutes'


def main():
    s = input('Date of Birth: ')
    birthday = parse_iso_date_or_exit(s)
    mins = minutes(birthday, date.today())
    print(to_english(mins))


if __name__ == '__main__':
    main()
