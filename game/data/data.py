import sys
sys.path.append("/media/cabrera/LF/Developing/New/Python/comm-draft/")

import pandas as pd
from game.config import Config

config = Config()

df = pd.read_csv(config.QUESTION_ANSWER_CSV_PATH)


print(len(df['question'].max()))