from __future__ import annotations

import typing as t
from dataclasses import dataclass, field

from Levenshtein import distance, ratio
from nltk.tokenize import word_tokenize
from nltk.translate.bleu_score import sentence_bleu
from rouge_score import rouge_scorer

from ragas.metrics.base import Metric

ROUGE_TYPES = t.Literal["rouge1", "rouge2", "rougeL"]


@dataclass
class BLEUScore(Metric):
    weights: list[float] = field(default_factory=lambda: [0.25, 0.25, 0.25, 0.25])
    smoothing_function = None

    @property
    def name(self):
        return "BLEU"

    @property
    def is_batchable(self):
        return True

    def init_model(self):
        ...

    def score(self, ground_truth: t.List[str], generated_text: t.List[str]):
        ground_truth_ = [[word_tokenize(text)] for text in ground_truth]
        generated_text_ = [word_tokenize(text) for text in generated_text]
        return [
            sentence_bleu(
                s1,
                s2,
                weights=self.weights,
                smoothing_function=self.smoothing_function,
            )
            for s1, s2 in zip(ground_truth_, generated_text_)
        ]


@dataclass
class ROUGE(Metric):
    type: t.Literal[ROUGE_TYPES]
    use_stemmer: bool = False

    def init_model(self):
        self.scorer = rouge_scorer.RougeScorer(
            [self.type], use_stemmer=self.use_stemmer
        )

    @property
    def name(self):
        return self.type

    @property
    def is_batchable(self):
        return False

    def score(
        self, ground_truths: list[str], generated_texts: list[str]
    ) -> list[float]:
        scores = [
            self.scorer.score(ground_truth, generated_texts[i])[self.type].fmeasure
            for i, ground_truth in enumerate(ground_truths)
        ]
        return scores


@dataclass
class EditScore(Metric):
    measure: t.Literal["distance", "ratio"] = "ratio"

    @property
    def name(self) -> str:
        return f"edit_{self.measure}"

    @property
    def is_batchable(self):
        return True

    def init_model(self):
        ...

    def score(self, ground_truth: t.List[str], generated_text: t.List[str]):
        if self.measure == "distance":
            score = [distance(s1, s2) for s1, s2 in zip(ground_truth, generated_text)]
        elif self.measure == "ratio":
            score = [ratio(s1, s2) for s1, s2 in zip(ground_truth, generated_text)]
        else:
            raise ValueError(f"Unkown measure {self.measure}")

        return score


rouge1 = ROUGE("rouge1")
rouge2 = ROUGE("rouge2")
rougeL = ROUGE("rougeL")
bleu_score = BLEUScore()
edit_distance = EditScore("distance")
edit_ratio = EditScore("ratio")
