# -*- coding: utf-8 -*-
from chatterbot import ChatBot
import logging
from chatterbot.trainers import ChatterBotCorpusTrainer



chatterbot = ChatBot('Terminal',
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    logic_adapters=[
        "chatterbot.logic.MathematicalEvaluation",
       
        {
         "import_path": "chatterbot.logic.BestMatch",
        "response_selection_method":"chatterbot.response_selection.get_first_response" ,
         "statement_comparison_function": "chatterbot.comparisons.levenshtein_distance"
        }
    ],
    filters=[
        'chatterbot.filters.RepetitiveResponseFilter'
    ],
    input_adapter='chatterbot.input.TerminalAdapter',
    output_adapter='chatterbot.output.TerminalAdapter',
    database='chatterbot-database'
)
chatterbot.set_trainer(ChatterBotCorpusTrainer)

chatterbot.train(
      "chatterbot.corpus.english.greetings",
    "chatterbot.corpus.english.conversations"
    )
print('Type something to begin...')

while True:
    try:
        bot_input = chatterbot.get_response(None)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break