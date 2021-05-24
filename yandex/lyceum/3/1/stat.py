import statistics


def print_statistics(arr):
    print(
        len(arr),
        *map(
            float,
            (
                statistics.mean(arr),
                min(arr),
                max(arr),
                statistics.median(arr),
            ),
        )
        if arr
        else [0] * 4,
        sep="\n"
    )
