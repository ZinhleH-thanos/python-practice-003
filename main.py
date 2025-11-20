def weather_graph():
    """
    This function draws a weather graph for four weeks.
    each week will be observing a specific attribute.
    WEEK 1: RAIN 🌧️ , WEEK 2: CLOUDS ☁️, WEEK 3: WIND 🍃, WEEK 4: SUN ☀️
    
    Returns:
        str: A string representation of the weather graph.
        
    i.e for RAIN: each character represents 10% of rain/attribute observed that day.
    0% - no character
    10% - 1 character
    20% - 2 characters
    ...
    
    Week 1: RAIN
    MON: 🌧️
    TUE: 🌧️🌧️🌧️🌧️🌧️
    WED: 🌧️🌧️🌧️
    THU: 🌧️🌧️🌧️🌧️
    FRI: 🌧️🌧️🌧️🌧️🌧️
    
    your task is to read data from a file 'weather.txt' and draw the graphs accordingly.
    """
        if len(sys.argv) < 2:
        print("Please input/type valid file path")
        sys.exit(1)

    graph = []
    week_headers = ["WEEK 1: RAIN 🌧️", "WEEK 2: CLOUDS ☁️", "WEEK 3: WIND 🍃", "WEEK 4: SUN ☀️"]
    emojis = ["🌧️", "☁️", "🍃", "☀️"]
    week_count = 0
    week_header_printed = False

    with open(file_path, "r") as f:
        lines = f.readlines()

        for line in lines:
            line = line.strip()
            if line == "":
                continue

            if line == "---":
                week_count += 1
                week_header_printed = False
                continue

            if ":" not in line:
                continue

            if not week_header_printed:
                print(week_headers[week_count])
                week_header_printed = True

            parts = line.split(": ")
            if len(parts) != 2:
                continue

            day = parts[0]
            value = int(parts[1])

            emoji_count = value // 10
            line_graph = emojis[week_count] * emoji_count

            print(f"{day}: {line_graph}")

            graph.append(value)

    return graph

weather_graph(sys.argv[1])
     
