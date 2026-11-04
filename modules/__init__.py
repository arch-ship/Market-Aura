"""
Modules package for Game Theory Market Strategy & IR Verification Engine.
Exposes Stages 1 through 6 for seamless imports across FastAPI and CLI runners.
"""

from .stage1_ingestion_crawler import (
    DocumentParser,
    QueryFormulator,
    WebAndSocialCrawler,
)
from .stage2_indexer import TextPreprocessor, DocumentIndexer
from .stage3_retrieval import RetrievalEngine
from .stage4_reliability import ReliabilityAndMiningEngine
from .stage5_ranking_qa import HybridRankingQAEngine
from .stage6_game_theory import GameTheoryIndustryEngine

__all__ = [
    "DocumentParser",
    "QueryFormulator",
    "WebAndSocialCrawler",
    "TextPreprocessor",
    "DocumentIndexer",
    "RetrievalEngine",
    "ReliabilityAndMiningEngine",
    "HybridRankingQAEngine",
    "GameTheoryIndustryEngine",
]