class OrderedStream:

    def __init__(self, n: int):
        self.stream = [""] * (n + 1)
        self.ptr = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        stream = self.stream

        stream[idKey] = value
        res = list()
        while self.ptr < len(stream) and stream[self.ptr]:
            res.append(stream[self.ptr])
            self.ptr += 1

        return res