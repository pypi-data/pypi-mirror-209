from attr import define, field, Factory
from griptape.drivers import OpenAiPromptDriver
from griptape.tokenizers import TiktokenTokenizer


@define
class TextChunker:
    separator: str = field(default="\n\n", kw_only=True)
    tokenizer: TiktokenTokenizer = field(default=OpenAiPromptDriver(), kw_only=True)
    max_tokens_per_chunk: int = field(
        default=Factory(lambda self: self.tokenizer.max_tokens, takes_self=True),
        kw_only=True
    )

    def chunk(self, string: str) -> list[str]:
        initial_chunks = string.split(self.separator)
        final_chunks = []

        for chunk in initial_chunks:
            if self.tokenizer.token_count(chunk) > self.max_tokens_per_chunk:
                final_chunks.extend(self.recursive_chunk(chunk))
            else:
                final_chunks.append(chunk)

        return final_chunks

    def recursive_chunk(self, string: str) -> list[str]:
        token_count = self.tokenizer.token_count(string)

        if token_count <= self.max_tokens_per_chunk:
            return [string]
        else:
            best_split_index = -1
            best_split_diff = float("inf")
            tokens_count = 0
            split_string = string.split()

            for index, word in enumerate(split_string):
                tokens_count += self.tokenizer.token_count(word)
                current_diff = abs(self.max_tokens_per_chunk - tokens_count)

                if current_diff < best_split_diff:
                    best_split_index = index
                    best_split_diff = current_diff

            first_chunk = " ".join(split_string[: best_split_index + 1]).strip()
            second_chunk = " ".join(split_string[best_split_index + 1:]).strip()

            return self.recursive_chunk(first_chunk) + self.recursive_chunk(second_chunk)