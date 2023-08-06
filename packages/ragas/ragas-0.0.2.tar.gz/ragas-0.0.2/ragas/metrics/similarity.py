from __future__ import annotations

import typing as t
from dataclasses import dataclass

import numpy as np
from numpy.linalg import norm
from sentence_transformers import SentenceTransformer

from ragas.metrics.base import Metric

BERT_METRIC = t.Literal["cosine", "euclidean"]


@dataclass
class BERTScore(Metric):
    similarity_metric: t.Literal[BERT_METRIC] = "cosine"
    model_path: str = "all-MiniLM-L6-v2"
    batch_size: int = 1000

    def init_model(self):
        self.model = SentenceTransformer(self.model_path)

    @property
    def name(
        self,
    ):
        return f"BERTScore_{self.similarity_metric}"

    @property
    def is_batchable(self):
        return True

    def score(
        self,
        ground_truth: list[str],
        generated_text: list[str],
    ):
        gndtruth_emb = self.model.encode(
            ground_truth, batch_size=self.batch_size, convert_to_numpy=True
        )
        gentext_emb = self.model.encode(
            generated_text, batch_size=self.batch_size, convert_to_numpy=True
        )
        assert isinstance(gentext_emb, np.ndarray) and isinstance(
            gndtruth_emb, np.ndarray
        ), (
            f"Both gndtruth_emb[{type(gentext_emb)}], gentext_emb[{type(gentext_emb)}]"
            " should be numpy ndarray."
        )

        if self.similarity_metric == "cosine":
            score = np.sum(gndtruth_emb * gentext_emb, axis=1) / (
                norm(gndtruth_emb, axis=1) * norm(gentext_emb, axis=1)
            )

        elif self.similarity_metric == "euclidean":
            score = norm(gndtruth_emb - gentext_emb, ord=2)

        else:
            raise ValueError(f"Unkown metrics {self.similarity_metric}")

        return score


bert_score = BERTScore()
