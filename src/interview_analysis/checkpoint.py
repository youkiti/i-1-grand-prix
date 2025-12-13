"""
チェックポイント機能

パイプラインの中間状態を保存・復元するためのユーティリティ。
"""
import json
import hashlib
import shutil
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple


def _compute_source_hash(source_path: Path) -> str:
    """ソースディレクトリ/ファイルのハッシュを計算（変更検出用）"""
    if source_path.is_file():
        content = source_path.read_bytes()
        return hashlib.md5(content).hexdigest()[:12]
    
    # ディレクトリの場合はファイル名リストのハッシュ
    files = sorted([p.name for p in source_path.iterdir() if p.is_file() and not p.name.startswith(".")])
    return hashlib.md5("|".join(files).encode()).hexdigest()[:12]


class Checkpoint:
    """チェックポイント管理クラス"""
    
    def __init__(self, checkpoint_dir: Path, source_path: Path, mode: str, focus: str):
        """
        Args:
            checkpoint_dir: チェックポイントを保存するベースディレクトリ
            source_path: ソースデータのパス（ディレクトリまたはファイル）
            mode: パイプラインモード（pre_hypothesis_iterative, pubcom_analysis）
            focus: 分析のフォーカス
        """
        self.checkpoint_dir = checkpoint_dir
        self.source_path = source_path
        self.mode = mode
        self.focus = focus
        
        # 一意のセッションIDを生成（ソース + モード + フォーカスに基づく）
        source_hash = _compute_source_hash(source_path)
        focus_hash = hashlib.md5(focus.encode()).hexdigest()[:8] if focus else "nofocus"
        self.session_id = f"{mode}_{source_path.name}_{source_hash}_{focus_hash}"
        
        # セッション固有のディレクトリ
        self.session_dir = checkpoint_dir / self.session_id
        self.session_dir.mkdir(parents=True, exist_ok=True)
        
        # 古いセッションをクリーンアップ（同じモードで異なるセッションID）
        self._cleanup_old_sessions()
        
        # チェックポイントファイルのパス
        self.part1_file = self.session_dir / "part1_results.json"
        self.part2_state_file = self.session_dir / "part2_state.json"
        self.metadata_file = self.session_dir / "metadata.json"
        self.map_batches_dir = self.session_dir / "map_batches"  # インクリメンタルMap保存用
        
        # メタデータを保存
        self._save_metadata()
    
    def _cleanup_old_sessions(self) -> None:
        """同じモードで異なるセッションIDの古いチェックポイントを削除"""
        if not self.checkpoint_dir.exists():
            return
        
        prefix = f"{self.mode}_"
        for old_dir in self.checkpoint_dir.iterdir():
            if old_dir.is_dir() and old_dir.name.startswith(prefix) and old_dir.name != self.session_id:
                try:
                    shutil.rmtree(old_dir)
                    print(f"[Checkpoint] Cleaned up old session: {old_dir.name}", flush=True)
                except Exception as e:
                    print(f"[Checkpoint] Warning: Could not clean up {old_dir.name}: {e}", flush=True)
    
    def _save_metadata(self) -> None:
        """メタデータを保存"""
        metadata = {
            "session_id": self.session_id,
            "mode": self.mode,
            "source_path": str(self.source_path),
            "focus": self.focus,
            "created_at": datetime.now().isoformat(),
        }
        self.metadata_file.write_text(json.dumps(metadata, ensure_ascii=False, indent=2), encoding="utf-8")
    
    # --- Part 1 チェックポイント ---
    
    def has_part1_checkpoint(self) -> bool:
        """Part 1のチェックポイントが存在するか"""
        return self.part1_file.exists()
    
    def save_part1(self, results: List[Tuple[str, str]]) -> None:
        """
        Part 1の結果を保存
        
        Args:
            results: [(filename, output), ...] のリスト
        """
        data = {
            "completed_at": datetime.now().isoformat(),
            "count": len(results),
            "results": [{"filename": fn, "output": out} for fn, out in results],
        }
        self.part1_file.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"[Checkpoint] Part 1 saved: {len(results)} items -> {self.part1_file}", flush=True)
    
    def load_part1(self) -> Optional[List[Tuple[str, str]]]:
        """
        Part 1の結果を読み込み
        
        Returns:
            [(filename, output), ...] のリスト、またはNone
        """
        if not self.part1_file.exists():
            return None
        
        data = json.loads(self.part1_file.read_text(encoding="utf-8"))
        results = [(item["filename"], item["output"]) for item in data["results"]]
        print(f"[Checkpoint] Part 1 loaded: {len(results)} items from {self.part1_file}", flush=True)
        return results
    
    # --- Map バッチ インクリメンタルチェックポイント ---
    
    def save_map_batch(self, batch_index: int, batch_id: str, output: str) -> None:
        """
        個別Mapバッチ結果を保存（スレッドセーフ）
        
        Args:
            batch_index: バッチのインデックス (0-based)
            batch_id: バッチの識別子
            output: 処理結果
        """
        self.map_batches_dir.mkdir(exist_ok=True)
        batch_file = self.map_batches_dir / f"batch_{batch_index:04d}.json"
        data = {
            "batch_id": batch_id,
            "output": output,
            "saved_at": datetime.now().isoformat()
        }
        batch_file.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
        print(f"[Checkpoint] Map batch {batch_index} saved -> {batch_file}", flush=True)
    
    def load_partial_map_results(self) -> Dict[int, Tuple[str, str]]:
        """
        保存済みMapバッチ結果を読み込み
        
        Returns:
            {batch_index: (batch_id, output)} の辞書
        """
        if not self.map_batches_dir.exists():
            return {}
        
        results = {}
        for f in self.map_batches_dir.glob("batch_*.json"):
            try:
                idx = int(f.stem.split("_")[1])
                data = json.loads(f.read_text(encoding="utf-8"))
                results[idx] = (data["batch_id"], data["output"])
            except (ValueError, KeyError, json.JSONDecodeError) as e:
                print(f"[Checkpoint] Warning: Could not load {f}: {e}", flush=True)
        
        if results:
            print(f"[Checkpoint] Loaded {len(results)} partial Map results", flush=True)
        return results
    
    def get_completed_batch_indices(self) -> set:
        """完了済みMapバッチのインデックス一覧を取得"""
        return set(self.load_partial_map_results().keys())
    
    def consolidate_map_batches(self, total_batches: int) -> Optional[List[Tuple[str, str]]]:
        """
        全Mapバッチが完了していれば、Part 1形式に統合
        
        Returns:
            全バッチ完了時は [(batch_id, output), ...] のリスト、未完了時はNone
        """
        partial = self.load_partial_map_results()
        if len(partial) < total_batches:
            return None
        
        # インデックス順にソートして返す
        results = [partial[i] for i in range(total_batches) if i in partial]
        if len(results) == total_batches:
            return results
        return None
    
    # --- Part 2 チェックポイント ---
    
    def has_part2_checkpoint(self) -> bool:
        """Part 2のチェックポイントが存在するか"""
        return self.part2_state_file.exists()
    
    def save_part2_state(self, batch_index: int, current_state: str) -> None:
        """
        Part 2の中間状態を保存
        
        Args:
            batch_index: 完了したバッチのインデックス（0-based）
            current_state: 現在のQ&A/レポート状態
        """
        data = {
            "saved_at": datetime.now().isoformat(),
            "completed_batch_index": batch_index,
            "current_state": current_state,
        }
        self.part2_state_file.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"[Checkpoint] Part 2 batch {batch_index + 1} saved -> {self.part2_state_file}", flush=True)
    
    def load_part2_state(self) -> Optional[Tuple[int, str]]:
        """
        Part 2の中間状態を読み込み
        
        Returns:
            (completed_batch_index, current_state) のタプル、またはNone
        """
        if not self.part2_state_file.exists():
            return None
        
        data = json.loads(self.part2_state_file.read_text(encoding="utf-8"))
        batch_index = data["completed_batch_index"]
        current_state = data["current_state"]
        print(f"[Checkpoint] Part 2 loaded: resuming from batch {batch_index + 2}", flush=True)
        return batch_index, current_state
    
    # --- クリーンアップ ---
    
    def clear(self) -> None:
        """全てのチェックポイントを削除"""
        if self.part1_file.exists():
            self.part1_file.unlink()
        if self.part2_state_file.exists():
            self.part2_state_file.unlink()
        if self.map_batches_dir.exists():
            shutil.rmtree(self.map_batches_dir)
        print(f"[Checkpoint] Cleared: {self.session_dir}", flush=True)


def get_checkpoint(
    source_path: Path,
    mode: str,
    focus: str,
    checkpoint_dir: Optional[Path] = None
) -> Checkpoint:
    """
    チェックポイントインスタンスを取得
    
    Args:
        source_path: ソースデータのパス
        mode: パイプラインモード
        focus: 分析のフォーカス
        checkpoint_dir: チェックポイントディレクトリ（デフォルト: doc/checkpoints）
    
    Returns:
        Checkpoint インスタンス
    """
    if checkpoint_dir is None:
        checkpoint_dir = Path("doc/checkpoints")
    
    return Checkpoint(checkpoint_dir, source_path, mode, focus)
