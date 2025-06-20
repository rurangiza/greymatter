class CompletionError(Exception):
    def __init__(self, cause) -> None:
        self.message = f"Completion Failed. Cause: {cause}"
        super().__init__(self.message)


class StreamingError(Exception):
    def __init__(self, cause) -> None:
        self.message = f"Streaming Failed. Cause: {cause}"
        super().__init__(self.message)


class UnexpectedFinishReason(Exception):
    def __init__(self, finish_reason) -> None:
        self.message = f"Unexpected finish reason while streaming: {finish_reason}"
        super().__init__(self.message)
