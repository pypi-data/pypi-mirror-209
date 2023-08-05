import logging

import nltk

from prompt_optimizer.poptim.autocorrect_optim import AutocorrectOptim
from prompt_optimizer.poptim.base import PromptOptimize
from prompt_optimizer.poptim.entropy_optim import EntropyOptim
from prompt_optimizer.poptim.lemmatizer_optim import LemmatizerOptim
from prompt_optimizer.poptim.name_replace_optim import NameReplaceOptim
from prompt_optimizer.poptim.pulp_optim import PulpOptim
from prompt_optimizer.poptim.punctuation_optim import PunctuationOptim
from prompt_optimizer.poptim.sequential import Sequential
from prompt_optimizer.poptim.stemmer_optim import StemmerOptim
from prompt_optimizer.poptim.stop_word_optim import StopWordOptim
from prompt_optimizer.poptim.synonym_replace_optim import SynonymReplaceOptim

nltk.download("wordnet")
nltk.download("punkt")
nltk.download("averaged_perceptron_tagger")
nltk.download("maxent_ne_chunker")
nltk.download("words")

__all__ = [
    "Sequential",
    "PromptOptimize",
    "LemmatizerOptim",
    "StopWordOptim",
    "NameReplaceOptim",
    "PunctuationOptim",
    "PulpOptim",
    "StemmerOptim",
    "AutocorrectOptim",
    "SynonymReplaceOptim",
    "EntropyOptim",
]

logger = logging.getLogger(__name__)
