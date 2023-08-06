from __future__ import annotations

import torch
from torch import Tensor
from torch import nn
from torchmetrics.classification import MulticlassAccuracy
from torchmetrics.classification import MulticlassPrecision
from torchmetrics.classification import MulticlassRecall


class MulticlassClassification(nn.Module):
    def __init__(
        self,
        in_channels: int,
        num_classes: int,
        level: int = -1,
        label_weights: list[float] | None = None,
        label_smoothing: float = 0.0,
    ) -> None:
        super().__init__()
        self.num_classes = num_classes
        self.level = level
        self.label_weights = torch.tensor(label_weights) if label_weights else None
        self.label_smoothing = label_smoothing
        self.net = nn.Sequential(
            nn.AdaptiveAvgPool2d(1), nn.Flatten(), nn.Linear(in_channels, num_classes)
        )

    def forward(self, inputs: list[Tensor]) -> tuple[Tensor, Tensor]:
        scores, classes = torch.max(
            torch.nn.functional.softmax(self.net(inputs[self.level]), dim=1), dim=1
        )
        return scores, classes

    def training_step(
        self, inputs: list[Tensor], labels: Tensor
    ) -> tuple[Tensor, dict[str, float]]:
        logits = self.net(inputs[self.level])
        loss = torch.nn.functional.cross_entropy(
            logits,
            labels,
            weight=self.label_weights,
            label_smoothing=self.label_smoothing,
        )
        return loss, {}

    def on_validation_start(self) -> None:
        self.accuracy_computer = MulticlassAccuracy(num_classes=self.num_classes)
        self.precision_computer = MulticlassPrecision(num_classes=self.num_classes)
        self.recall_computer = MulticlassRecall(num_classes=self.num_classes)

    def validation_step(
        self, inputs: list[Tensor], labels: Tensor
    ) -> tuple[Tensor, dict[str, float]]:
        input = inputs[self.level]
        self.accuracy_computer = self.accuracy_computer.to(input.device)
        self.precision_computer = self.precision_computer.to(input.device)
        self.recall_computer = self.recall_computer.to(input.device)
        logits = self.net(input)
        loss = torch.nn.functional.cross_entropy(
            logits,
            labels,
            weight=self.label_weights,
            label_smoothing=self.label_smoothing,
        )
        self.accuracy_computer.update(logits, labels)
        self.precision_computer.update(logits, labels)
        self.recall_computer.update(logits, labels)
        return loss, {}

    def on_validation_end(self) -> dict[str, float]:
        return {
            "accuracy": self.accuracy_computer.compute().item(),
            "precision": self.precision_computer.compute().item(),
            "recall": self.recall_computer.compute().item(),
        }
