def convert_to_preferred_format(sec):
    """
    Функция переводит секунды в года, месяцы, дни, часы, минуты, секунды в формате
    1 hour, 1 minute and 2 seconds
    """
    words = ["year", "day", "hour", "minute", "second"]

    if not sec:
        return "now"
    else:
        m, s = divmod(sec, 60)
        h, m = divmod(m, 60)
        d, h = divmod(h, 24)
        y, d = divmod(d, 365)

        time = [y, d, h, m, s]

        duration = []

        for x, i in enumerate(time):
            if i == 1:
                duration.append(f"{i} {words[x]}")
            elif i > 1:
                duration.append(f"{i} {words[x]}s")

        if len(duration) == 1:
            return duration[0]
        elif len(duration) == 2:
            return f"{duration[0]} and {duration[1]}"
        else:
            return ", ".join(duration[:-1]) + " and " + duration[-1]


print(convert_to_preferred_format(3662))
