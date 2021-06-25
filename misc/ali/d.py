print(
    "".join(
        sorted(
            set("qwertyuiopasdfghjklzxcvbnm")
            - set(input() + input() + input())
        )
    )
)
