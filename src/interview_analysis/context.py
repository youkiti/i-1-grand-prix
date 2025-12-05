"""
パイプライン実行コンテキスト

処理の過程を追跡し、レポート用のメタデータを生成する。
"""
import time
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional


@dataclass
class ProcessingStep:
    """処理ステップの記録"""
    name: str
    phase: str  # e.g., "Map", "Reduce", "Compare"
    input_count: int
    output_count: int
    model: str
    start_time: float = field(default_factory=time.time)
    end_time: Optional[float] = None
    details: Dict[str, Any] = field(default_factory=dict)
    
    def complete(self) -> None:
        """ステップ完了を記録"""
        self.end_time = time.time()
    
    @property
    def duration_seconds(self) -> float:
        if self.end_time is None:
            return 0
        return self.end_time - self.start_time
    
    @property
    def duration_str(self) -> str:
        secs = self.duration_seconds
        mins = int(secs // 60)
        secs = int(secs % 60)
        return f"{mins}m {secs:02d}s"


@dataclass
class DataSource:
    """データソースの記録"""
    name: str
    path: str
    count: int
    unit: str = "件"  # e.g., "ファイル", "コメント"


class PipelineContext:
    """パイプライン実行コンテキスト"""
    
    def __init__(self, pipeline_name: str, focus: str = ""):
        self.pipeline_name = pipeline_name
        self.focus = focus
        self.created_at = datetime.now()
        self.data_sources: List[DataSource] = []
        self.steps: List[ProcessingStep] = []
        self.tree_reduce_stats: Dict[str, Any] = {}
        self._current_step: Optional[ProcessingStep] = None
    
    def add_data_source(self, name: str, path: str, count: int, unit: str = "件") -> None:
        """データソースを追加"""
        self.data_sources.append(DataSource(name, path, count, unit))
    
    def start_step(self, name: str, phase: str, input_count: int, model: str, **details) -> ProcessingStep:
        """処理ステップを開始"""
        step = ProcessingStep(
            name=name,
            phase=phase,
            input_count=input_count,
            output_count=0,
            model=model,
            details=details
        )
        self._current_step = step
        return step
    
    def complete_step(self, output_count: int = 1, **extra_details) -> None:
        """現在のステップを完了"""
        if self._current_step:
            self._current_step.output_count = output_count
            self._current_step.details.update(extra_details)
            self._current_step.complete()
            self.steps.append(self._current_step)
            self._current_step = None
    
    def record_tree_reduce(self, initial_batches: int, levels: List[int]) -> None:
        """ツリーReduceの統計を記録"""
        self.tree_reduce_stats = {
            "initial_batches": initial_batches,
            "levels": levels,
            "total_levels": len(levels)
        }
    
    def render_metadata_section(self) -> str:
        """メタデータセクションをMarkdownで生成"""
        lines = []
        lines.append("\n\n---\n")
        lines.append("# 処理メタデータ\n")
        
        # データソース
        if self.data_sources:
            lines.append("## データソース\n")
            lines.append("| 種別 | パス | 件数 |")
            lines.append("|------|------|------|")
            for ds in self.data_sources:
                lines.append(f"| {ds.name} | `{ds.path}` | {ds.count:,} {ds.unit} |")
            lines.append("")
        
        # 処理パイプライン
        lines.append("## 処理パイプライン\n")
        
        # ステップをフェーズごとにグループ化
        current_phase = None
        for step in self.steps:
            if step.phase != current_phase:
                current_phase = step.phase
                lines.append(f"### {step.phase}\n")
            
            details_str = ""
            if step.details:
                detail_parts = [f"{k}: {v}" for k, v in step.details.items() if k not in ["tree_levels"]]
                if detail_parts:
                    details_str = f" ({', '.join(detail_parts)})"
            
            lines.append(f"- **{step.name}**: {step.input_count:,}入力 → {step.output_count:,}出力{details_str}")
            lines.append(f"  - モデル: `{step.model}`")
            if step.duration_seconds > 0:
                lines.append(f"  - 処理時間: {step.duration_str}")
            lines.append("")
        
        # ツリーReduce統計
        if self.tree_reduce_stats:
            lines.append("## ツリーReduce統計\n")
            stats = self.tree_reduce_stats
            lines.append(f"- 初期バッチ数: {stats['initial_batches']}")
            lines.append(f"- 並列レベル数: {stats['total_levels']}")
            if stats.get('levels'):
                level_str = " → ".join([f"L{i+1}:{n}ペア" for i, n in enumerate(stats['levels'])])
                lines.append(f"- レベル詳細: {level_str}")
            lines.append("")
        
        # 処理統計サマリー
        if self.steps:
            lines.append("## 処理統計サマリー\n")
            lines.append("| ステップ | 入力 | 出力 | 時間 |")
            lines.append("|---------|------|------|------|")
            for step in self.steps:
                lines.append(f"| {step.name} | {step.input_count:,} | {step.output_count:,} | {step.duration_str} |")
            
            # 合計時間
            total_time = sum(s.duration_seconds for s in self.steps)
            total_mins = int(total_time // 60)
            total_secs = int(total_time % 60)
            lines.append(f"| **合計** | - | - | **{total_mins}m {total_secs:02d}s** |")
            lines.append("")
        
        lines.append(f"\n*生成日時: {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}*\n")
        
        return "\n".join(lines)


# グローバルコンテキスト（パイプライン実行中に使用）
_current_context: Optional[PipelineContext] = None


def create_context(pipeline_name: str, focus: str = "") -> PipelineContext:
    """新しいパイプラインコンテキストを作成"""
    global _current_context
    _current_context = PipelineContext(pipeline_name, focus)
    return _current_context


def get_context() -> Optional[PipelineContext]:
    """現在のコンテキストを取得"""
    return _current_context
