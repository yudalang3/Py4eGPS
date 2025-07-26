def sort_dict_by_value(d: dict[str, int], top_n: int = None) -> list[tuple[str, int]]:
    top3 = sorted(d.items(), key=lambda x: x[1], reverse=True)[:top_n]
    return top3


if __name__ == "__main__":
    d = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
    print(sort_dict_by_value(d, 10))
