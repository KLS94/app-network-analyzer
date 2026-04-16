from analyzer import classify_event

def process_file(filename):
    counts = {}

    with open(filename, "r") as file:
        for line in file:
            url = line.strip()
            event = classify_event(url)

            counts[event] = counts.get(event, 0) + 1

            print(f"{url} -> {event}")

    print("\nSummary:")
    for event, count in counts.items():
        print(f"{event}: {count}")


if __name__ == "__main__":
    process_file("sample_data.txt")
